# -*- coding: UTF-8 -*-
import os
import yaml

CONFIG_FILE_NAME = 'config.yaml'
PTOOLKIT_HOME = os.environ.get('PTOOLKIT_HOME', os.path.join(os.path.expanduser("~"), '.ptoolkit'))
CODES_HOME = os.path.split(os.path.realpath(__file__))[0]


def get_config():
    options = [
        CONFIG_FILE_NAME,
        os.path.join(PTOOLKIT_HOME, CONFIG_FILE_NAME),
        os.path.join(CODES_HOME, CONFIG_FILE_NAME)
    ]
    for path in options:
        if os.path.isfile(path):
            with open(os.path.join(path), 'rb') as f:
                token_dict = yaml.safe_load(f)
                if token_dict:
                    return token_dict
    raise Exception("can't found ptoolkit config from anywhere!")
