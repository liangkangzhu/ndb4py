#coding=utf-8

import statement
import common
import operate

def read(filename):
    return common.read(filename)

def write_node(filename, name, node):
    common.write_node(filename, name, node)

def print_node(name, node):
    return common.print_node(name, node)

def execute(node, query, action = None):
    return statement.Statement().execute(node, query, action)

def select(node, path, action=None):
    return operate.select(node, path, action)

def locate(node, query, multi):
    return operate.locate(node, query, multi)

def filter_list(table, query=None, union=False):
    return operate.filte(table, query, union)