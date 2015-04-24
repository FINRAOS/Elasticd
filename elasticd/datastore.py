from base_plugin import BasePlugin


class Datastore(BasePlugin):
    def __init__(self, config):
        BasePlugin.__init__(self, config)

    def add_backend(self, ip_address):
        pass

    def remove_backend(self, ip_address):
        pass

    def get_all_backends(self):
        pass

