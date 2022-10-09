from typing import List

from normatrix.errors.norm import TooManyFunctions, _TemplateNormError
from normatrix.parser.cfile import CContextType, CFile


def check_nfpf(file: CFile) -> List[_TemplateNormError]:
    nb_func = 0
    for ctx in file.parsed_context:
        if ctx.type == CContextType.FUNCTION:
            nb_func += 1
    if nb_func > 5:
        return [TooManyFunctions(file.filepath, f"{nb_func} > 5 authorized")]
    return []
