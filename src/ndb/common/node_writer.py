# coding=utf-8

import types

class NodeWriter():
    '''
    #输出和存储ndb内容
    '''

    def write_node(self, filename, node_name, node):
        '''
        #将节点数据信息写入文件
        '''
        output = open(filename, 'w')
        output.write(self.print_node(node_name, node))
        output.close()
    

    def print_node(self, node_name, node):
        '''
        #将节点数据内容输出为字符串
        
        @param node_name: 根节点名称
        @param node: 节点数据
        
        @return: 节点数据字符串
        '''
        result = []
        result.append(node_name + '{\n')
        for key in node.keys():
            value = node[key]
            if type(value) == types.ListType and len(value) != 0:
                for item in value:
                    if type(item) == types.DictionaryType:
                        result.append(self.print_node(key, item))
                    if type(item) == types.StringType:
                        result.append(key + ':' + item + '\n')
                        
            if type(value) == types.DictionaryType and len(value.keys())!=0:
                result.append(self.print_node(key, value))
                
            if (type(value) == types.StringType or type(value) == types.UnicodeType) and value!='':
                result.append( key + ':' + value +'\n')
                
            if type(value) == types.IntType or type(value) == types.LongType or type(value) == types.BooleanType:
                result.append( key + ':' + str(value) +'\n')
            
        result.append('}\n')
        return ''.join(result)

    '''
    print Dictionary to XML Information
    
    @param node_name: Root node name
    @param node: Dictionary Object
    
    @return: XML Information
    '''    
    def print_xml(self, node_name, node):
        result = []
        result.append('<' + node_name + ">\n")
        for key in node.keys():
            value = node[key]
            if type(value) == types.ListType and len(value) != 0:
                for item in value:
                    if type(item) == types.DictionaryType:
                        result.append(self.print_xml(key, item))
                    if type(item) == types.StringType:
                        result.append('<' + key + '>' + item + '</' + key + '>\n')
                        
            if type(value) == types.DictionaryType and len(value.keys()) != 0:
                result.append(self.print_xml(key, value))
                
            if (type(value) == types.StringType or type(value) == types.UnicodeType) and value != '':
                result.append('<' + key + '>' + value + '</' + key + '>\n')
                
            if type(value) == types.IntType or type(value) == types.LongType or type(value) == types.BooleanType:
                result.append('<' + key + '>' + str(value) + '</' + key + '>\n')
            
        result.append('</' + node_name + ">\n")
        return ''.join(result)
