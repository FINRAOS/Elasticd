__author__ = 'patelm'

import logging
import importlib


# key name that the PluginManager will use
DATASTORE_KEY = 'datastore'
DRIVER_KEY = 'driver'
RESOURCE_LOCATOR_KEY = 'resource-locator'

# There are the required methods for each plugin type.
#   The PluginManager will check to make sure any plugin being loaded has the
#       required attributes prior to instantiating the implementation
required_attributes = {DATASTORE_KEY: ['add_backend'],
                       DRIVER_KEY: ['update'],
                       RESOURCE_LOCATOR_KEY: ['get_resources']}

# todo lots of exception handling.

class PluginManager():
    # plugin cache
    plugins = {}

    def __init__(self, config):
        logging.debug('initializing plugins ')
        self._load_plugins(config)

    def get_datastore(self):
        """Simple 'getter'

        :return: The loaded Datastore plugin implementation
        :rtype: elasticd.plugins.Datastore
        """
        return self.plugins[DATASTORE_KEY]

    def get_driver(self):
        """Simple 'getter'

        :return: The loaded Driver plugin implementation
        :rtype: elasticd.plugins.Driver
        """
        return self.plugins[DRIVER_KEY]

    def get_resource_locator(self):
        """Simple 'getter'

        :return: The loaded ResourceLocator plugin implementation
        :rtype: elasticd.plugins.ResourceLocator
        """
        return self.plugins[RESOURCE_LOCATOR_KEY]

    def _load_plugins(self, config):
        self._load_plugin(DATASTORE_KEY, config)
        self._load_plugin(DRIVER_KEY, config)
        self._load_plugin(RESOURCE_LOCATOR_KEY, config)

    def _load_plugin(self, plugin_type, config):
        logging.debug('Loading %s' % plugin_type)

        module_name = config.get(plugin_type, 'module_name')
        plugin_class = config.get(plugin_type, 'plugin_class')

        # Load the module and get a handle to the class definition.
        module = importlib.import_module(module_name)
        plugin_class = getattr(module, plugin_class)

        # Validate the class definition is correct.
        if self._plugin_is_valid(plugin_class, required_attributes[plugin_type]):
            # Instantiate the class and cache it within this plugin manager
            self.plugins[plugin_type] = plugin_class(config)

    @staticmethod
    def _plugin_is_valid(plugin, _required_attributes):
        """Check the plugin implementation to be loaded is valid by looking for the required attributes

        :param plugin: The implementation to be loaded
        :param _required_attributes: The attributes required for this implementation
        :return: True the implementation of the plugin is valid; False otherwise
        :rtype: bool
        """
        valid = True
        for attribute in _required_attributes:
            if hasattr(plugin, attribute):
                valid = True
            else:
                return False
        return valid
