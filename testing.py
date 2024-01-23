import requests
import json
import pandas as pd
import numpy as np
from flatten_json import flatten

r = requests.get('https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&first_name=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=90201&country_code=&limit=10&skip=&version=2.0')
results_text = r.text
print(results_text)
