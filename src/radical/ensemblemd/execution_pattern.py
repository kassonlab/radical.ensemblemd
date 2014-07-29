#!/usr/bin/env python

"""TODO: Docstring.
"""

__author__    = "Ole Weider <ole.weidner@rutgers.edu>"
__copyright__ = "Copyright 2014, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.ensemblemd.engine import Engine

#-------------------------------------------------------------------------------
#
class ExecutionPattern(object):
    """An execution pattern represents a specific molecular dynamics workflow
       pattern. Pattern is the abstract base-class and not used directly. 
       To create an execution pattern, use either of the following derived 
       classes:

         * :class:`radical.ensemblemd.DummyPattern`
         * :class:`radical.ensemblemd.SimulationAnalysisPattern
         * ...`
    """

    def __init__(self):
        """Creates a new ExecutionPattern instance.
        """

        self._engine = Engine()