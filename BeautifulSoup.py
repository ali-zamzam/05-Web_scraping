"""BeautifulSoup"""

"""
- Beautiful Soup est une bibliothèque Python permettant d'extraire des données de fichiers HTML et XML.
- we will use it to build a database containing the title, the year of release as well as the average ratings given
by each user for each film present in the list of the 111 best films on the Sens Critique site.
"""
# https://web.archive.org/web/20210422083605/https://www.senscritique.com/films/tops/top111


"""
- The Web Scraping method with the BeautifulSoup package is a so-called **static method** because it **ignores** 
the JavaScript and only uses the **source code** of the web page considered.
- It is opposed to **dynamic methods** which allow scraping sites whose content is generated by JavaScript script.
- It is possible to do **dynamic scraping** with Python's **Selenium package**
"""


"""
-The very first step in writing a web-scraper is to load the BeautifulSoup package. 
- the **urlopen** function from the request module.
- the pandas package (which we'll use at the end to build the database)
"""


from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

# request allows to retrieve a website
# bs4 convert website to BeautifulSoup object


# We use the urlopen function to retrieve the HTML code of the web page that interests us
# (here the top 111 of SensCritique), we store everything in a variable named page:
page_SC = urlopen(
    "https://web.archive.org/web/20210422083605/https://www.senscritique.com/films/tops/top111"
)

# We create a soup instance of the BeautifulSoup class to decrypt this HTML code:
soup = BeautifulSoup(page_SC, "html.parser")
"""
- Then we will be able to search and retrieve what interests us, starting with the title of all the films in the list 
using the ***findAll function***.
"""
# To do this, we must look in the source code of the page, in which tag is included the title of each film.
# In Google Chrome, all you have to do is right-click then select **"Inspect"** to access the HTML code of the page:

"""
- The title of each film is included in an "a" tag (hyperlink)."""

# <a href="/web/20210422083605/https://www.senscritique.com/film/12_hommes_en_colere/370894" class="elco-anchor" id="product-title-370894">12 hommes en colère</a>
"""
- To select only the links that correspond to the titles of the films in the list, simply retrieve the class 
of this tag:
- We then use it in the **findAll** method, the name argument contains the tag and we fill in the attrs argument 
with the class that identifies the elements we are trying to retrieve:
"""
noms_SC = soup.findAll(name="a", attrs={"class": "elco-anchor"})

"""
**nom_SC** is a list containing all the movie titles but also the HTML code (the "a" tags surrounding the titles),
to extract only the text, we use the text attribute. The attribute can only be used for one element at a time,
so we make a loop:
"""
titre_SC = []

for element in noms_SC:
    titre_SC.append(element.text)

print(titre_SC)

# ------------------------------------------------------------------------------------------------
annee_sortie_SC = []

# <span class="elco-date">(1957)</span>
"""# here we don't use name = a because we have span"""
for date_s in soup.findAll(name="span", attrs={"class": "elco-date"}):
    #  weuse strip to eleminate the ( ) becase on the site we have the date like that (1957)
    annee_sortie_SC.append(date_s.text.strip("()"))

print(annee_sortie_SC)

# ----------------------------------------------------------------------------
# <a href="/web/20210422083605/https://www.senscritique.com/film/12_hommes_en_colere/370894/critiques" class="erra-global" data-sc-tooltip="true" data-hasqtip="0" oldtitle="Note globale pondérée sur : 45520 avis" title="">
#                                 8.7                            </a>
note_SC = []

for note in soup.findAll(name="a", attrs={"class": "erra-global"}):
    # because we have space (      8.7      </a>) we use strip
    note_SC.append(note.text.strip())

print(note_SC)

# -------------------------------------------------------------------------------------------
"""create the data frame"""

critique = pd.DataFrame(
    list(zip(titre_SC, annee_sortie_SC, note_SC)), columns=["Title", "year", "note"]
)

critique.head()

# to save the dataframe
critique.to_csv("generated_data/critique.csv")

