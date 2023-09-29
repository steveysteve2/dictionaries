"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"

"""

import json
infile = open("school_data.json", 'r')

schools = json.load(infile)     #loads a list of the json file

conference_schools = [372,108,107,130]

#Display schools in ACC, Big 12, Big Ten, and SEC
for school in schools:
    if school['NCAA']["NAIA conference number football (IC2020)"] in conference_schools:
        print(school["instnm"])

# Display report for all universities that have a graduation rate for Women over 75%

st1 = "Graduation rate  women (DRVGR2020)"

for school in schools:
    if (school[st1]) != None and (school[st1]) > 75:
        print(f"School: {school['instnm']}")
        print(f'Women Grad Rate: {school[st1]}')

# Display report for all universities that have a total price for 
# in-state students living off campus over $50,000

st = "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"

for school in schools:
    if (school[st]) != None and (school[st]) > 50000:
        print(f"School: {school['instnm']}")
        print(f'Price for students in-state living off-campus: {school[st]}')

infile.close()