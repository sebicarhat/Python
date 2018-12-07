'''
Created on Nov 23, 2017

@author: Sebi
'''
import unittest
from Validator import *
from builtins import False

class TestValidator(unittest.TestCase):


    def test_validateNr(self):
        v=Validator()
        try:
            v.validatePhoneNr(123)
            assert False
        except MyExeption:
            pass
        
        try:
            v.validatePhoneNr("+40123")
            assert False
        except MyExeption:
            pass
        
        try:
            v.validatePhoneNr("0774971333777")
            assert False
        except MyExeption:
            pass
        
        try:
            v.validatePhoneNr("+abcdefghijklm")
            assert False
        except MyExeption:
            pass
        
    def test_ValidateContact(self):
        c=Contact("a","ab")
        v=Validator()
        try:
            v.validateContact(3.12)
        except MyExeption:
            pass
        
        try:
            v.validateContact(c)
            assert False
        except MyExeption:
            pass
        
        c.setNr("+40771112911")
        try:
            v.validateContact(c)
            assert False
        except MyExeption:
            pass
        
        c.setName(123)
        try:
            v.validateContact(c)
            assert False
        except MyExeption:
            pass
        
        c.setName("aaa")
        try:
            v.validateContact(c)
            assert False
        except MyExeption:
            pass
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()