# -*- coding: utf8 -*-

from distutils.core import setup

setup(
       name="MordoTool",
       description="Project management utility tool",
       author="Petr Jindra",
       author_email="el.mordo@gmail.com",
       packages=[ "mordotool", "mordotool.qmake", "mordotool.git" ],
       package_dir={ "mordotool" : "src/mordotool" },
       scripts=[ "scripts/mortool.py" ]
    )
