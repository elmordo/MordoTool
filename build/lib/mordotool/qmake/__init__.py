# -*- coding: utf8 -*-

def setup_parser(parser):
    parser.add_argument("project", help="Project name to build")
    parser.add_argument("stage", help="Stage to build (default debug)", 
            choices=("release", "debug", "test"), default="debug", nargs="?")
    parser.add_argument("action", help="Selected action (default build)", 
            choices=("build", "clean", "rebuild"), default="build", nargs="?")

