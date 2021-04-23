#!/usr/bin/env python
"""
logger tests
"""

import unittest
## import model specific functions and variables
from logger import *

class LoggerTest(unittest.TestCase):
    """
    test the essential log functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train logfile
        today = date.today()
        logfile = "{}-{}-{}.log".format("train",today.year,today.month)
        log_path = os.path.join(LOG_DIR, logfile)
        
        self.assertTrue(os.path.exists(log_path))



    def test_02_predict(self):
        """
        test the predict functionality
        """
        
        ## train logfile
        today = date.today()
        logfile = "{}-{}-{}.log".format("predict",today.year,today.month)
        log_path = os.path.join(LOG_DIR, logfile)
        
        self.assertTrue(os.path.exists(log_path))

        
        
    def test_03_load(self):
        """
        test the load functionality
        """

        ## load model first
        logfile = log_load(env = 'train',year=2021,month=4, verbose=False)
        logpath = os.path.join(LOG_DIR, logfile)
        with open(logpath, "r") as log:
            text = log.read()
        self.assertTrue(len(text.split("\n"))>2)        
        
        
### Run the tests
if __name__ == '__main__':
    unittest.main()
