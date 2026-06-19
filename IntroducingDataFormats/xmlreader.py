import xmltodict

# with open(r'IntroducingDataFormats/r1.xml') as file:
#     xml_data = file.read()

with open('r1.xml') as file:
    xml_data = file.read()

data=xmltodict.parse(xml_data)

print(data)
print()
print(data['router']['interfaces'])
print()
print(data['router']['interfaces']['interface'][0]['ip'])
print()
print(data['router']['routing']['routes'])

# import os

# print("Python is currently looking here:", os.getcwd())
# print("Files visible in this folder:", os.listdir())