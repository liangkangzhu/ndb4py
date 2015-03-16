# coding=utf-8


import types

import node_locate

class NodeInsert(node_locate.NodeLocate):
    '''
    #节点插入：向ndb中插入数据
    #当遇到路径中没有的节点时，主动建立路径节点，并在末尾节点插入数据
    '''
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
        
