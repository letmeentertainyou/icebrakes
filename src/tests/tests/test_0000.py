'''Doc strings GOOabove the block of test code for pylint.
See TESTING_README for a full write up.'''
from src.tests.tools import pytest_runner

##################################################
############### BEGIN TEST CODE ##################
##################################################
FOO = 0
BAR = 0 #$
GOO = 0
CAR = 0 #$
FOO = GOO * BAR
##################################################
################ END TEST CODE ###################
##################################################

def test() -> None:
    '''This is the default test implementation, call a test with the number of your test.'''
    pytest_runner('0')


#Copyright © 2023 Lars S.
