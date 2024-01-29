#!/usr/bin/python3
"""fix 834's with PCP names to be NPI numbers"""
NameToNPI = __import__('NameToNPI').NameToNPI

def fileTransform(fileName=""):
    """accepts file name, searches for PCP names passing to NameToNPI, with valid return NPI is substituted in file"""
    import re

    with open(fileName, "r") as file:
        content = file.read()
    pattern = r"NM1\*P3\*1\*.+~"
    matches = re.findall(pattern, content)
    
    modMatches = matches
    modStr = '****XX*'
    for i in modMatches:
        NameArr = i[9:-1].split('*')
        NPI = NameToNPI(NameArr[1],NameArr[0])
        i = i[:-1] + modStr + NPI  + '~'
        print (i)
    print (matches)
    print (modMatches)

"""
this for OSU
pattern = r"NM1\*P3\*2\*+SV\*.+\*72~"
Name = i[17:-4]
"""
