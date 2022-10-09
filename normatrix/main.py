from typing import List

from normatrix.checkers.check import check as check_norm
from normatrix.config.config_class import Config
from normatrix.errors.norm import _TemplateNormError
from normatrix.parser import file, get_files
from normatrix.tests.main import main as main_test


def print_header(config: Config):
    if not config.only_exit_code:
        config.console.rule("[bold blue]normatrix", style="bold blue")
        config.console.print(
            "Check the Epitech C Coding Style", style="italic"
        )  # noqa: E501
        config.console.line(2)


def print_config(config: Config):
    if config.show_config:
        config.console.rule(
            "Parsed Config from cmdline + `.normatrix.json`", style="blue"
        )
        config.console.print_json(data=config)
        config.console.line()


def pass_test(config: Config) -> int:
    config.console.rule("Execute Tests", style="blue")
    ex = main_test()
    config.console.line()
    return ex


def check_file(config, filepath: str) -> List[_TemplateNormError]:
    list_err: List[_TemplateNormError] = []
    if not config.only_exit_code:
        config.console.print(f"[magenta underline]{filepath}")
    try:
        f = file.File(filepath, config)
        f.init(config)
        list_err = f.check_norm(config)
        list_err.extend(check_norm(f))
    except Exception:
        config.console.print(":warning: [red]An Error Occured")
        config.console.print_exception()
    else:
        if not config.only_exit_code and list_err:
            config.console.print("\n".join([f"- {x}" for x in list_err]))
    if not config.only_exit_code:
        if not list_err:
            config.console.print("FILE [green]OK :heavy_check_mark:")
        else:
            config.console.print("FILE [red]KO x")
        config.console.line()
    return list_err


def main(config: Config) -> int:
    nb_errors = 0
    print_header(config)
    print_config(config)

    if config.pass_test:
        return pass_test(config)

    if not config.only_exit_code:
        config.console.rule("Norm:", style="blue")
    for folder in config.paths:
        list_all_err: List[List[_TemplateNormError]] = []
        try:
            files_to_check = get_files.get_all_files(folder, [], [])
        except Exception:
            config.console.print(":warning: [red]An Error Occured")
            config.console.print_exception()
            continue
        for filepath in files_to_check:
            list_all_err.append(check_file(config, filepath))
            nb_errors += len(list_all_err[-1])
        # TODO: stat for folder
    if nb_errors:
        return 42
    return 0
