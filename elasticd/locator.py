from base_plugin import BasePlugin


class ResourceLocator(BasePlugin):
    def __init__(self, config):
        BasePlugin.__init__(self, config)

    def get_resources(self):
        pass