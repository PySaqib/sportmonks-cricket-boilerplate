#!/bin/python3

# SportMonks Cricket API Boilerplate. Helps you get up and running quickly with your sportmonks cricket application.

import requests     # Creates a request
import json         # Parses JSON data
import pprint       # Prints out stuff in a well-organized format

# API Token to access the API
API_token = "insert_your_API_token_here"

'''
Set the retrieve variable to these various options depending on your requirements.

livescores => For getting livescore data.
countries => For getting countries data. Use countries/{country_id}/ to get a specific country. For example, Pakistan is 52126.
continents => For getting continents data.
leagues => For getting leagues data.

More details can be found on sportmonks.com

'''

retrieve_option = 'insert_retrieve_option_from_above'

# Generates a request to the sportmonks API
API_request = requests.get("https://cricket.sportmonks.com/api/v1/" + retrieve_option + "?api_token=" + API_token)

content = API_request.content   # Stores the content retrieved from API_request

json_content = json.loads(content) 
pprint.pprint(json_content)