from elasticd.plugins import Driver


class VarnishDriver(Driver):
    def __init__(self, config):
        Driver.__init__(self, config)

    def update(self, current_state):
        Driver.update(self, current_state)

