#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
#            CoinCap Project
# =============================================================================
# PROJECT : Guillaume Bally
# FILE : CoinCap.py
# DESCRIPTION :
"""

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.1.0     2019/02/25     Creation
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
import argparse

from MorseTranlator import MorseTranlator
mt = MorseTranlator()

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'Guillaume'
__date__ = '2019/09/25'
__version__ = '0.1.0'
__maintainer__ = 'Guillaume'

# [GLOBALS]--------------------------------------------------------------------


# [Functions]-------------------------------------------------------------------
def main(test):
    # mt.translate(test)
    mt.generate_sound(test)

# [MAIN]-----------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input a sentence or morse '
                                                 'code')

    parser.add_argument("test", help="Whatever you want to be translated words "
                                      "OR morse code")

    args = parser.parse_args()

    main(args.test)
