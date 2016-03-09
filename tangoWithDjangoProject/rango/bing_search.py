import json
import urllib, urllib2

BING_API_KEY = 'XpYMFCZPS0JuM1eicl2UZSnYYWjPOrCdLfnAjRFlQAU'

def run_query(search_terms):
    root_url = 'https://api.datamarket.azure.com/Bing/Search/v1/'
    source = 'Web'

    results_per_page = 10
    offset = 0

    query = "'{0}".format(search_terms)
    query = urllib.quote(query)


