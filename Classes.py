# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:28:20 2022

@author: Nikos
"""
import requests
import urllib.parse
import datetime
class Company(object):
    
    def __init__(self,address,phone,afm,name):
        self.name = name;
        self.address = address
        self.phone = phone
        self.afm = afm
    
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getAfm(self):
        return self.afm
    def getAddress(self):
        return self.address
    def getDirections(self):       
        address = self.address
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
        response = requests.get(url).json()
        lat = response[0]["lat"]
        lon = response[0]["lon"]
        return ("https://www.google.com/maps/a"+lat+","+lon+',15z')
    
class Campaign(object):    
    def __init__(self,customersList,deliveryTime,notificationText,notificationType):
        self.deliveryTime = deliveryTime
        self.notificationText = notificationText
        self.notificationType = notificationType
        self.customerList = customersList
        self.company = Company
        
    