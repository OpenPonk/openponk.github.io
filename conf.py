# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'OpenPonk modeling platform'
copyright = u'2018, Peter Uhnak'
author = u'Peter Uhnak'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''


# <CustomRoles>
from docutils import nodes
import posixpath
from sphinx.writers.html import HTMLTranslator
from sphinx.addnodes import download_reference

class download_link(nodes.reference):
    """Node for external download link references."""

def visit_download_link(self, node):
    self.body.append(
        '<a class="reference download external" href="%s" onclick="%s">' % (node.refuri, node['onclick'])
    )
    self.context.append('</a>')

    def visit_reference(self, node):
        # type: (nodes.Node) -> None
        atts = {'class': 'reference'}
        if node.get('internal') or 'refuri' not in node:
            atts['class'] += ' internal'
        else:
            atts['class'] += ' external'
        if 'refuri' in node:
            atts['href'] = node['refuri'] or '#'
            if self.settings.cloak_email_addresses and \
               atts['href'].startswith('mailto:'):
                atts['href'] = self.cloak_mailto(atts['href'])
                self.in_mailto = 1
        else:
            assert 'refid' in node, \
                   'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts['class'] += ' image-reference'
        if 'reftitle' in node:
            atts['title'] = node['reftitle']
        if 'target' in node:
            atts['target'] = node['target']
        self.body.append(self.starttag(node, 'a', '', **atts))

        if node.get('secnumber'):
            self.body.append(('%s' + self.secnumber_suffix) %
                             '.'.join(map(str, node['secnumber'])))

def visit_reference(self, node):
    # type: (nodes.Node) -> None
    atts = {'class': 'reference'}
    if node.get('internal') or 'refuri' not in node:
        atts['class'] += ' internal'
    else:
        atts['class'] += ' external'
    if 'refuri' in node:
        atts['href'] = node['refuri'] or '#'
        if self.settings.cloak_email_addresses and \
           atts['href'].startswith('mailto:'):
            atts['href'] = self.cloak_mailto(atts['href'])
            self.in_mailto = 1
    else:
        assert 'refid' in node, \
               'References must have "refuri" or "refid" attribute.'
        atts['href'] = '#' + node['refid']
    if not isinstance(node.parent, nodes.TextElement):
        assert len(node) == 1 and isinstance(node[0], nodes.image)
        atts['class'] += ' image-reference'
    if 'reftitle' in node:
        atts['title'] = node['reftitle']
    if 'target' in node:
        atts['target'] = node['target']
    if 'onclick' in node:
        atts['onclick'] = node['onclick']
    self.body.append(self.starttag(node, 'a', '', **atts))

    if node.get('secnumber'):
        self.body.append(('%s' + self.secnumber_suffix) %
                         '.'.join(map(str, node['secnumber'])))

def depart_download_link(self, node):
    self.depart_reference(node)

def setup(app):
    app.add_role('download-link', download_link_role)
    app.add_node(nodes.reference, html=(visit_reference, HTMLTranslator.depart_reference))

def download_link_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    "text = plugin,version,platform"
    parts = text.split(',')
    plugin = parts[0]
    version = parts[1]
    platform = parts[2]
    url = 'https://openponk.ccmi.fit.cvut.cz/builds/' + plugin + '/openponk-' + platform + '-' + version + '.zip'
    node = nodes.reference(rawtext, 'download', refuri=url)
    node['onclick'] = "ga('send', 'event', 'Downloads', 'download', 'uml-" + platform + "-stable')"
    return [node],[]

# </CustomRoles>

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

#import guzzle_sphinx_theme
#html_theme = 'guzzle_sphinx_theme'
#html_theme_path = guzzle_sphinx_theme.html_theme_path()

#import sphinx_bootstrap_theme
#html_theme = 'bootstrap'
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = { }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'OpenPonkmodelingplatformdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'OpenPonkmodelingplatform.tex', u'OpenPonk modeling platform Documentation',
     u'Peter Uhnak', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'openponkmodelingplatform', u'OpenPonk modeling platform Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'OpenPonkmodelingplatform', u'OpenPonk modeling platform Documentation',
     author, 'OpenPonkmodelingplatform', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------
