import requests
import json
import pandas
import numpy
from flatten_json import flatten


a = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=JILL&use_first_name_alias=&last_name=WENGER&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
arez = a.text
b = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=CHRISTOPHER&use_first_name_alias=&last_name= KLOTZ&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1 = requests.get')
c = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=JACOB&use_first_name_alias=&last_name=CALLISON&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
d = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=BRIAN&use_first_name_alias=&last_name=CROTTY&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
e = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=LISA&use_first_name_alias=&last_name=DAUTENHAHN&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
f = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=CARE&use_first_name_alias=&last_name=ATC&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
g = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=KEVIN&use_first_name_alias=&last_name=STEICHEN&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')


print(arez)
print('-----------------')
print(b.text)
print('-----------------')
print(c.text)
print('-----------------')
print(d.text)
print('-----------------')
print(e.text)
print('-----------------')
print(f.text)
print('-----------------')
print(g.text)
print('-----------------')
