# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:21:13 2021

@author: Bilgin Altundas
reference : https://www.youtube.com/watch?v=-xJvpnenx6Y
https://www.youtube.com/watch?v=3ekQpwvgTR8&list=PLPdtS77PaSutvrLxZJT5gmASGSed0dO_T&index=2
"""


class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def levelOrder(root):
    q=[]
    q.append(root)
    while len(q)!=0:
        root =q.pop(0)
        print(root.data, end=' ')
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)

def checkBST(root):
    def in_order(root,values):
        if root is None:
            return
        in_order(root.left,values)
        values.append(root.data)
        in_order(root.right,values)
        
    values = []
    in_order(root, values)
    
    for i in range(len(values)-1):
        if values[i]>=values[i+1]:
            return False
    return True
      
class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data<node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    
    def traverse_inorder(self,root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)
            
    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
   
tree = Tree()
root = tree.createNode(5)

print(root.data)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

print('---In traverse order---:')
tree.traverse_inorder(root)

print('==height====')
print(f'height of the tree is {tree.height(root)}')

print('==Level Order')
print(f'{levelOrder(root)}')

BST = checkBST(root)

print(f'The tree is a BST:{BST}')