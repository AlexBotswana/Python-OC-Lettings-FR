"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

import os
import sys
import django
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env si nécessaire
load_dotenv()

# Ajouter le chemin du projet au sys.path
project_path = os.path.abspath('../..')
# print(f"Project path: {project_path}")  # Ajouté pour le débogage
sys.path.insert(0, project_path)

# Définir le module de réglages de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
# Ajouté pour le débogage
# print(f"DJANGO_SETTINGS_MODULE: {os.environ['DJANGO_SETTINGS_MODULE']}")

# Initialiser Django
django.setup()

# Informations sur le projet
project = 'oc-lettings-doc'
copyright = '2024, Alexis Aubry'
author = 'Alexis Aubry'
release = '1'

# Configuration générale
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
templates_path = ['_templates']
exclude_patterns = []

# Options pour HTML output
html_theme = 'alabaster'
html_static_path = ['_static']
