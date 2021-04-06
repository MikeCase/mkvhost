import os
import json
import sys

server_paths = {
    'apache': '/etc/apache2',
    'nginx': '/etc/nginx',

    'apache-conf-av': '/conf-available',
    'apache-conf-en': '/conf-enabled',
    'nginx-site-av': '/sites-available',
    'nginx-site-en': '/sites-enabled',
}

class SysConfig:

    def __init__(self):
        self.server_paths = server_paths
        self.path_avail = []
        filepath = ''
        if os.path.exists(filepath.join([self.server_paths['nginx'],self.server_paths['nginx-site-av']])):
            # print('It exists')
            self.path_avail.append(filepath.join([self.server_paths['nginx'],self.server_paths['nginx-site-av']]))