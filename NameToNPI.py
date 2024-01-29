import requests
import json

firstName = 'JESSICA'
lastName = ' KELLER'

q1 = 'https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=' 
q2 = '&use_first_name_alias=&last_name='
q3 = '&organization_name=&address_purpose=&city=&state=OK&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1'
query = q1 + firstName + q2 + lastName + q3
res = requests.get(query)
res_json = res.json()
print(res_json['results'][0]['number'])
