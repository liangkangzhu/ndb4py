#coding=utf-8

'''
ndb存储

将ndb的数据内容保存至文件中

@author: Huiyugeng
'''

import types

class NodeWriter():
    
    '''
    write Node Information to File
    '''
    def write_node(self, filename, node_name, node):
        output = open(filename, 'w')
        output.write(self.print_node(node_name, node))
        output.close()
    
    '''
    print Dictionary to Node Information
    
    @param node_name: Root node name
    @param node: Dictionary Object
    
    @return: Node Information
    '''
    def print_node(self, node_name, node):
        
        result = []
        result.append(node_name + '{\n')
        for key in node.keys():
            value = node[key]
            if type(value) == types.ListType and len(value)!=0:
                for item in value:
                    if type(item) == types.DictionaryType:
                        result.append(self.build_node(key, item))
                    if type(item) == types.StringType:
                        result.append(key + ':' + item + '\n')
                        
            if type(value) == types.DictionaryType and len(value.keys())!=0:
                result.append(self.build_node(key, value))
                
            if (type(value) == types.StringType or type(value) == types.UnicodeType) and value!='':
                result.append( key + ':' + value +'\n')
            
        result.append('}\n')
        return ''.join(result)

