import requests
import json
import pandas
import numpy
from flatten_json import flatten


a = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=JILL&use_first_name_alias=&last_name=WENGER&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
a_json = a.json()
print(a_json['results'][0]['number'])
print('------------------------------------------------------------------------------------------')
b = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=CHRISTOPHER&use_first_name_alias=&last_name= KLOTZ&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
b_json = b.json()
print(b_json['results'][0]['number'])
print('------------------------------------------------------------------------------------------')
c = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=JACOB&use_first_name_alias=&last_name=CALLISON&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
c_json = c.json()
print(c_json['results'][0]['number'])
print('------------------------------------------------------------------------------------------')
d = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=BRIAN&use_first_name_alias=&last_name=CROTTY&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
d_json = d.json()
print(b_json['results'][0]['number'])
print('------------------------------------------------------------------------------------------')
e = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=LISA&use_first_name_alias=&last_name=DAUTENHAHN&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
e_json = e.json()
print(e_json['results'][0]['number'])
print('------------------------------------------------------------------------------------------')

"""

f = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=CARE&use_first_name_alias=&last_name=ATC&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
f_json = f.json()
print(f_json['results'][0]['number'])
print('------------------------------------------------------------------------------------------')

"""

g = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=KEVIN&use_first_name_alias=&last_name=STEICHEN&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1')
g_json = g.json()
print(g_json['results'][0]['number'])
print('------------------------------------------------------------------------------------------')
