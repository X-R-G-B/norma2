from typing import List

from normatrix.checkers.c.comma import check_comma
from normatrix.checkers.c.comment import check_comment
from normatrix.checkers.c.header import check_header
from normatrix.checkers.c.indent import check_indent
from normatrix.checkers.c.libc_func import check_lf
from normatrix.checkers.c.nb_function_per_file import check_nfpf
from normatrix.checkers.c.nb_line_per_func import check_nlpf
from normatrix.checkers.c.nb_params import check_np
from normatrix.checkers.c.nested_branch import check_nb
from normatrix.checkers.c.operator import check_op
from normatrix.checkers.c.parenthesis import check_parenthesis
from normatrix.checkers.c.preprocessor import check_preprocessor
from normatrix.checkers.c.snake_case import check_sc
from normatrix.checkers.c.statements import check_statements
from normatrix.checkers.c.subscriptor import check_subscriptor
from normatrix.checkers.c.tabulation import check_tab
from normatrix.checkers.c.two_space import check_ts
from normatrix.errors.norm import _TemplateNormError
from normatrix.parser.cfile import CFile

checkerss = [
    check_nfpf,
    check_tab,
    check_comma,
    check_comment,
    check_nlpf,
    check_header,
    check_indent,
    check_lf,
    check_np,
    check_nb,
    check_op,
    check_parenthesis,
    check_preprocessor,
    check_sc,
    check_statements,
    check_subscriptor,
    check_ts,
]


def check(file: CFile) -> List[_TemplateNormError]:
    err = []
    for check in checkerss:
        cur_err = check(file)
        err.extend(cur_err)
    return err
