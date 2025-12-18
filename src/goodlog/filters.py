import logging

from . import extra_info


class AddExtraInfoFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        setattr(record, "extra_info", extra_info.get_info())
        return True
