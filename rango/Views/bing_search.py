# import json
# import urllib
#
#
# def read_bing_key():
#     bing_api_key = None
#     try:
#         with open('bing.key','r') as f:
#             bing_api_key = f.readline()
#     except :
#         raise IOError('bing.key file not found')
#     return bing_api_key
#
# def run_query(search_terms):
#     bing_api_key = read_bing_key()
#
#     if not bing_api_key :
#         raise KeyError('Bing key not found')
#     root_url = 'https://api.co'
#     service = 'Web'
#     results_per_page = 10
#     offset = 0
#     query = "'{0}'".format(search_terms)
#     try:
#         from urllib import parse
#         query = urllib.parse.quote(query)
#     except ImportError:
#         from urllib import quote
#         query = quote(query)
#     search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
#         root_url,
#         service,
#         results_per_page,
#         offset,
#         query)
#     username =''
#     try:
#         from urllib import request
#         password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
#     except ImportError:
#         import urllib2
#         password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
#         password_mgr.add_password(None, search_url, username, bing_api_key)
#     results = []
#     try:
#         import ipdb
#         ipdb.set_trace()
#         handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
#         opener = urllib.request.build_opener(handler)
#         request.install_opener(opener)
#
#         try:
#             response = request.urlopen(search_url).read()
#             response = response.decode('utf-8')
#         except UnboundLocalError:
#             response = urllib2.urlopen(search_url).read()
#         json_response = json.loads(response)
#
#         for result in json_response['d']['results']:
#             results.append({'title':result['Title'],
#                             'link':result['Url'],
#                             'summary':result['Description']})
#     except:
#         print("Error when Querying the Bing api")
#     return results
#

import json
import urllib
import requests


def read_bing_key():
    bing_api_key = None
    try:
        # import ipdb
        # ipdb.set_trace()
        with open('rango/bing.key', 'r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found')
    return bing_api_key


def run_query(search_items):
    bing_api_key = read_bing_key()
    root_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    headers = {"Ocp-Apim-Subscription-Key": bing_api_key}
    params = {"q": search_items, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(root_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    return search_results

def main():
    result_list = run_query(input())
    print(result_list)
if __name__ == "__main__":
    main()



# def main():
#     print("Enter a query ")
#     query = input()
#     results = run_query(query)
#     for result in results:
#         print(result['title'])
#         print('-' * len(result['title']))
#         print(result['summary'])
#         print(result['link'])
#         print()
