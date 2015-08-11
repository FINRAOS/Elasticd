
"""Plugins module. This will contain all the base class definitions for the various pluggable components.

    BasePlugin - class for all plugins to inherit.

    Datastore - Datastore plugins provide storage for the backend host data.
        An in-memory plugin implementation is provided.  This is good if the number of backend hosts is small.

    Driver - Driver plugins are responsible for updating the front end technology to know about the new backends.
        A varnish driver is provided.  A VCL file will be updated when backend hosts are added or removed

    ResourceLocator -  ResourceLocator plugins are responsible for locating the backend hosts and their ip addresses.
        An AWS resource locator is provided.  Additional plugin implementations can support other cloud providers.

"""


DATASTORE_KEY = 'datastore'
DRIVER_KEY = 'driver'
RESOURCE_LOCATOR_KEY = 'resource-locator'


class BasePlugin():
    _config = None
    _config_section = None

    def __init__(self, config):
        """All elasticd plugins should inherit this class directly or indirectly.

        All common plugin functions should reside in this class.  At the moment only a handle to the
        configuration is common.

        :param config(ConfigParser.ConfigParser): will be passed in from the plugin manager
        :return:
        """
        self._config = config

    def _get_config_value(self, name):
        """
        Gets config value for the
        :param name:
        :return:  The value from the configuration section
        """
        return self._config.get(self._config_section, name)

    def _get_all_config_items(self):
        """
        Gets a list of tuples for all key values pairs in
        this section
        :return:  All items from this config section
        """
        return self.config.items(self._config_section)

class Datastore(BasePlugin):
    def __init__(self, config):
        """Datastore plugins are used to store the ip address information for all known backend hosts.

        All datastore plugins must inherit this class.  All methods require implementation.

        :param config(ConfigParser.ConfigParser): will be passed in from the plugin manager
        :return:
        """
        BasePlugin.__init__(self, config)
        self._config_section = DATASTORE_KEY

    def add_backend(self, ip_address):
        pass

    def remove_backend(self, ip_address):
        pass

    def get_all_backends(self):
        pass


class Driver(BasePlugin):
    def __init__(self, config):
        """Driver plugins are used to update and reload the front end service with the
        latest known ip address information of the backend hosts.

        All Driver plugins must inherit this class.  All methods require implementation.

        :param config (ConfigParser.ConfigParser): will be passed in from the plugin manager
        :return:
        """
        BasePlugin.__init__(self, config)
        self._config_section = DRIVER_KEY

    def update(self, current_state):
        pass


class ResourceLocator(BasePlugin):
    def __init__(self, config):
        """ResourceLocators plugins are used to identify the backend hosts and their ip addresses

        All ResourceLocator plugins must inherit this class.  All methods require implementation.

        :param config (ConfigParser.ConfigParser): will be passed in from the plugin manager
        :return:
        """
        BasePlugin.__init__(self, config)
        self._config_section = RESOURCE_LOCATOR_KEY

    def get_resources(self):
        pass
