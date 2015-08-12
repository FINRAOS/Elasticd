__app_name__ = "elasticd"
__version__ = "0.1.0"
__author__ = "FINRA opensource"
__email__ = "finra.org"

import ConfigParser
import logging
import logging.handlers
import server
import daemon
from threading import Thread
from registrar import Registrar
from elasticd import registrar
from plugin_manager import PluginManager


DEFAULT_SETTINGS_FILE = '/etc/elasticd/settings.cfg'
LOG_FORMAT = '%(asctime)-15s %(module)s %(funcName)s %(thread)d %(message)s'

def startup(config_path=DEFAULT_SETTINGS_FILE):
    #init logging
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    setup_logging(config)

    #load the config file and start the listener, daemon
    logging.debug('reading setting from: %s' % config_path)

    #Load the plugin manager to get a handle to the plugins.
    _plugin_manager = PluginManager(config)
    locator = _plugin_manager.get_resource_locator()
    datastore = _plugin_manager.get_datastore()
    driver = _plugin_manager.get_driver()

    _registrar = Registrar(datastore, driver)

    #should the listener be started?
    start_server = config.getboolean('DEFAULT', 'start_server')
    if start_server:
        server.set_registrar(registrar)
        Thread.start(server.start())

    #start looking for backends and updating the driver
    #THIS CALL WILL NOT RETURN
    daemon.start(_registrar, locator, config)


def setup_logging(config):
    handler = logging.handlers.TimedRotatingFileHandler(config.get('DEFAULT', 'log_file'),
                                                        when="d",
                                                        interval=1,
                                                        backupCount=5)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(config.getint('DEFAULT', 'log_level'))
