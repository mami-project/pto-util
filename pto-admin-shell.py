#!/usr/bin/env python3

################################################################################
# Simple shell to interact with pto-admin
#
# type `help` for a list of commands 
# One command / argument per line
#
# Author: Piet De Vaere --- piet@devae.re
################################################################################


import sys
import json
import requests

base_url = 'http://localhost:33525'

def json_pretty_print(data):
    print(json.dumps(data, sort_keys=True, indent=4))

def print_response(response):
    try:
        json_data = response.json()
    except json.decoder.JSONDecodeError:
        json_data = None 
    print(response)
    if json_data:
        json_pretty_print(json_data)
    else:
        print(response.text)

def get_analyzer_data():
    return requests.get(base_url + '/analyzer').json()

def clean_input(prompt):
    return input(prompt).strip()


################################################################################
# User commands
################################################################################

def analyzers_print_names():
    analyzers = get_analyzer_data()
    for analyzer in analyzers:
        print(analyzer['_id'])

def analyzers_print_all():
    json_pretty_print(get_analyzer_data())

def analyzer_print_detail():
    print('Print detail of analyzer')
    analyzers = get_analyzer_data()
    selected_id = clean_input('analyzer id >> ')
    for analyzer in analyzers:
        if selected_id == analyzer['_id']:
            json_pretty_print(analyzer)

def create_analyzer():
    print('Create a new analyzer')
    analyzer_id = clean_input("id >> ")
    repo_url = clean_input("repo_url >> ")
    repo_commit = clean_input("repo_commit >> ")
    conf = {'repo_url' : repo_url, 'repo_commit': repo_commit}
    url = base_url + '/analyzer/' + analyzer_id + '/create'
    
    response = requests.post(url, json = conf)
    print_response(response)

def update_analyzer():
    print('Update an analyzer')
    analyzer_id = clean_input("id >> ")
    repo_url = clean_input("repo_url >> ")
    repo_commit = clean_input("repo_commit >> ")
    conf = {'repo_url' : repo_url, 'repo_commit': repo_commit}
    url = base_url + '/analyzer/' + analyzer_id + '/setrepo'
    
    response = requests.post(url, json = conf)
    print_response(response)

def cancel_analyzer():
    print('Cancel an analyzer')
    analyzer_id = clean_input("id >> ")
    url = base_url + '/analyzer/' + analyzer_id + '/cancel'
    
    response = requests.put(url)
    print_response(response)

def enable_analyzer():
    print('Enable an analyzer')
    analyzer_id = clean_input("id >> ")
    url = base_url + '/analyzer/' + analyzer_id + '/enable'
    
    response = requests.put(url)
    print_response(response)

def disable_analyzer():
    print('Disable an analyzer')
    analyzer_id = clean_input("id >> ")
    url = base_url + '/analyzer/' + analyzer_id + '/disable'
    
    response = requests.put(url)
    print_response(response)

def validate_upload():
    print('Validate an upload')
    upload_id = clean_input("id >> ")
    url = base_url + '/upload/' + upload_id + '/valid'
    
    response = requests.put(url)
    print_response(response)

def invalidate_upload():
    print('Invalidate an upload')
    upload_id = clean_input("id >> ")
    url = base_url + '/upload/' + upload_id + '/invalid'
    
    response = requests.putt(url)
    print_response(response)

commands = dict()
commands['list'] = analyzers_print_names
commands['list_detail'] = analyzers_print_all
commands['detail'] = analyzer_print_detail
commands['exit'] = sys.exit
commands['create'] = create_analyzer
commands['update'] = update_analyzer
commands['cancel'] = cancel_analyzer
commands['enable'] = enable_analyzer
commands['disable'] = disable_analyzer
commands['valid'] =  validate_upload
commands['invalid'] = invalidate_upload

while 1:
    user_input = clean_input('>> ')
    if user_input in ('?', 'h','help'):
        command_list = list(commands.keys())
        command_list.sort()
        print(', '.join(command_list))
        continue
    try:
        command = commands[user_input]
    except KeyError:
        print('Not a valid command, try again')
    else:
        command()

