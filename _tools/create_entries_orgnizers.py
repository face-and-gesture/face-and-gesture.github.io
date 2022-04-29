# create_entries_organizers.py

import os
import yaml
import pandas as pd

def create_file(fname, content):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(content, f,
                encoding='utf-8', allow_unicode=True,
                default_flow_style=False)
        f.write('---\n')

filename = '../../_data/conference/organizers.csv'
mdpath = '../../my_collections/_organizers'
imgpath = '/assets/images/organizers/'
df = pd.read_csv(filename)
index = 0
for row in df.iterrows():
    firstname = row[1][0].strip()
    lastname = row[1][1].strip()
    position = row[1][2].strip() + ' Chair'
    web = row[1][3].strip()
    newfilename = firstname.lower() + '-' + lastname.lower()
    name = firstname + ' ' + lastname
    content = {}
    content['name'] = name
    content['first_name'] = firstname
    content['last_name'] = lastname
    content['position'] = position

    links = {}
    links['name'] = 'Profile'
    links['absolute_url'] = web
    content['links'] = links
    
    content['image'] = os.path.join(imgpath, 'cropped-' + newfilename) + '.jpeg'
    content['affiliation'] = row[1][4]
    content['country'] = row[1][5]
    mdfilename = os.path.join(mdpath, str(index).zfill(2) + "-" + newfilename) + '.md'
    create_file(mdfilename, content)
    index += 1