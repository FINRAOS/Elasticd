
__app_name__ = "elasticd"
__version__ = "0.1.0"
__author__ = "FINRA opensource"
__email__ = "finra.org"


import ConfigParser
import logging
import server
import daemon
from threading import Thread
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
    plugin_manager = PluginManager(config)
    _locator = plugin_manager.get_resource_locator()
    _datastore = plugin_manager.get_datastore()
    _driver = plugin_manager.get_driver()

    _registrar = Registrar(_datastore, _driver)

    #should the listener be started?
    start_server = config.getboolean('DEFAULT', 'start_server')
    if start_server:
        server.set_registrar(registrar)
        Thread.start(server.start())

    #start looking for backends and updating the driver
    #THIS CALL WILL NOT RETURN
    daemon.start(_registrar, _locator, config)




