#-*- coding: utf8 -*-

import mordotool.config as config
import mordotool.modules as modules


def run():
    parser = config.create_config_parser()

    module_set = modules.discover()
    module_set.setup_argparser(parser)

    vals = parser.parse_args().__dict__
    module_name = vals["module_name"]
    vals.pop("module_name")

    module_set.run_module(module_name, **vals)

if __name__ == "__main__":
    run()