# ----------------------------------------------------------------------------------------------
"""We are going to try to build the same database as before, this time for the IMDB site, 
and thus be able to compare the users of the two sites according to the ratings they gave for the same films."""
# The top 250 movies from the IMDB site are available here.
# https://www.imdb.com/chart/top

"""
- On some sites, it will not be possible to isolate a specific element from its class 
(either because the **class is not assigned** to the only elements that interest us, 
or because **no class** is specified in the code).

- In this case, the **SelectorGadget extension** available in **Google Chrome** can be useful, 
the latter allows us to directly select the elements that interest us and to obtain the corresponding CSS path.

- For example on the IMDB classification, no class is entered in the a tag which contains the titles of 
the films in the list."""

# <td class="titleColumn">
#       5.
#       <a href="/title/tt0050083/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&amp;pf_rd_r=ZJAHCFM459XN1SJNR4CS&amp;pf_rd_s=center-1&amp;pf_rd_t=15506&amp;pf_rd_i=top&amp;ref_=chttp_tt_5" title="Sidney Lumet (dir.), Henry Fonda, Lee J. Cobb" class="selectorgadget_selected">12 Hommes en colère</a>
#         <span class="secondaryInfo">(1957)</span>
#     </td>

page_imdb = urlopen("https://www.imdb.com/chart/top")

soup = BeautifulSoup(page_imdb, "html.parser")

titre_imdb = []

"""we use **soup.select** """
#  .titleColumn from class and  a from < a href ...>
for element in soup.select(".titleColumn a"):
    titre_imdb.append(element.text)


annee_sortie_imdb = []
for element in soup.findAll(name="span", attrs={"class": "secondaryInfo"}):
    annee_sortie_imdb.append(element.text.strip("()"))


# <td class="ratingColumn imdbRating">
#             <strong title="8,9 based on 779&nbsp;745 user ratings">8,9</strong>
#     </td>
#  we don't put imdbRating ??
note_imdb = []
for element in soup.select(".ratingColumn strong"):
    note_imdb.append(element.text)


imdb = pd.DataFrame(
    list(zip(titre_imdb, annee_sortie_imdb, note_imdb)),
    columns=["Title", "year", "Note_imdb"],
)

imdb.head()

imdb.to_csv("generated_data/imdb.csv")
# ----------------------------------------------------------------------------
from scipy.stats import ttest_rel

# An advertiser wishing to advertise a certain film has every interest in publishing his campaign on a site
# whose users are closer to the audience he wishes to target.
# He may therefore be led to wonder whether the users of the Sens Critique and IMDB sites have the same profiles.

"""# To verify this, we will compare the rating on the two sites by creating a DataFrame containing only the films
# present in both the Sens Critique and the IMDB rating."""

"""# To do this, we perform a merge using the method with the same name in pandas"""


""" we will delete the accent from films titles"""
imdb["Title"] = (
    imdb["Title"]
    .str.normalize("NFKD")
    .str.encode("ascii", errors="ignore")
    .str.decode("utf-8")
)
critique["Title"] = (
    critique["Title"]
    .str.normalize("NFKD")
    .str.encode("ascii", errors="ignore")
    .str.decode("utf-8")
)

# Before performing the merge, we are going to "standardize" the titles of the films.
# Use the str.upper() method to uppercase the entire Title column.
imdb["Title"] = imdb["Title"].str.upper()
critique["Title"] = critique["Title"].str.upper()

# (g) Perform the merge of the two DataFrames on the Title column by selecting only the intersection of the two.
final_note = imdb.merge(critique, how="inner", on="Title")
print(final_note)


# (h) Change the type of the Note_IMDB and Note_SC columns to numeric format if not already done.
final_note["Note_imdb"] = pd.to_numeric(final_note["Note_imdb"])
final_note["note"] = pd.to_numeric(final_note["note"])

# # (i) Perform a paired Student test to compare the means given by Sens Critique and by IMDB using the ttest_rel()
# # function of the scipy.stats module. What do you notice?
ttest_rel(final_note["Note_imdb"], final_note["note"])
# ----------------------------------------------------------------------------
