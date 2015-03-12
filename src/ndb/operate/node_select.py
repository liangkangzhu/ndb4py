# coding=utf-8

'''
ndb节点查询

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