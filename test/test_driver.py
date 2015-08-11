from test import *


class TestDriver(unittest.TestCase):

    def test_driver(self):
        _plugin_manager = get_test_plugin_manager()
        _driver = _plugin_manager.get_driver()
        resources = _plugin_manager.get_resource_locator()
        backends = resources.get_resources()
        self.assertTrue(_driver.update(_driver), "Hello Jasdasdasdohn Doe2")

if __name__ == '__main__':
    unittest.main()