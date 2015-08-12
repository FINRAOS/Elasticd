from test import *
import elasticd.resource

class TestAWSResourceLocator(unittest.TestCase):
    def test_init(self):
        _plugin_manager = get_test_plugin_manager('settings.arl.cfg')
        self.assertIsNotNone(_plugin_manager)

        _resource_locator = _plugin_manager.get_resource_locator()

        self._test_obj(_resource_locator, ResourceLocator)
        resources = _resource_locator.get_resources()
        # Check if list
        self.assertNotIsInstance(resources, basestring)

    def _test_obj(self, obj, cls):
        self.assertIsNotNone(obj)
        self.assertTrue(isinstance(obj, BasePlugin), '%s does not extend base plugin' % obj)
        self.assertTrue(isinstance(obj, cls), '%s does not extend %s' % (obj, cls))


if __name__ == '__main__':
    unittest.main()
