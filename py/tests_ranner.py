#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import tests_people

prodTestSuite = unittest.TestSuite()
prodTestSuite.addTest(unittest.makeSuite(tests_people.HumanTests))
print("count of tests: " + str(prodTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(prodTestSuite)
