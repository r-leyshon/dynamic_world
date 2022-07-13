# dynamic_world documentation build configuration file
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this autogenerated
# file.
#
# All configuration values have a default; values that are commented out serve to show
# the default.

# If extensions (or modules to document with autodoc) are in another directory, add
# these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "4.0"

# Add any Sphinx extension module names here, as strings. They can be extensions coming
# with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.  You can specify multiple suffix as a list of
# string:
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "dynamic_world"
author = "Your GitHub/GitLab organisation name, for example ukgovdatascience"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the built
# documents.
# The short X.Y.Z version.
version = "0.0.1"
# The full version, including alpha/beta/rc tags.
release = "0.0.1"

# List of patterns, relative to source directory, that match files and directories to
# ignore when looking for source files. These patterns also affect html_static_path and
# html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

# -- Options for HTML output -----------------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of
# builtin themes.
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme further.
# For a list of options available for each theme, see the documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents. "<project> v<release> documentation" by
# default.
# html_title = "None"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top of the
# sidebar.
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of the
# docs. This file should be a
# Windows icon file (.ico) being 16x16 or 32x32 pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here, relative
# to this directory. They are copied after the builtin static files, so a file named
# "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or .htaccess) here,
# relative to this directory. These files are copied directly to the root of the
# documentation.
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page bottom, using
# the given strftime format. The empty string is equivalent to '%b %d, %Y'.
# html_last_updated_fmt = None

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to template
# names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will contain a
# <link> tag referring to it. The value of this option must be the base URL from
# which the finished HTML is served.
# html_use_opensearch = ""

# This is the file name suffix for HTML files (for example ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index. Sphinx supports
# the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
# html_search_language = "en"

# A dictionary with options for the search language support, empty by default. 'ja'
# uses this config value. 'zh' user can custom change `jieba` dictionary path.
# html_search_options = {"type": "default"}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = "scorer.js"

# Output file base name for HTML help builder.
htmlhelp_basename = "dynamic_worlddoc"

# -- Options for autosection output ----------------------------------------------------

# Prefix document path to section labels, otherwise autogenerated labels would look
# like 'heading' rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# -- Options for autosummary output ----------------------------------------------------

# Set the autosummary to generate stub files
autosummary_generate = True

# -- Options for Napoleon extension ----------------------------------------------------

# Napoleon settings to enable parsing of Google- and NumPy-style docstrings.
# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = False
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = True
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True

# -- Options for MyST ------------------------------------------------------------------

# Enforce heading anchors for h1 to h6 headings
myst_heading_anchors = 6

# Enable MyST extensions
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]
