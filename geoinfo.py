#!/usr/bin/env python3

"""
This one still is a bit of a work in progress
Takes a list of newline seperated ip's from stdin,
returns geoip distribution.
"""

import sys
import geoip2.database

georeader = geoip2.database.Reader('data/GeoLite2-Country.mmdb')

target_count = dict()
country_count = dict()
failed_lookups = 0

def default_increment(dictionary, key):
    try:
        dictionary[key] = dictionary[key] + 1
    except KeyError:
        dictionary[key] = 1

total_country_count = dict()
total_country_file = open('data/absolute_ip_frequencies')
for line in total_country_file:
    country, count = line.strip().split(',')
    total_country_count[country] = int(count)

counter = 0
for line in sys.stdin:
    if line.strip() == '':
        break
    counter += 1
    if counter % 1000 == 0:
        sys.stderr.write(str(counter) + '\n')
    ip = line.strip().split(',')[0]
    try:
        geodata = georeader.country(ip)
    except geoip2.errors.AddressNotFoundError:
        failed_lookups += 1
    else:
        country = geodata.country.iso_code
        default_increment(country_count, country)


count_list = list(country_count.items())
count_list.sort(key = lambda x: x[1], reverse=True)

for entry in count_list:
    country = entry[0]
    abs_freq = entry[1]
    try:
        total_count = total_country_count[country]
    except IndexError:
        print("{}, {}".format(country, abs_freq))
    else:
        rel_freq = abs_freq / total_count
        print("{}, {:5}, {:.3e}".format(country, abs_freq, rel_freq))

sys.stderr.write("Failed lookups: {}\n".format(failed_lookups))
