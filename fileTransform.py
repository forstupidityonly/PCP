#!/usr/bin/python3
"""fix 834's with PCP names to be NPI numbers"""
NameToNPI = __import__('NameToNPI').NameToNPI


def fileTransform(fileName=""):
    """accepts file name, searches for PCP names passing to NameToNPI, with valid return NPI is substituted in file"""
    import re

    with open(fileName, "r") as file:
        content = file.read()
    pattern = r"NM1\*P3\*2\*+SV\*.+\*72~"
    matches = re.findall(pattern, content)
    
    modMatches = matches
    for i in modMatches:
        Name = i[17:-4]
        Name = Name.split('*')
        NPI = NameToNPI(Name[1],Name[0])
        print (NPI)
        print (i)
        print ('---------------')
        
