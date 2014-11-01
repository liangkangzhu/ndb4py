# coding=utf-8

'''
Created on 2014-5-28

@author: Huiyugeng
'''
import types

import node_locate

class NodeUpdate(node_locate.NodeLocate):
    
    def __init__(self):
        pass
    
    def update(self, node, path, value, action):
        self.update_value = super(NodeUpdate, self).convert_value_map(value)
        self.action = action
        
        super(NodeUpdate, self).locate(node, path);
        
        return node
    
    def do_action(self, node):
        if self.action != None:
            self.action(node)
        else:
            if self.update_value != None and type(node) == types.DictionaryType:
                for key in self.update_value:
                    node[key] = self.update_value.get(key)
        
