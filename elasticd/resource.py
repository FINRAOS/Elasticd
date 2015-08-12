# A resource is something that can be located, stored, and passed to a driver for processing.
# In this regard all resources require compatible resource_locator, datastore, and driver plugins to function.

class Resource():
    def __init__(self):
        '''
        Base Resource Class.
        :return:
        '''

    def __str__(self):
        '''
        All Resources must implement __str__ as a way to persist them in a data store.
        :return:
        '''
        pass

    def __eq__(self, other):
        pass

class IPResource(Resource):
    _ip = ''

    def __init__(self, ip):
        Resource.__init__(self);
        self._ip = ip

    def get_ip(self):
        return self._ip

    def __str__(self):
        return self.get_ip()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__