"""Web Scraping on Google"""

"""This method requires the use of the googlesearch package."""

# In this particular case, the goal is to find all articles related to this topic.
# **la parité en intelligence artificielle**

"""We start by installing the google library using pip or conda on the terminal command line:"""
# with pip
# pip install googlesearch

# with conda
# conda install -c conda-forge googlesearch

"""We can then import the library into our Jupyter Notebook via:"""
# from googlesearch import search

# The next step is to create an empty list, and use a for loop to iterate through the code:

# for url in search(query, # the query you want to run
#                   tld='com', # the domain
#                   lang='en', # the language
#                   num=10, # number of results per page
#                   start=0, # first result to retrieve
#                   stop=None, # last result to retrieve
#                   pause=2.0, # delay between HTTP requests
#                ):
#     print(url)


from googlesearch import search

for url in search(
    "parité en intelligence artificielle",
    tld="com",
    lang="fr",
    start=0,
    stop=10,
    pause=2.0,
):
    print(url)
# ------------------------------------------------------------------------------
"""We can now use these urls to scrape the websites that are returned."""

# pip install newspaper3k

# You can now use the following command to scrape the urls returned by Google search:

# from newspaper import Article
# article = article(url)
# article.download()
# article.parse()

from newspaper import Article

url = "https://datascientest.com/parite-en-intelligence-artificielle-un-enjeu-cle"
article = Article(url)
article.download()
article.parse()
print(article.text)

# -------------------------------------------------------------------------------------------
"""
- One of the coolest features of the newspaper library is that it incorporates NLP (natural language processing) algorithms
and can return keywords, summaries, and other interesting information.

- For this to work, you must have the Natural Language Toolkit **(NLTK) installed** with
 pip install nltk and the punkt package of nlt installed with nltk.download('punkt')."""

# pip install nltk
# nltk.download('punkt')

# Retrieve the authors, publication date, abstract and keywords of our blog post on parity in artificial intelligence.

article.nlp()  # we use nlp on the article
article.authors
article.publish_date
article.summary
article.keywords
