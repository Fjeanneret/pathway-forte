# -*- coding: utf-8 -*-

import os
import re
import sys

sys.path.insert(0, os.path.abspath('../../src'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinx_click.ext',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'PathwayForte'
copyright = '2019, Daniel Domingo-Fernández and Sarah Mubeen'
author = 'Daniel Domingo-Fernández and Sarah Mubeen'

release = '0.0.1-dev'

parsed_version = re.match(
    '(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:-(?P<release>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+(?P<build>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?',
    release
)
version = parsed_version.expand('\g<major>.\g<minor>.\g<patch>')

tags = set()

if parsed_version.group('release'):
    tags.add('prerelease')

language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
html_static_path = []
htmlhelp_basename = 'pathway_forte_doc'
latex_elements = {}
latex_documents = [
    (master_doc, 'pathway_forte.tex', 'PathwayForte Documentation',
     'Sarah Mubeen and Daniel Domingo-Fernández', 'manual'),
]
man_pages = [
    (master_doc, 'pathway_forte', 'PathwayForte Documentation', [author], 1)
]
texinfo_documents = [
    (master_doc, 'PathwayForte', 'PathwayForte Documentation', author, 'PathwayForte'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'networkx': ('https://networkx.github.io/', None),
    'sqlalchemy': ('https://docs.sqlalchemy.org/en/latest', None),
    'pybel': ('https://pybel.readthedocs.io/en/latest/', None),
}

autodoc_member_order = 'bysource'
autoclass_content = 'both'

if os.environ.get('READTHEDOCS'):
    tags.add('readthedocs')
