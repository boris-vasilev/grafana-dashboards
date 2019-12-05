#!/usr/bin/env python3

import sys
import json
from urllib.request import urlopen
import subprocess

def apply_wlcg_mapping(grafana_dashboard_definition_filename):
    with open('grafana_color_scheme.ini', 'r') as f:
        color_scheme = f.read().split(',')
    
    urls = ["http://wlcg-cric.cern.ch/api/core/rcsite/query/?json&state=ANY",
                "http://wlcg-cric.cern.ch/api/core/federation/query/?json"]
    
    wlcg_mappings = set()
    
    for url in urls:
        response = urlopen(url)
        wlcg_data = response.read().decode("utf-8")
        wlcg_data = json.loads(wlcg_data)
        
        wlcg_mappings.update(wlcg_data.keys())
        
    with open('colourmapper.ini', 'w') as f:
        f.write('[Colours]\n')

        for index, obj in enumerate(wlcg_mappings):
            f.write(f'{obj} = {color_scheme[index % len(color_scheme)]}\n')
    
    subprocess.call(['python3', 'colourmapper.py', grafana_dashboard_definition_filename])

if __name__ == '__main__':
    apply_wlcg_mapping(sys.argv[1])
