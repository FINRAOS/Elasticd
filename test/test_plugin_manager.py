import unittest
from elasticd.base_plugin import BasePlugin
from elasticd.locator import ResourceLocator
from elasticd.driver import Driver
from elasticd.datastore import Datastore
from elasticd.plugin_manager import PluginManager
import os
import ConfigParser


class TestPluginManager(unittest.TestCase):
    def test_init(self):
        config_file = os.path.dirname(os.path.realpath(__file__)) + '/../conf/settings.cfg'
        config_file = os.path.realpath(config_file)

        config = ConfigParser.ConfigParser()
        config.read(config_file)
        self.assertIsNotNone(config)

        _plugin_manager = PluginManager(config)
        self.assertIsNotNone(_plugin_manager)

        _resource_locator = _plugin_manager.get_resource_locator()
        _driver = _plugin_manager.get_driver()
        _datastore = _plugin_manager.get_datastore()

        self._test_obj(_resource_locator, ResourceLocator)
        self._test_obj(_driver, Driver)
        self._test_obj(_datastore, Datastore)

    def _test_obj(self, obj, cls):
        self.assertIsNotNone(obj)
        self.assertTrue(isinstance(obj, BasePlugin), '%s does not extend base plugin' % obj)
        self.assertTrue(isinstance(obj, cls), '%s does not extend %s' % (obj, cls))


if __name__ == '__main__':
    unittest.main()
