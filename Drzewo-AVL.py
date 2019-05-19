import random
import sys
import time
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.balance = 0

class AVLTree:
    def __init__(self):
        self.root = Node(None,None)
    def add_element(self,value):
            self.add_element_helper(value, self.root)

    def add_element_helper(self, value, node):
        if node.value == None:
            node.value = value
        elif node.value < value:
            if node.right is not None:
                self.add_element_helper(value, node.right)
            else:
                node.right = Node(value, node)
                self.balance(node, 1)
        else:
            if node.left is not None:
                self.add_element_helper(value, node.left)
            else:
                node.left = Node(value, node)
                self.balance(node, -1)

    def delete_element(self,value):
            self.delete_element_helper(value, self.root)

    def delete_element_helper(self,value , node):
        if node.value < value:
            self.delete_element_helper(value,node.right)
        elif node.value > value:
            self.delete_element_helper(value,node.left)
        else:
            if node.parent is None:
                if node.right is None and node.left is None:
                    avl.root.value = None
                elif node.right is None and node.left is not None:
                    avl.root.value = node.left.value
                    node.left.parent = None
                    avl.root.left = None
                elif node.right is not None and node.left is None:
                    avl.root.value = node.right.value
                    node.right.parent = None
                    avl.root.right = None
            elif node.left is None and node.right is None:
                x = node.parent
                if x.right == node:
                    x.right = None
                    self.balance_delete(x, -1)
                    node.parent = None
                else:
                    x.left = None
                    self.balance_delete(x, 1)
                    node.parent = None
            elif node.left is None and node.right is not None:
                x = node.parent
                if x.right == node:
                    x.right = node.right
                    node.right.parent = x
                    node.parent = None
                    node.right = None
                    self.balance_delete(x, -1)
                else:
                    x.left = node.right
                    node.right.parent = x
                    node.parent = None
                    node.right = None
                    self.balance_delete(x, 1)
            elif node.left is not None and node.right is None:
                x = node.parent
                if x.right == node:
                    x.right = node.left
                    node.left.parent = x
                    node.parent = None
                    node.left = None
                    self.balance_delete(x, -1)
                else:
                    x.left = node.left
                    node.left.parent = x
                    node.parent = None
                    node.left = None
                    self.balance_delete(x, 1)
            else:
                x = node.parent
                if x.right == node:
                    node.value = self.find_the_smallest(node.right)
                    self.balance_delete(x, -1)
                else:
                    y=self.find_the_smallest(node.right)
                    node.value = y
                    self.balance_delete(x, 1)

    def find_the_smallest(self,node):
        while node.left:
            node=node.left
        x=node.value
        self.delete_element(x)
        return x

    def balance(self, node, direction):
        node.balance += direction
        if node.balance < -1:
            if node.left.balance < 0:
                self.rotateLL(node)
            else:
                self.rotateRR(node.left)
                self.rotateLL(node)
        if node.balance > 1:
            if node.right.balance > 0:
                self.rotateRR(node)
            else:
                self.rotateLL(node.right)
                self.rotateRR(node)

        if node.balance == 0 or node.parent is None:
            return
        else:
            if node.parent.right is node:
                self.balance(node.parent,1)
            else:
                self.balance(node.parent,-1)

    def balance_delete(self, node, direction):
        x = False
        if node.balance == 0 or node.parent == None:
            x = True
        node.balance += direction
        if node.balance < -1:
            if node.left.balance < 0:
                self.rotateLL(node)
            else:
                self.rotateRR(node.right)
                self.rotateLL(node)
        if node.balance > 1:
            if node.right.balance > 0:
                self.rotateRR(node)
            else:
                self.rotateLL(node.right)
                self.rotateRR(node)
        else:
            if x:
                return
            if node.parent.right is node:
                self.balance_delete(node.parent,-1)
            else:
                self.balance_delete(node.parent,1)

    def rotateRR(self,node):
        a = node
        a.balance = 0
        b = node.right
        b.balance = 0
        x = node.parent
        b.parent = a.parent
        a.parent = b
        if x is None:
            self.root = b
        elif x.left == a:
            x.left = b
        else:
            x.right = b
        if b.left is not None:
            c = b.left
            a.right = c
            c.parent=a
        else:
            a.right = None
        node = b
        node.left = a

    def rotateLL(self,node):
        a = node
        a.balance = 0
        b = node.left
        b.balance = 0
        x = node.parent
        b.parent = a.parent
        a.parent = b
        if x is None:
            self.root = b
        elif x.left == a:
            x.left = b
        else:
            x.right = b
        if b.right is not None:
            c = b.right
            a.left = c
            c.parent = a
        else:
            a.left = None
        node = b
        node.right = a

    def generate_tree(self,values):
        for i in values:
            self.add_element(i)

    def in_order(self):
        self.in_order_helper(self.root)

    def in_order_helper(self,node):
        if node.left is not None:
            self.in_order_helper(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_helper(node.right)

    def pre_order(self):
        self.pre_order_helper(self.root)

    def pre_order_helper(self, node):
        print(node.value)
        if node.left is not None:
            self.pre_order_helper(node.left)
        if node.right is not None:
            self.pre_order_helper(node.right)

    def delete_post_order(self):
        self.delete_post_order_helper(self.root)

    def delete_post_order_helper(self,node):
        if node.left is not None:
            self.delete_post_order_helper(node.left)
        if node.right is not None:
            self.delete_post_order_helper(node.right)
        self.delete_element(node.value)

    def find_element(self,value):
        node=self.root
        tab=[]
        while node.value != value:
            tab.append(node.value)
            if node.value < value:
                node=node.right
            else:
                node=node.left
        tab.append(node.value)
        return tab
#for j in range(1000):
tab = []
for i in range(1,20):
     tab.append(i)
random.shuffle(tab)
#tab = [2, 6, 1, 3, 4, 8]
#tab=[3,2,4,5,6]
#tab = [10,6,11,5,7,8]
#tab = [139, 101, 6, 119, 33, 189, 185, 133, 23, 191, 41, 59, 92, 152, 113, 77, 81, 188, 98, 89, 84, 115, 116, 179, 154, 47, 50, 145, 22, 132, 13, 21, 82, 121, 160, 37, 164, 18, 95, 181, 131, 118, 109]
print(tab)
t1=time.time()
avl = AVLTree()
avl.generate_tree(tab)
print(avl.find_element(5))
print(avl.find_element(6))
#avl.delete_post_order()
print(time.time()-t1)