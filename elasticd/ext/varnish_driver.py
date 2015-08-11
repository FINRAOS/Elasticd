from elasticd.plugins import Driver

from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader

import os

import logging

class VarnishDriver(Driver):
    def __init__(self, config):
        Driver.__init__(self, config)

    def update(self, resources):
        Driver.update(self, resources)
        if not resources:
            return

        # Get the templates directory.
        templates_dir = os.path.dirname(os.path.realpath(__file__)) + \
                        self._get_config_value('templates_path')
        templates_dir = os.path.realpath(templates_dir)

        # Setup template environment.
        env = Environment(loader=FileSystemLoader(templates_dir))
        # @todo - Ben - Make a config param for this.
        template = env.get_template(self._get_config_value('backend_vcl_path'))

        # Switch this to load out of current_state.
        rendered_result = template.render({'resources': resources})

        # Save to file.
        # @todo - Ben - Make a config param for where to save to.

        logging.debug(rendered_result)

        # Bounce the varnish config
        # exec(varnish reload)
