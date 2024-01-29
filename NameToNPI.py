#!/usr/bin/python3
"""fix 834's with PCP names to be NPI numbers"""


def NameToNPI(firstName="", lastName=""):
    """accepts fist and last name and returns NPI"""
    import requests
    import json

    q1 = 'https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=' 
    q2 = '&use_first_name_alias=&last_name='
    q3 = '&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1'
    query = q1 + firstName + q2 + lastName + q3
    res = requests.get(query)
    res_json = res.json()
    return(res_json['results'][0]['number'])

