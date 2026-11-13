import csv
import json
import requests

# COLLECTION --> https://www.loc.gov/free-to-use/colors-tell-the-story/

"""
GET COLLECTION LIST
"""

baseURL = 'https://www.loc.gov'
endpoint = '/free-to-use'
collection = '/colors-tell-the-story'
parameters = {
    'fo' : 'json'
}

collection_list_response = requests.get(baseURL + endpoint + collection, params=parameters)
# print(collection_list_response.url)
# print(collection_list_response.status_code)

collection_json = collection_list_response.json()
# print(json.dumps(collection_json, indent=4))

# print(collection_json.keys())

collection_items = collection_json['content']['components'][0]['masonry_gallery'][0]['items']

# print(collection_items)
# print(type(collection_items))
# print(len(collection_items))
