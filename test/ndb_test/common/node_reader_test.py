#coding=utf-8

'''
Created on 2012-8-14

@author: Huiyugeng
'''
import unittest
import ndb

'''
NodeReader Unit Test
'''
class NodeReaderTest(unittest.TestCase):


    def test_load(self):
        config_map = ndb.read('test')
        print config_map
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()