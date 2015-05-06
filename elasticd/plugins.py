
class BasePlugin():
    _config = None

    def __init__(self, config):
        """All elasticd plugins should inherit this class directly or indirectly.

        All common plugin functions should reside in this class.  At the moment only a handle to the
        configuration is common.

        Args:
            config (ConfigParser.ConfigParser): will be passed in form the plugin manager
        """
        _config = config


class Datastore(BasePlugin):
    def __init__(self, config):
        BasePlugin.__init__(self, config)

    def add_backend(self, ip_address):
        pass

    def remove_backend(self, ip_address):
        pass

    def get_all_backends(self):
        pass


class Driver(BasePlugin):
    def __init__(self, config):
        BasePlugin.__init__(self, config)

    def update(self, current_state):
        pass


class ResourceLocator(BasePlugin):
    def __init__(self, config):
        BasePlugin.__init__(self, config)

    def get_resources(self):
        pass