
__app_name__ = "elasticd"
__version__ = "0.1.0"
__author__ = "FINRA opensource"
__email__ = "finra.org"


import ConfigParser
import logging
import server
import daemon
from registrar import Registrar
from elasticd import registrar
from plugin_manager import PluginManager

#todo set logging path in /var/log/elasticd/  read from config?
FORMAT = '%(asctime)-15s %(module)s %(funcName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, filename='elasticd.log', level=logging.DEBUG)

DEFAULT_SETTINGS_FILE = '/etc/elasticd/settings.cfg'


def startup(config_path=DEFAULT_SETTINGS_FILE):
    #load the config file and start the listener, daemon
    logging.debug("init starting up")
    config = ConfigParser.ConfigParser()
    logging.debug('reading setting from: %s' % config_path)
    config.read(config_path)

    #Load the plugin manager to get a handle to the plugins.
    p_manager = PluginManager(config)
    _locator = p_manager.get_resource_locator()
    _datastore = p_manager.get_datastore()
    _driver = p_manager.get_driver()

    _registrar = Registrar(_datastore, _driver)

    #start looking for backends
    daemon.start(_registrar, _locator, config)

    start_server = config.getboolean('DEFAULT', 'start_server')

    if start_server:
        server.set_registrar(registrar)
        server.start()




