# -*- coding: utf-8 -*-
import os
from os.path import join, dirname
from dotenv import load_dotenv
from enum import Enum

class ImportEnvKeyEnum(Enum):
  IP_ADDRESS = 'ip_address'
  SERVER_PORT = 'server_port'
  PASSWORD = 'password'

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ENV_DIC = {}
ENV_KEYS = [ \
  ImportEnvKeyEnum.IP_ADDRESS.value, \
  ImportEnvKeyEnum.SERVER_PORT.value, \
  ImportEnvKeyEnum.PASSWORD.value ]

for key in ENV_KEYS:
  ENV_DIC[key] = os.environ.get(key)

