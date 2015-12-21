# -*- coding: utf8 -*-

import os
import importlib


def discover():
    """ discover modules

    """
    modules = ModuleSet()
    base_path = os.path.dirname(os.path.realpath(__file__))
    directories = _get_directories(base_path)
    module_list = _filter_modules(directories)

    modules.set_from_dirs(module_list)

    return modules


def _get_directories(path):
    ''' return set of subdirectories in path

    Args:
        path (str): path where search to

    Returns:
        list: set of subdirectories in path
    '''
    entries = os.listdir(path)
    directories = list()

    for entry in entries:
        full_path = path + os.sep + entry
        if os.path.isdir(full_path):
            directories.append(full_path)

    return directories

def _filter_modules(directories):
    ''' filter only directories that are modules

    Args:
        directories (list): list of directory names

    Returns:
        list: set of only directories with __init__.py file
    '''
    module_list = list()

    for entry in directories:
        # if __init__ file is in subdir, this is the module

        init_name = entry + os.sep + "__init__.py"

        if os.path.isfile(init_name):
            module_list.append(entry)

    return module_list


class ModuleEntry(object):

    def __init__(self, module_name, module_path):
        self.name = module_name
        self.path = module_path

class ModuleSet(object):
    """ set of modules

    """

    def __init__(self):
        self.modules = list()

    def run_module(self, module_name, **kwargs):
        """ load and run module

        Args:
            module_name: module name
            kwargs (dict): options
        """
        full_name = "mordotool." + module_name + ".main"
        module = importlib.import_module(full_name)

        module.run(**kwargs)

    def set_from_dirs(self, dir_list):
        for entry in dir_list:
            dir_name = os.path.basename(entry)

            self.modules.append(ModuleEntry(dir_name, entry))

    def setup_argparser(self, parser):
        """ setup argument parser for registered modules

        """
        available_modules = list()
        subparsers = parser.add_subparsers(help="commands", dest="module_name")

        for module_entry in self.modules:
            subparser = subparsers.add_parser(module_entry.name)
            available_modules.append(module_entry.name)

            # setup subparser
            mod_destination = "mordotool." + module_entry.name
            prog_module = importlib.import_module(mod_destination)
            prog_module.setup_parser(subparser)

