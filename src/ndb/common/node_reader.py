#coding=utf-8
'''
Created on 2012-10-31

@author: root
'''

import types

class NodeReader():
    def __init__(self):
        self.linenum=0
    
    '''
    Load Node File
    @param filename: Node file name
    
    @return: Node File Result(Dictionary Object)
    '''
    def read(self, filename):
        try:
            _list = [line for line in open(filename, 'r').readlines()]
        except:
            _list = []
        return self.__parse(_list)
    
    '''
    Parse Dictionary Object
    '''
    def __parse(self, _list):
        node ={}

        while self.linenum < len(_list):
            
            line = _list[self.linenum].strip()
    
            self.linenum = self.linenum + 1
            
            if line==None or line=='' or line.startswith('#'):
                continue
            
            if line.endswith('{'):
                node_name = line[0: line.find('{')].strip()
                node_value = self.__parse(_list)
                sub_node = node.get(node_name)
                
                if sub_node == None:
                    node[node_name] = node_value
                else:
                    node_list = sub_node if type(sub_node) == types.ListType else [sub_node]
                    node_list.append(node_value)
                    node[node_name] = node_list
                    
            elif line.endswith('}'):
                return node
            
            else:    
                if ':' in line:
                    node_name = line[0: line.find(':')]
                    item_value = line[line.find(':') + 1: len(line)]
                
                node_value = node.get(node_name) if node_name != None else None
                
                if node_value != None:
                    item_value_list = node_value if type(node_value) == types.ListType else [node_value]
                    item_value_list.append(item_value)   
                    node[node_name] = item_value_list
                else:
                    node[node_name] = item_value
        
        return node
