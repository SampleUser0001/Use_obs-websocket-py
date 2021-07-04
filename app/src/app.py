# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os
import importenv as setting
from importenv import ImportEnvKeyEnum

from obswebsocket import obsws, requests

import sys
sys.path.append('./')
from logutil import LogUtil

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':

  host = setting.ENV_DIC[ImportEnvKeyEnum.IP_ADDRESS.value]
  port = int(setting.ENV_DIC[ImportEnvKeyEnum.SERVER_PORT.value])
  password = setting.ENV_DIC[ImportEnvKeyEnum.PASSWORD.value]

  ws = obsws(host, port, password)
  ws.connect()

  scenes = ws.call(requests.GetSceneList())

  if scenes.status:
      for s in scenes.getScenes():
          print(s["name"])

  ws.disconnect()