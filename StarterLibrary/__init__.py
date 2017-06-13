# -*- coding: utf-8 -*-
from robot.api import logger

import os
import signal
import subprocess

__version__ = '1.0'
ROBOT_LIBRARY_DOC_FORMAT = 'reST'


class StarterLibrary:
    """Minimal example for a Robot Framework Library.
    """

    # TEST CASE => New instance is created for every test case.
    # TEST SUITE => New instance is created for every test suite.
    # GLOBAL => Only one instance is created during the whole test execution.
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        """WebpackLibrary can be imported with optional arguments.
        """
        pass

    def my_keyword(self, my_first_parameter):
        logger.console("my_keyword")
