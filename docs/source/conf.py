# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test'
copyright = '2025, Ve Samy'
author = 'Ve Samy'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 'sphinx_copybutton',  'sphinx_new_tab_link','sphinx_favicon']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

html_static_path = ['_static']
def setup(app):
    app.add_css_file("custom.css")

sphinxemoji_style = 'twemoji'
favicons = [
{
    "sizes": "32x32",
    "href": "favicon.png",
}
]
html_logo = "_static/logo.png"