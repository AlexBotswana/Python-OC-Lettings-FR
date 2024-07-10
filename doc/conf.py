# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django


# Ajouter le chemin de votre projet Django
sys.path.insert(0, os.path.abspath('../../PYTHON-OC-LETTINGS-FR'))

# Configuration de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
django.setup()

project = 'oc-lettings-doc'
copyright = '2024, Alexis Aubry'
author = 'Alexis Aubry'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
