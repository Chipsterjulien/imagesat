#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time, Image, yaml, requests, logging, urllib, io

# Depend of python-yaml, python-imaging and python-requests





class Img_info:
	def __init__(self):
		self.base    = str()    # Définit la chaine à rajouter à la recherche
		self.url     = str()    # Contient l'adresse internet
		self.search  = str()    # Définit la chaine à rechercher
		self._path   = str()    # Définit l'emplacement pour la sauvegarde
		self._time   = int()    # Définit le temps avant la mise à jour
		self._crop   = []       # Tableau contenant les dimensions à découper
		self._resize = []       # Tableau contenant les nouvelles dimensions de l'image

# Getter
	def _get_crop(self):
		return self._crop

	def _get_path(self):
		return self._path

	def _get_resize(self):
		return self._resize

	def _get_time(self):
		return self._time


# Setter
	def _set_crop(self, c):
		for val in c.split('x'):
			if is_number(val):
				self._crop.append(int(val))
			else:
				logging.critical("In " + self._path + " \"crop: " + c + "\" is incorrect !")
				sys.exit(2)

	def _set_path(self, p):
		(path, f) = os.path.split(p)
		if path == "":
			path = os.path.expanduser('~')

		if not os.access(path, os.W_OK):
			logging.critical("You don't have write permissions on \"" + self._path + "\" !")
			sys.exit(2)

		self._path = os.path.join(path, f)

	def _set_resize(self, r):
		for val in r.split('x'):
			if is_number(val):
				self._resize.append(int(val))
			else:
				logging.critical("In " + self._path + " \"resize: " + r + "\" is incorrect !")
				sys.exit(2)

	def _set_time(self, t):
		if is_number(t):
			self._time = t
		else:
			logging.critical("\"" + t + "\" is not a number gretter than 0 !")
			sys.exit(2)


	crop   = property(_get_crop, _set_crop)
	path   = property(_get_path, _set_path)
	resize = property(_get_resize, _set_resize)
	time   = property(_get_time, _set_time)




#--------------------------

def is_number(number):
	try:
		s = int(number)
		if s < 0:
			return False
		else:
			return True
	except ValueError:
		return False


def download(url):
	page = str()
	try:
		page = requests.get(url)
	except requests.exceptions.ConnectionError:
		time.sleep(10)
		os.execl('/usr/bin/imagesat', 'imagesat')

	return page




######
# Début du programme principal
############

list_picture = []
error_file   = "/var/log/imagesat/error.log"
conf_file    = "/etc/imagesat.conf"
logging.basicConfig(filename=error_file, format='%(asctime)s %(message)s', level=logging.WARNING)

# On teste si on a bien les droits d'écritures sur error_file
(path, f) = os.path.split(error_file)
if not os.access(path, os.W_OK):
	print("You don't have the right permissions on " + error_file + " !", file=sys.stderr)
	sys.exit(2)

# On regarde si le fichier de configuration existe et qu'on a les droits de lecture
if not os.path.isfile(conf_file):
	logging.critical("The \"" + conf_file + "\" don't exist !")
	print("The \"" + conf_file + "\" don't exist !")
	sys.exit(2)
if not os.access(conf_file, os.R_OK):
	logging.critical("You don't have the right permissions to read \"" + conf_file + "\" !")
	print("You don't have the right permissions to read \"" + conf_file + "\" !", file=sys.stderr)
	sys.exit(2)

# On récupère les données du fichier de configuration
data = str()
try:
	file_yaml = open(conf_file, 'r')
	data = yaml.load(file_yaml.read())
	file_yaml.close()
except yaml.parser.ParserError as e:
	print(e)
	sys.exit(2)

# On range les infos correctement pour les exploiter derrière
try:
	for pic_name in data:
		picture = Img_info()
		for info in data[pic_name]:
			for key, val in info.items():
				if key == 'url':
					picture.url = val
				elif key == 'path_sav':
					picture.path = val
				elif key == 'update':
					picture.time = val
				elif key == 'crop':
					picture.crop = val
				elif key == 'resize':
					picture.resize = val
				elif key == 'search':
					picture.search = val
				elif key == 'base_url':
					picture.base = val
				else:
					logging.warning("In config file, \"" + key + "\" is unknown !")
		list_picture.append(picture)
