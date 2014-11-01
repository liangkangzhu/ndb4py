# coding=utf-8

'''
Created on 2014-5-28

@author: Huiyugeng
'''

import types
import regex

class NodeLocate(object):
    
    '''
    Locate node by expression
     
    Search query like: A->B->C:Value
     
    @param query: search query
    @param node: search node(Dictionary Object) 
     
    @return search result
    '''
    def locate(self, node, query, is_create = False):
        if query == None or query == "":
            return
        
        query_key = query
        sub_query = query
        
        if type(node) == types.ListType:
            for item in node:
                self.locate(item, sub_query, is_create)
        elif type(node) == types.DictionaryType:
            if '->' in query:
                query_key = query[0 : query.find('->')].strip()
                sub_query = query[query.find('->') + 2 : len(query)].strip() #2 is "->"'s length

            if is_create == True and node.has_key(query_key) == False:
                node[query_key] = {}
            
            if sub_query != query_key or query_key.startswith(':'):
                if query_key.startswith(':'):
                    exp = query_key[1:]

                    for key in node:
                        if self.check_value(key, exp):
                            if sub_query.startswith(':'):
                                self.locate(node, key, is_create)
                            else:
                                self.locate(node.get(key), sub_query, is_create)
                else:
                    self.locate(node.get(query_key), sub_query, is_create)

            else:
                if ':' in sub_query:
                    
                    match_items = sub_query.split('&&')
                    
                    match_result = True
                    
                    for match_item in match_items:
                        
                        items = match_item.strip().split(':')
                        if len(items) == 2:
                            
                            key = items[0].strip()
                            exp = items[1].strip()
                            
                            value = node.get(key)
                            
                            if self.check_value(value, exp) == False:
                                match_result = False
                    
                    if match_result == True:
                        self.do_action(node)

                else:
                    
                    result = node.get(query_key)

                    if is_create == True:
                        
                        if type(result) == types.ListType:
                            item = {}
                            self.do_action(item)
                            result.append(item)
                        elif type(result) == types.DictionaryType:
                            if len(result) == 0:
                                self.do_action(result)
                            else:
                                item = {}
                                self.do_action(item)
                                
                                node[query_key] = [result, item]

                    else:
                        if type(result) == types.ListType:
                            for item in result:
                                self.do_action(item)
                        else:
                            self.do_action(result)
                            
    def check_value(self, value, exp):
        # regex valueression match
        if len(exp) > 2 and exp.startswith('/') and exp.endswith('/'):
            regex_str = exp[1: len(exp) - 1]
            if regex.check_line(regex_str, value):
                return True
        # exp region match
        if len(exp) > 3 and exp.startswith('[') and exp.endswith(']'):
            region = exp[1: len(exp) - 1].split(',')
            if len(region) == 2 and type(value) == types.StringType:
                _min = int(region[0])
                _max = int(region[1])
                value = int(value)
                if value >= _min and value <= _max:
                    return True
        # startwith match
        if exp.startswith('^'):
            if value.startswith(exp[1: len(exp)]):
                return True
        # endswith match
        if exp.endswith('$'):
            if value.endswith(exp[: len(exp) - 1]):
                return True
        # exp match
        else:
            if value != None and value == exp:
                return True
        
        return False
    
    def do_action(self, node):
        self.do_action(node)
    
    
    def convert_value_map(self, update_value):
        update_value_map = {}
        values = update_value.split(',')
        for value in values:
            value_pair = value.split('=')
            if len(value_pair) == 2:
                update_value_map[value_pair[0].strip()] = value_pair[1].strip()
        
        return update_value_map

