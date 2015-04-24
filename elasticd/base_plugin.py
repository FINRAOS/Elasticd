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

