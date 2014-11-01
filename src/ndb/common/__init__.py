'''
Created on 2014-5-8

@author: Huiyugeng
'''

import node_reader
import node_writer

def read(filename):
    return node_reader.NodeReader().read(filename)

def write_node(filename, name, node):
    node_writer.NodeWriter().write_node(filename, name, node)

def print_node(name, node):
    return node_writer.NodeWriter().print_node(name, node)