except AttributeError as e:
	logging.error("There is a big mistake in config file. See the example !")
	sys.exit(1)

# On vérifie que nous avons récupérer des données
if len(list_picture) == 0:
	logging.critical("The file \"" + conf_file + "\" is empty !")
	sys.exit(2)

# On détermine le temps pour s'endormir le plus court
t = []
for pic in list_picture:
	t.append(pic.time)
time2sleep = min(t)
del(t)


# Début de la boucle while 1
while 1:
	# On traite les informations récupérées pour chaque image
	copy_time2sleep = time2sleep
	for i, pic in enumerate(list_picture):
		must_download = False
		now           = time.time()

		# On regarde si l'image existe
		if os.path.isfile(pic.path):
			# On vérifie qu'on a les droits en écriture
			if not os.access(pic.path, os.W_OK):
				logging.warning("You don't have write permissions on \"" + pic.path + "\" !")
				del list_picture[i]
				if len(list_picture) == 0:
					logging.error("There is no picture in the list since there is a mistake in the config file, so I'll stop !")
					sys.exit(2)
				else:
					copy_time2sleep(0.1)
					continue

			time_image = os.stat(pic.path)[8]
		
			if time_image + pic.time <= now:
				must_download = True

		# Si l'image n'existe pas, on la télécharge
		else:
			must_download = True

		if must_download:
			if pic.search:
				# On télécharge la page où se trouve les informations sur l'image
				page = download(pic.url)

				if page.status_code != requests.codes.ok:
					logging.warning(pic.url + " isn't a valid url ! Error code : " + str(page.status_code))
					del list_picture[i]
					if len(list_picture) == 0:
						logging.error("There is no picture in the list since there is a mistake in the config file, so I'll stop !")
						sys.exit(2)
					else:
						copy_time2sleep = 0.1
						continue

				for word in page.content.decode('utf-8', 'ignore').split(" "):
					if pic.search in word:
						pic.url = word.split('=')[1][1:-1]
						if pic.base:
							pic.url = urllib.parse.urljoin(pic.base, pic.url)


			# On télécharge l'image
			req = download(pic.url)

			if req.status_code != requests.codes.ok:
				logging.warning(pic.url + " isn't a valid url ! Error code : " + str(page.status_code))
				del list_picture[i]
				if len(list_picture) == 0:
					logging.error("There is no picture in the list since there is a mistake in the config file, so I'll stop !")
					sys.exit(2)
				else:
					copy_time2sleep = 0.1
					continue

			# Si on a les infos pour découper et/ou redimensionné on les applique
			if pic.crop or pic.resize:
				# On charge l'image en mémoire avant d'y appliquer les modifications
				image_src = Image.open(io.BytesIO(req.content))
				if pic.crop:
					image_src = image_src.crop(pic.crop)
				if pic.resize:
					image_src = image_src.resize((pic.resize), Image.ANTIALIAS)

				# On sauvegarde l'image à l'emplacement indiqué
				image_src.save(pic.path)

			else:
				with open(pic.path, 'wb') as e:
					e.write(req.content)

		else:
			# On calcule le temps avant la prochaine mise à jour
			time_remaining = time_image + pic.time - now

			if time_remaining < copy_time2sleep:
				copy_time2sleep = time_remaining


	# Boucle "intelligente" pour prendre en compte l'hibernation et la veille
	loop = True
	while loop:
		# On récupère l'heure
		time_tmp = time.time()
		# Si on a dormi trop longtemps, on quitte la boucle
		if now + copy_time2sleep < time_tmp:
			loop = False

		# Sinon on va s'endormir et se réveiller régulièrement
		else:
			# On calcule le temps qu'il nous reste à dormir
			rest = (now + copy_time2sleep) - time_tmp
			# S'il est inférieur à 2s par besoin de se rendormir inutilement
			if rest < 2:
				loop = False
			# S'il est inférieur à 120s, on se rendort du temps qu'il reste
			elif rest < 120:
				time.sleep(rest)
			# Autrement, on s'endort pendant 120s
			else:
				time.sleep(120)
