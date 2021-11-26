"""
project_name base module.

This is the principal module of the project_name project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

import os
import importlib.util
from pathlib import Path


class Project:
    def instance():
        pyscript_url = getScriptUrl("project.py")
        spec = importlib.util.spec_from_file_location("caribe.Project", pyscript_url)
        instance = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(instance)
        return instance

    def getRoot():
        return getScriptPath("project.py")


g_project_url = []

class Workspace:
    def list(self) -> []:
        """
        Base method.
        """
        return "hello from BaseClass"

    def instance():
        pyscript_url = Workspace.getScriptUrl()
        spec = importlib.util.spec_from_file_location("caribe.Workspace", pyscript_url)
        instance = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(instance)
        return instance


    def makeProject(self):
        pass

    def getScriptUrl():
        return getScriptUrl("workspace.py")

    def include(name):
        g_project_url.append(name)

    #def __call__(self) -> str:
    #    return self.base_method()



def getScriptUrl(name: str):
    pyscript_path = Path("./")
    for i in range(10):
        pyscript_url = pyscript_path / name
        if os.path.exists(pyscript_url):
            break
        pyscript_path = pyscript_path / ".."
    return pyscript_url

def getScriptPath(name: str):
    pyscript_path = Path("./")
    for i in range(10):
        pyscript_url = pyscript_path / name
        if os.path.exists(pyscript_url):
            break
        pyscript_path = pyscript_path / ".."
    return pyscript_path


def base_function() -> str:
    """
    Base function.
    """
    return "hello from base function"
