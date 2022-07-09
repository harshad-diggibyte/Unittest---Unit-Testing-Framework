#UNITTEST
#BuiltIn Python distribution Network, Not required pip install.

import unittest

# To invoke the unittest Framework -(it will capture them, and run one by one)
if __name__ == "__main__":
    unittest.main()

#You need to write 1st test class before test class
# All test function are part of test class

import unittest

def test_fn():

if __name__ == "__main__":
    unittest.main()

#All the unittest classes derived from "unittest.TestCase"
#This is the only way the function inside the unit class will be inovke the unittest framework.
#class is just a logical convinience feature, functions, area.

import unittest

class LearnTest(unittest.TestCase)

if __name__ == "__main__":
    unittest.main()

# all unittest start with keyword call "test"
# if it not start with "test" it will not run.
# '_' not mandatory but we have to follow for coding guidelines.also help you to name test in better way.

# It will show "Ran 1 tests in ..."
import unittest
class LearnTest(unittest.TestCase):
    def test_func1(self):
        pass
if __name__ == "__main__":
    unittest.main()

# It will show "Ran 2 tests in ..."
import unittest
class LearnTest(unittest.TestCase):
    def test_func1(self):
        pass
    def test_func1(self):
        pass
if __name__ == "__main__":
    unittest.main()

# It will show "Ran 2 tests in ..."
import unittest
class LearnTest(unittest.TestCase)
    def myfunc(self):  # <-- it will not run
        pass
    def test_func1(self):
        pass
    def test_func1(self):
        pass

if __name__ == "__main__":
    unittest.main()

# Creating sum function

import unittest
def sum(a, b):
    return a + b
class SumTest(unittest.TestCase):

    def test_sumfunc_1(self):
        # Arrange
        a = 10
        b = 20
        # Act
        result = sum(a, b)
        # Assert
        self.assertEqual(result, a + b)

if __name__ == "__main__":
    unittest.main()



import unittest
def sum(a, b):
    return a + b

class SumTest(unittest.TestCase):

    # setup function called before each and every func.
    def setUp(self):
        print("SETUP Called...")
        self.a = 10
        self.b = 20

    def test_sumfunc_1(self):
        print("Test func1 Called...")
        # Act
        result = sum(self.a, self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)

    def test_sumfunc_2(self):
        print("Test func2 Called...")
        # Act
        result = sum(self.b, self.a)
        # Assert
        self.assertEqual(result, self.a + self.b)

if __name__ == "__main__":
    unittest.main()


import unittest
def sum(a, b):
    return a + b
class SumTest(unittest.TestCase):
    # setup function called before each and every func.
    def setUp(self):
        print("SETUP Called...")
        self.a = 10
        self.b = 20

    # Teardown function
    def tearDown(self):
        self.a = 0
        self.b = 0
        print("TEARDOWN CALLED....")

    def test_sumfunc_1(self):
        print("Test func1 Called...")
        # Act
        result = sum(self.a, self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)

    def test_sumfunc_2(self):
        print("Test func2 Called...")
        # Act
        result = sum(self.b, self.a)
        # Assert
        self.assertEqual(result, self.a + self.b)

if __name__ == "__main__":
    unittest.main()

# SETUP AND TEARDOWN function is for making sure that all the pre-rquesites are available.

# Assertions

import unittest
class LearnUnitTest(unittest.TestCase):

    def test_sample(self):
        a = 10
        b = 20
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()


import unittest
class LearnUnitTest(unittest.TestCase):

    def test_sample(self):
        a = 1
        b = 10
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
# this will pass

# other case --->
import unittest
class LearnUnitTest(unittest.TestCase):

    def test_sample(self):
        a = 1
        b = 10
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()
# this will not pass


import unittest
class LearnUnitTest(unittest.TestCase):

    def test_sample(self):
        a = 1
        b = 10
        # self.assertEqual(a,b,msg="1 is not equal to 10")
        self.assertIs(a, b)

if __name__ == "__main__":
    unittest.main()

