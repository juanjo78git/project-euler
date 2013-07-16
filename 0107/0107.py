# -*- coding: utf-8 -*-

#!/usr/bin/python

# primero una clase que sea una DisjointSet

class DisjoinSet(object):
    
    def makeset(self, x):
        self.parent = x
        self.rank = 0

    def find(self, x):
        if self.parent != x:
            self.parent = self.find(self.parent)
        else:
            return self.find(self.x)
 
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if xroot.rank < yroot.rank:
            xroot.parent = yroot
        elif xroot.rank > yroot.rank:
            yroot.parent = xroot
        else:
            yroot.parent = xroot
            xroot.rank += 1


#http://programmingpraxis.com/2010/04/06/minimum-spanning-tree-kruskals-algorithm/
#http://programmingpraxis.com/2010/04/02/disjoint-sets/
class DisjointSet(dict):
    def add(self, item):
        self[item] = item
 
    def find(self, item):
        parent = self[item]
 
        while self[parent] != parent:
            parent = self[parent]
 
        self[item] = parent
        return parent
 
    def union(self, item1, item2):
        self[item2] = self[item1]
