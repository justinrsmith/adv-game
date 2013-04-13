try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'Justin Smith',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'justinrsmith88@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['adv'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)