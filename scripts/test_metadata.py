import GEOparse

gse = GEOparse.get_GEO("GSE280902")

mapping = {}
for gsm_name, gsm in gse.gsms.items():
    title = gsm.metadata['title'][0]
    response = 1 if 'Complete' in gsm.metadata['characteristics_ch1'][3] else 0
    mapping[gsm_name] = {'title': title, 'response': response}

print(mapping)