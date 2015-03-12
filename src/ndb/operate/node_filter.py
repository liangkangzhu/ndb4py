#coding=utf-8

'''
ndb节点过滤

@author: Huiyugeng
'''

class NodeFilter:
    '''
    List过滤
    
    @param table: 需要过滤的列表
    @param query: 查询条件，支持eq(相等),like（类似），例如['name':{'type': 'eq', 'value': 'wang'}],查找table中name属性为wang的信息
    @param union: 是否采用交叉结果
    
    @return: 过滤后的List   
    '''
    def filte(self, table, query=None, union=False):
    
        if query == None:
            return table
        if table == None:
            return []
        
        _table = []
        if union == False:
            _table = self.filter_and(table, query)
        else:
            _table = self.filter_or(table, query)
                
        return _table
    
    '''
    条件间取与，query中全部条件满足，就加入列表
    '''
    def filter_and(self, table, query):
        _table = []
        for row in table:
            add_row = True
            
            for key in query:
                value = query[key]
                query_type = value.get('type')
                query_value = value.get('value')
                
                if value == None:
                    continue
                if query_value == None or query_value == '':
                    continue
                
                if row.has_key(key):
                    row_value = str(row[key]).strip()
                    if query_type == 'eq' and query_value != row_value:
                        add_row = False
                    elif query_type == 'like' and (query_value not in row_value):
                        add_row = False
                else:
                    add_row - False
                        
            if add_row == True:       
                _table.append(row)
        
        return _table
    
    '''
    条件间取或，query中任意条件满足，就加入列表
    '''
    def filter_or(self, table, query):
        _table = []
        for row in table:
            add_row = False
            
            for key in query:
                value = query[key]
                query_type = value.get('type')
                query_value = value.get('value')
                
                if value == None:
                    add_row = True
                    continue
                if query_value == None or query_value == '':
                    add_row = True
                    continue
                
                if row.has_key(key):
                    row_value = str(row[key]).strip()
                    if query_type == 'eq' and query_value == row_value:
                        add_row = True
                    elif query_type == 'like' and (query_value in row_value):
                        add_row = True
                else:
                    add_row = False
                
            if add_row == True:       
                _table.append(row)
        
        return _table
