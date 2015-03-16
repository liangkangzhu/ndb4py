#coding=utf-8

'''
ndb语句执行器

@author: Huiyugeng
'''

import types
import operate

class Statement:
    
    def __init__(self):
        pass
    
    '''
     * 执行ndb语句
     * 
     * @param query 需要执行的ndb语句
     * @param ndb ndb信息
     * @param action 自定义行为,如果使用自定义行为，则仅进行定位不执行值变更
     * 
     * @return 执行结果
    '''
    def execute(self, node, query, action):
        
        result = node
        command = query
        
        if ':' in query:
            command = query[0 : query.find(':')].strip()
            query = query[query.find(':') + 1 : len(query)].strip()
        
        query_items = query.split("!!");
        
        if query_items != None and len(query_items) > 0:
            
            path = query_items[0].strip()
            value = ''
            
            if len(query_items) > 1:
                value = query_items[1].strip()
            
            result_list = []
            
            if type(node) == types.ListType:
                
                for item in node:
                    if type(item) == types.DictionaryType:
                        if action != None:
                            result_list.append(self.__execute(node, command, path, None, action))
                        else:
                            result_list.append(self.__execute(node, command, path, value, None))
            elif type(node) == types.DictionaryType:
                if action != None:
                    return self.__execute(node, command, path, None, action)
                else:
                    return self.__execute(node, command, path, value, None)

            if len(result_list) > 0:
                return result_list

        return result

    def __execute(self, node, command, path, value, action):

        result = node
        
        if command != None:
            if command == 'select' or command == 'one':
                if action != None:
                    result = operate.select(node, path, action)
                else:
                    result = operate.select(node, path)

                if command == 'one':
                    if type(result) == types.ListType and len(result) > 0:
                        result = result[0]
                    else:
                        result = {}
            
            elif command == 'update':
                if action != None:
                    result = operate.update(node, path, value, action)
                else:
                    result = operate.update(node, path, value)
                    
            elif command == 'delete':
                if action != None:
                    result = operate.delete(node, path, value, action)
                else:
                    result = operate.delete(node, path, value)
            
            elif command == 'insert':
                if action != None:
                    result = operate.insert(node, path, value, action)
                else:
                    result = operate.insert(node, path, value)
        return result;
