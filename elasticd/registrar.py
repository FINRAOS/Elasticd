__author__ = 'patelm'

import logging


class Registrar():
    """Responsible for registering/deregistering backends and informing the Driver with the latest information

        Uses the datastore to keep track of known backends
        Call the driver with the latest known state of the backends
    """

    datastore = None
    driver = None
    last_change = 0
    last_run = 0

    def __init__(self, datastore, driver):
        """
        Args:
            datastore (Datastore): Datastore plugin to use when storing backend ip addresses.
            driver (Driver): Driver plugin to use to update the frontend config.
        """
        # todo - Ben - Check plugin types.
        self.datastore = datastore
        self.driver = driver

    def register(self, resource):
        """Register a new backend
        Args:
            resource (String): ip address of the backend.
        """
        # Check if the backend is already in the list.
        # If not add it.
        # If yes, don't duplicate.
        all_resources = self.datastore.get_all_backends()
        if resource not in all_resources:
            self.datastore.add_backend(resource)
            self.last_change += 1
            logging.debug('do register')
        logging.debug("don't do register")

    def deregister(self, resource):
        """remove a backend from the registry
        Args:
            resource (String): ip address of the backend.
        """
        self.datastore.remove_backend(resource)
        self.last_change += 1
        logging.debug("Do deregister.")

    def process(self):
        """Inform the driver of the current state of the backends
        """
        print 'informing the driver'
        if self.last_change > self.last_run:
            logging.debug("Calling driver update.")
            backends = self.datastore.get_all_backends()
            self.driver.update(backends)
            # Note we've caught up.
            self.last_run = self.last_change
        logging.debug("Not calling driver update.")
