from test import *
import tempfile
import shutil


string_to_compare = """    backend web0 {
            .host = "10.0.0.1";
            .port = "80";
    }

    backend web1 {
            .host = "10.0.0.2";
            .port = "80";
    }

    backend web2 {
            .host = "10.0.0.3";
            .port = "80";
    }"""


class TestDriver(unittest.TestCase):

    def test_driver(self):
        _plugin_manager = get_test_plugin_manager()
        _driver = _plugin_manager.get_driver()
        resources = _plugin_manager.get_resource_locator()
        backends = resources.get_resources()
        print backends

        temp_dir = '%s/elasticd' % tempfile.gettempdir()

        if os.path.isdir(temp_dir):
            shutil.rmtree(temp_dir)
        temp_dir = os.path.realpath(temp_dir)
        os.makedirs(temp_dir)
        print temp_dir
        _driver._config.set('driver', 'vcl_output_path', temp_dir)

        _driver.update(backends)

        vcl_output_path = '%s/%s' % (_driver._get_config_value('vcl_output_path'),
                                     _driver._get_config_value('vcl_output_name'))
        f = open(vcl_output_path, 'r')
        content = f.read()
        f.close()
        print content

        self.assertEquals(content.strip(), string_to_compare.strip())
        shutil.rmtree(temp_dir)



if __name__ == '__main__':
    unittest.main()