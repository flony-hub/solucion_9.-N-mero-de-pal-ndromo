# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:55:50 2024

@author: auten
"""

class Solution:
    def isPalindrome(self, x:int() ) -> bool():
        lista_de_digitos = list()
        for digito in str(x):
            lista_de_digitos.append(digito)
        if (lista_de_digitos[::1] == lista_de_digitos[::-1]):
            return True
        else: return False
        
        
objeto = Solution()
print(objeto.isPalindrome(-242))