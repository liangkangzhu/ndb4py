#coding=utf-8

'''
Created on 2012-8-5

@author: Huiyugeng
'''
import unittest
import ndb

'''
Node Locate Unit Test
'''
class StatementTest(unittest.TestCase):
    
    def setUp(self):  
        self.node = ndb.load('../../resource/example_1.txt')
    
    def test_select(self):
        
        result = ndb.execute(self.node, 'select:firewall->interface->name:dmz && ip:192.168.12.2')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get('ip'), '192.168.12.2')
        
        result = ndb.execute(self.node, 'select:firewall->interface->name:/dmz|inside/ && ip:/192.168.12.2|192.168.228.122/')
        self.assertEqual(len(result), 2)
            
        result = ndb.execute(self.node, 'select:firewall->interface')
        self.assertEqual(len(result), 3)
        
        result = ndb.execute(self.node, 'select:firewall->interface->mask:255.255.255.0')
        self.assertEqual(len(result), 3)
        
        result = ndb.execute(self.node, 'select:firewall->access-list->action:/permit|deny/')
        self.assertEqual(len(result), 11)
        
        result = ndb.execute(self.node, 'select:firewall->:/\\S+-list/->action:/permit|deny/')
        self.assertEqual(len(result), 11)
        
        result = ndb.execute(self.node, 'select:firewall->interface->security:[50,100]')
        self.assertEqual(len(result), 2)
        
        result = ndb.execute(self.node, 'select:firewall->:/host|interface/')
        self.assertEqual(len(result), 4)
    
    def test_update(self):
        
        result = ndb.execute(self.node, 'update:firewall->interface->name:dmz !! name=dmz2,mask=255.255.255.32')
        result = ndb.execute(result, 'select:firewall->interface->name:dmz2')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get('ip'), '192.168.12.2')
        
    def test_delete(self):
        result = ndb.execute(self.node, 'delete:firewall->interface->name:inside !! [mask, security]')
        result = ndb.execute(result, 'select:firewall->interface->name:inside')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get("mask"), None)
        self.assertEqual(result[0].get("security"), None)
        
        result = ndb.execute(self.node, 'delete:firewall->interface->name:outside !! block')
        result = ndb.execute(result, 'select:firewall->interface->name:outside')
        self.assertEqual(len(result), 0)
    
    def test_insert(self):
        result = ndb.execute(self.node, 'insert:firewall->nat !! name=192.168.9.21,ip=192.168.9.21')
        select_result = ndb.execute(result, 'select:firewall->nat')
        self.assertEqual(len(select_result), 1)
        
        result = ndb.execute(result, 'insert:firewall->nat !! name=192.168.9.22,ip=192.168.9.22')
        select_result = ndb.execute(result, 'select:firewall->nat')
        self.assertEqual(len(select_result), 2)
        
        result = ndb.execute(result, 'insert:firewall->nat !! name=192.168.9.23,ip=192.168.9.23')
        select_result = ndb.execute(result, 'select:firewall->nat')
        self.assertEqual(len(select_result), 3)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()