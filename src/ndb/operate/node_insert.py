# coding=utf-8

'''
Created on 2014-5-28

@author: Huiyugeng
'''
import types

import node_locate

class NodeInsert(node_locate.NodeLocate):
    
    def __init__(self):
        self.columns = []
        self.clear = False
    
    def insert(self, node, path, value, action):
        self.update_value = super(NodeInsert, self).convert_value_map(value)
        self.action = action
        
        super(NodeInsert, self).locate(node, path, True);
        
        return node
    
    def do_action(self, node):
        if self.action != None:
            self.action(node)
        else:
            if node != None and type(node) == types.DictionaryType:
                for key in self.update_value:
                    node[key] = self.update_value.get(key)
        
