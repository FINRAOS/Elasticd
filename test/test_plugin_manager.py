from test import *


class TestPluginManager(unittest.TestCase):
    def test_init(self):
        _plugin_manager = get_test_plugin_manager()
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
