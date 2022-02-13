# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 09:14:51 2022

@author: 20192024
"""
class Vector:
        def __init__(self, *elements):
                self.elements = elements
                
        def __repr__(self):
                s = '['
                for x in self.elements:
                        s += str(x) + ', '
                s += ']'
                return s
            
        def __len__(self):
            return len(self.elements)
        

        def __add__(self, other):
               assert len(self) == len(other)
               sums = []
               for a, b in zip(self.elements, other.elements):
                       sums.append(a + b)
               return Vector(*sums)
           
        def __abs__(self):
                  return Vector(*[abs(x) for x in self.elements])

