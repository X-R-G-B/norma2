import sys
from typing import Optional

import regex
from regexs import regexs_class

# https://regex101.com/r/I6fr0x/1
re = r"^( ){0,}\/{0,1}\/\*"
reg = regex.compile(re)


def is_token_not_escaped(text: str, index: int) -> bool:
    if index < 0 or len(text) <= index:
        return False
    if index - 1 == 0:
        return True
    if text[index - 1] != "\\":
        return True
    if index - 2 == 0:
        return False
    if text[index - 2] == "\\":
        return True
    return False


def search(text: str, timeout=1) -> Optional[regexs_class.RegexsResult]:
    try:
        res = reg.search(text, timeout=timeout)
    except TimeoutError as esc:
        print(f"ERROR: {__file__}:search: {esc}: {text}", file=sys.stderr)
        return None
    if res is None:
        return None
    start = res.start()
    end = res.end()
    if text[end] == ";":
        return regexs_class.RegexsResult(text, start, end)
    fifo = ["/*"]
    while fifo and len(text) > end + 2:
        end += 1
        if text[end : end + 2] == "*/" and is_token_not_escaped(text, end):
            fifo.pop(-1)
        elif text[end : end + 2] == "/*" and is_token_not_escaped(text, end):
            fifo.append("/*")
    regexs_class.RegexsResult(text, start, end)


def sub(text: str, replace: str, timeout=1) -> Optional[str]:
    is_ok = True
    while is_ok:
        patr = search(text, timeout=timeout)
        if patr:
            text = text.replace(patr.matching, replace)
        else:
            is_ok = False
    return text