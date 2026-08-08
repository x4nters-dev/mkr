from enum import Enum


class RunMode(Enum):
    AUTO = 'auto'
    SCRIPTS_ONLY = 'scripts_only'
    ROLLBACKS_ONLY = 'rollbacks_only'