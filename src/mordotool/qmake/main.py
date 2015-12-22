# -*- coding: utf8 -*-

import sys
import os

def run(**kwargs):
    project_name = kwargs["project"]
    stage = kwargs["stage"]
    dest_path = assemble_dest_path(project_name, stage)

    # prepare destination and refresh make file
    prepare_path(dest_path)
    refresh_makefile(project_name, stage, dest_path)
    
    # resolve action
    action_name = kwargs["action"]

    if action_name == "clean":
        clean_project(dest_path)
    elif action_name == "build":
        build_project(dest_path, project_name, stage)
    elif action_name == "rebuild":
        clean_project(dest_path)
        build_project(dest_path, project_name, stage)

def prepare_path(full_path):
    path_parts = full_path.split(os.sep)

    # test for parts exist
    walked_path = ""

    for part in path_parts:
        walked_path += part + "/"

        if not os.path.isdir(walked_path):
            # create directory
            os.mkdir(walked_path)

def assemble_dest_path(project_name, stage):
    script_path = os.getcwd()
    return "%s/build/%s/%s" % (script_path, stage, project_name)

def assemble_makefile_name(dest_path):
    return "%s%sMakefile" % (dest_path, os.sep)

def assemble_lib_path(project_name, stage):
    script_path = os.getcwd()
    return "%s/build/%s/lib/" % (script_path, stage)

def refresh_makefile(project_name, stage, dest_path):
    """ create Makefile for project's stage in destination path

    """
    make_file = assemble_makefile_name(dest_path)

    additional_args = []
    make_stage = stage

    # add additional commands
    if stage in ("debug", "test"):
        additional_args.append("CONFIG+=debug")

        if stage == "test":
            additional_args.append("CONFIG+=TEST")
            make_stage="debug"

    # assemble command
    joined_arguments = " ".join(additional_args)
    cmd = "qmake %s %s STAGE=%s -o %s" % (project_name, joined_arguments, make_stage, make_file)

    print "Start generating Makefile for %s (%s) to %s" % (project_name, stage, dest_path)
    os.system(cmd)
    print "Makefile generated"

def clean_project(dest_path):
    cmd = "make -C %s clean" % dest_path
    print "Cleaning project project in %s" % dest_path
    os.system(cmd)
    print "Project cleaned"

def build_project(dest_path, project_name, stage):
    cmd = "make -C %s" % dest_path

    print "Building project in %s" % dest_path
    os.system(cmd)
    print "Building finished"

    print "Linking library to the local library storage"

    # target destination
    lib_path = assemble_lib_path(project_name, stage)

    # source files
    lib_sources = "%s/lib%s.so*" % (dest_path, project_name)
    prepare_path(lib_path)
    cmd = "ln -s %s %s" % (lib_sources, lib_path)
    os.system(cmd)
    print "Linking finished"


