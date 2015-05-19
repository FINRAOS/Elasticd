#/bin/python/env

import elasticd
import os

#elasticd.startup()
elasticd.startup(os.path.dirname(os.path.realpath(__file__)) + '/../conf/settings.cfg')
