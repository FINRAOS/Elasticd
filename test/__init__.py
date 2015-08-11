import unittest
from elasticd.plugins import BasePlugin
from elasticd.plugins import ResourceLocator
from elasticd.plugins import Driver
from elasticd.plugins import Datastore
from elasticd.plugin_manager import PluginManager
import os
import ConfigParser

def get_test_plugin_manager():
    config_file = os.path.dirname(os.path.realpath(__file__)) + '/../test-conf/settings.cfg'
    config_file = os.path.realpath(config_file)

    config = ConfigParser.ConfigParser()
    config.read(config_file)

    _plugin_manager = PluginManager(config)
    return _plugin_manager