from docopt import docopt
from typing import Any


class AbstractCmd:
    @classmethod
    def run(cls, doc) -> Any:
        print(docopt(doc))
        cls.exec(cls.Args.from_dict(docopt(doc), restrict=False, force_cast=True))


