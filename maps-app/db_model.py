'''
Created on 07/mar/2009

@author: yanke
'''

from google.appengine.ext import db

class Vehicle(db.Model):
    name = db.StringProperty()
    

    def __init__(selfparams):
        '''
        Constructor
        '''
        