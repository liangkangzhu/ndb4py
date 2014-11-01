# coding=utf-8

'''
Created on 2014-5-28

@author: Huiyugeng
'''

import node_locate

class NodeSelect(node_locate.NodeLocate):
    
    def __init__(self):
        self.result = []
    
    def select(self, node, path, action):
        self.action = action
        
        super(NodeSelect, self).locate(node, path);
        
        return self.result
    
    def do_action(self, node):
        if self.action != None:
            self.action(node)
        
        if node!= None:
            self.result.append(node)