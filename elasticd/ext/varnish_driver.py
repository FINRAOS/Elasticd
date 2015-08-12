from elasticd.plugins import Driver

from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
import subprocess
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
        template = env.get_template(self._get_config_value('template_name'))

        # Switch this to load out of current_state.
        rendered_result = template.render({'resources': resources})

        # Save to file.
        filename = '%s/%s' % (self._get_config_value('vcl_output_path'),
                              self._get_config_value('vcl_output_name'))
        filename = os.path.realpath(filename)

        f = open(filename, "w")
        f.write(rendered_result)
        f.close()

        logging.debug(rendered_result)

        # Bounce the varnish config
        if self._config.getboolean(self._config_section, 'varnish_reload'):
            subprocess.call('service varnishd reload')
