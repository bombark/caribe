import argparse  # pragma: no cover
import os
from pathlib import Path

from . import Project, Workspace  # pragma: no cover

import importlib.util






def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m project_name` and `$ project_name `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """





    workspace = Workspace.instance()
    workspace.build()



    parser = argparse.ArgumentParser(
        description="project_name.",
        epilog="Enjoy the project_name functionality!",
    )
    # This is required positional argument
    #parser.add_argument(
    #    "name",
    #    type=str,
    #    help="The username",
    #    default="author_name",
    #)

    # This is optional named argument
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        help="The Message",
        default="Hello",
        required=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Optionally adds verbosity",
    )
    args = parser.parse_args()
    #print(f"{args.message} {args.name}!")
    if args.verbose:
        print("Verbose mode is on.")



if __name__ == "__main__":  # pragma: no cover
    main()
