import unittest

class Node(object):

    def __init__(self,item):
        self.item = item
        self.nextnode = None

def cyle_check(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 =  marker2.nextnode.nextnode

        if marker2 == marker1:
            print('True')
    print('False')

a = Node(1)
b = Node(2)
c = Node(3)




