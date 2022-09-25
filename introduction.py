"""web scraping"""

"""
- HTML: Content management and organization.
- CSS: Management of the appearance of the web page (Layout, decoration, colors, text size, etc...)."""

# html
"""
- Tags in pairs: They open, contain text, and close. <title>This is a title</title>.
- The / character indicates that this is a closing tag."""

# example
# <title>The Wall-Git</title>

"""
- Orphan tags: These are tags used to insert an element at a specific location (for example an image, a link).
- It is not necessary to delimit the beginning and the end. An orphan tag is written like this: <tag />"""

# example:
# <img src= {{ url_for('static',filename='images/3.gif')}} height="40%" width="100%"/>

"""
- Attributes complement tags to provide additional information.
- The attribute is placed after the name of the opening tag and most often has a value, like this: <beacon attribute="value">.
- For example, in an orphan tag inserting an image, we generally add an attribute that indicates the 
address of the image to display <img src="image.jpg" />."""

"""Exemples de balises HTML"""
# Balises	Rôle
# <html>...</html>	Encadre tout le code HTML (balise principale)
# <head>...</head>	En tête de la page
# <body>...</body>	Corps de la page
# <h1> <h2>...<h6>	Titres
# <img src="lien" />	Image
# <a href="lien"> </a>	Lien hypertexte
# <p>...</p>	Paragraphe
# <ul>...</ul>	Liste à puces (non numérotée)
# <ol>...</ol>	Liste à puces (numérotée)
# <li>...</li>	Eléments de liste à puces
# <table>...</table>	Table
# <tbody>...</tbody>	Corps d'une table (regroupe une ou plusieurs balises <tr>)
# <tr>...</tr>	Ligne d'une table
# <td>...</td>	Cellule d'une table
# <div>...</div>	Division du contenu (prend un sens lorsqu'elle est associée à un attribut)
# <script>...</script>	Code JavaScript
# ------------------------------------------------------------------------------------------------
"""Basic structure of an HTML page"""
# <!DOCTYPE html>
# <html>
#
#   <head>
#       <title>The Wall-Git</title>
#       <meta charset="utf-8">
#   </head>
#
#   <body>
#
#   </body>
# </html>
"""
- The HTML element: made up of a pair of opening <html> and closing </html> tags. 
The html element will represent our page, we will insert all the content of our page inside it.
- The head element: <head> is a header element. It will contain elements that will be used to provide
 information about the page to the browser, such as the title of the page.
- The body: <body> element will contain the elements defining the content of the page intended for the user,
 such as the various texts present in the page, images, etc.
- The title element: <title> will allow us to indicate the title of the page visible on the top of your browser tabs.
 For example here we would have <title> DataScienTest - Train </title>
- The meta element: This tag will communicate to browsers the metadata of the page. For example <meta charset="utf-8"> 
defines the character encoding that will be used for this page."""
# ------------------------------------------------------------------------------------------------
# css
"""
- CSS is no more complicated than HTML: it complements it to help the developer format his web page.
- CSS code can be inserted directly into an HTML document with the <style>...</style> tags or into a dedicated .css file.

Schematically, a CSS style sheet is presented as follows:"""

# tag # Tag whose style we want to define
# {
#     # Properties of the tag to style
#     property 1: value 1;
#     property 2: value 2;
#     property 3: value 3;
# }

"""
In a CSS style sheet, there are three different elements:

- Tag names: We write the names of the tags whose style we want to modify. For example, 
if I want to change the appearance of all <p> paragraphs, the CSS block defining their style must be preceded by p.
- CSS properties: The "style effects" of the page are stored in properties.

 In the example below, we modify the following properties:
- color, which sets the text color.
- font-size, which sets the font size.
- text-align, which sets the text alignment.
- Values: For each CSS property, you must specify a value. For example, for the color property, 
you must indicate the name of the color. For font-size, you have to indicate what size you want, etc.

Example :"""
# p # We modify the style of the paragraphs (tag <p>)
# {
#     color: red; # Text color will be red
#     text-align: center; # Text will be centered
#     font-size: 20px; # Font size will be 20 pixels
# }
# If both tags need to have the same style, just combine the declaration.

