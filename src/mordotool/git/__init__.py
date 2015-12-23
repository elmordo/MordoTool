# -*- coding: utf8 -*-

def setup_parser(parser):
   parser.add_argument("project", help="Project to manage") 
   parser.add_argument("action", help="Action to done", choices=("pull", "push", "commit", "status", "branch", "add"))
