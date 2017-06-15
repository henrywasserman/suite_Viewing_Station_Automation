# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():            
    try:
        step_counter = 1
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        
        snooze(1.0)

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