# Example :

# h1, h2 # We modify the style of titles and subtitles (tag <h1> and <h2>)
# {
#     color: blue; # Title text will be blue
# }

"""
# Apply styling with class and id attributes #
We will now see how to target a particular element rather than an element type.
You can use these special attributes that work on all tags:

- the class attribute
- the id attribute


The class attribute
In the class attribute of a tag, you must enter a name that will create a subclass of this tag.

For example, we are going to create the "introduction" class which will be a subclass of paragraphs:
"""
# !DOCTYPE html>
# <html>
#     <head>
#         <meta charset="utf-8" />
#         <link rel="stylesheet" href="style.css" />
#         <title>Intro to CSS</title>
#     </head>

#     <body>
#         <h1>My first website</h1>

#         <p class="introduction">Welcome to my first site!</p>
#         <p>Thanks to <em>DataScientest</em> for making me understand how websites work!</p>
#     </body>
# </html>

"""
The "introduction" class will make it possible to define a particular style for the paragraphs of this class. 
To define the style of this class in the CSS file, you will need **to indicate** the name of your class starting with a (dot)."""

# Example :

# .introduction
# {
#     color: blue; # Only paragraphs of the "introduction" class will be blue
# }

"""The id attribute"""
# The id attribute is used to give a unique identifier to an element on the page: it can only be used once in the code.

# <img src="images/logo.png" id="logo" />
# To define the style of this particular element in the CSS code, you must refer to it by preceding the identifier with the # character:

# logo
# {
#      text-align: center; # The logo will be in the center of the page
# }
# We must retain the id and class attributes because they will allow us to identify the elements that will interest us
#  for Web Scraping."""
# # ------------------------------------------------------------------------------------------------
"""Web Scraping (meaning "scraping" or "scraping", and containing only a single "p") is a technology that allows 
the automated recovery of data from various web pages.
It is currently enjoying increasing popularity and is widely used in industry, 
especially for business intelligence purposes."""

"""
- Web Scraping refers to a technology.
-The Web Scraper, on the other hand, is the computer program or script that scrapes HTML code 
from web pages and analyzes it.
- The Web Scraper makes it possible to extract data and information that are presented on these websites 
in a systematized way, and to transform them into other more usable formats (Excel, csv, etc.).
- It is therefore a kind of large-scale "copy-paste" much more efficient than when done by hand."""


"""the pages and/or directories of the site that you are prohibited from scraping."""
# robots.txt for https://www.imdb.com properties
# User-agent: *
# Disallow: /OnThisDay
# Disallow: /ads/
# Disallow: /ap/
# Disallow: /mymovies/
# Disallow: /r/
# Disallow: /register
# Disallow: /registration/
# Disallow: /search/name-text
# Disallow: /search/title-text
# Disallow: /find
# Disallow: /find$
# Disallow: /find/
# Disallow: /tvschedule
# Disallow: /updates
# Disallow: /watch/_ajax/option
# Disallow: /_json/video/mon
# Disallow: /_json/getAdsForMediaViewer/
# Disallow: /list/ls*/_ajax
# Disallow: /*/*/rg*/mediaviewer/rm*/tr
# Disallow: /*/rg*/mediaviewer/rm*/tr
# Disallow: /*/mediaviewer/*/tr
# Disallow: /title/tt*/mediaviewer/rm*/tr
# Disallow: /name/nm*/mediaviewer/rm*/tr
# Disallow: /gallery/rg*/mediaviewer/rm*/tr
# Disallow: /tr/
# Disallow: /title/tt*/watchoptions
# Disallow: /search/title/?title_type=feature,tv_movie,tv_miniseries,documentary,short,video,tv_short&release_date=,2020-12-31&lists=%21ls538187658,%21ls539867036,%21ls538186228&view=simple&sort=num_votes,asc&aft

# User-agent: Baiduspider
# Disallow: /list/*
# Disallow: /user/*
