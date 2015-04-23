from base_plugin import BasePlugin


class Driver(BasePlugin):
    def __init__(self, config):
        BasePlugin.__init__(self, config)

    def update(self, current_state):
        pass