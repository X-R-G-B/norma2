import os
from pathlib import Path
from typing import List

from normatrix.config.config_class import Config
from normatrix.errors.norm import _TemplateNormError


class _File:
    def __init__(self, filepath: str, config: Config) -> None:
        if not os.path.isfile(filepath):
            raise os.error(f"Invalid filepath: {filepath}")
        self.filepath = filepath
        self.text_origin = Path(self.filepath).read_text()
        self.lines_origin = []
        self.parsed_context = []
        self.config = config
        self.is_init = False

    def init(self):
        pass

    def check_norm(self) -> List[_TemplateNormError]:
        return []