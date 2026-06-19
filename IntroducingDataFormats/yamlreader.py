import yaml

with open(r'IntroducingDataFormats/r1.yml') as file:
    data = yaml.safe_load(file)

print(data)