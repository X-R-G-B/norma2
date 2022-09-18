import argparse

from normatrix.config.config_class import Config, OutputFormat

__FULL_DOC = f"""SOURCE:
    https://github.com/Saverio976/NorMatrix

UPDATE:
    - if you install it with 'pip'
        pip install -U normatrix
    - if you install it with git
        git pull
    - other method:
        (do it yourself)

CONFIGS:
    normatrix can read a special json file for configuration.
    -> put a `.normatrix.json` file on the path where you execute normatrix
    -> and execute normatrix like you did it before

    default configuration file:
        ```json
        {{
            "libc_banned_func": {Config.libc_banned_func},
            "no_libc_banned_func": [],
            "file_extension_banned": {Config.file_extension_banned},
            "no_file_extension_banned": [],
            "features": {Config.preview}
            "operators_plugin": {Config.operators_plugin}
        }}
        ```

    for further information read the README.md on
    https://github.com/Saverio976/NorMatrix
"""

options = [
    {
        "name_or_flags": "--no-operators-plugin",
        "action": "store_const",
        "dest": "operators_plugin",
        "const": not Config.operators_plugin,
        "default": Config.operators_plugin,
        "help": "remove the operators pluggin (because it print"
        " some false positiv for now)",
    },
    {
        "name_or_flags": "--preview",
        "action": "store_const",
        "dest": "preview",
        "const": not Config.preview,
        "default": Config.preview,
        "help": "add some plugin that are added recently",
    },
    {
        "name_or_flags": "--only-errors",
        "action": "store_const",
        "dest": "only_error",
        "const": not Config.only_error,
        "default": Config.only_error,
        "help": "print only bad files with errors",
    },
    {
        "name_or_flags": "--no-fclean",
        "action": "store_const",
        "dest": "no_fclean",
        "const": not Config.no_fclean,
        "default": Config.no_fclean,
        "help": 'if you want normatrix dont do a "make fclean" at the end',
    },
    {
        "name_or_flags": "--link-line",
        "action": "store_const",
        "dest": "link_line",
        "const": not Config.link_line,
        "default": Config.link_line,
        "help": 'to have the "link" to the file (in vscode terminal you can'
        " click it and it will open the file at the line of the error)",
    },
    {
        "name_or_flags": "--tests-run",
        "action": "store_const",
        "dest": "pass_test",
        "const": True,
        "default": False,
        "help": "run the unit tests for normatrix",
    },
    {
        "name_or_flags": "--output",
        "metavar": "format",
        "choices": OutputFormat,
        "dest": "output_format",
        "default": Config.format,
        "help": "tell which output format to use [html, md, term_color,"
        " term_rich]; for html the file is normatrix-result.html;"
        " for md the file is normatrix-result.md, other are on stdout",
    },
    {
        "name_or_flags": "paths",
        "metavar": "paths",
        "nargs": "*",
        "default": Config.paths,
        "help": "list of path to check (default: the current working directory)",
    },
]


def _parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Norm Checker For the C Epitech Coding Style",
        epilog=__FULL_DOC,
    )
    for args in options:
        parser.add_argument(**args)
    result = parser.parse_args()
    return result


def from_cmdline() -> Config:
    conf = Config()
    args = _parser()
    conf = conf + args
    return conf
