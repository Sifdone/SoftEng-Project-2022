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
        
        def sendCampaign():
            return 0
        def changeTime(self,time):
            self.deliveryTime = time
            
class Appointment(object):
    next_id = 0 
  
    def __init__(self,date,customerId,operationId,length):
        self.date = date
        self.customerId = Customer.id
        self.operationId = Operation.id
        self.length = length
        self.id = Appointment.next_id
        Appointment.next_id += 1
        updateAgenda()
        def changeDate(self,newdate):
            self.date = newdate
        def updateAgenda(self):
            Agenda.calenddar.append(self.date)
        def getAppointment():
            return Appointment()
class Operation(object):
    next_id = 0
    def __init__(self,cost,description,carId,delay,date):
        self.cost =cost
        self.description = description
        self.carId = Vehicle.id
        self.delay = delay
        self.date = date
        self.id =  Operation.next_id
        Operation.next_id += 1
        
        def getDelay(self):
            return self.delay
        def getCost(self):
            return self.cost
        def getDescription(self):
            return self.description
        def getType(self):
            return self.type
        def getCarDetails(self):
            if Vehicle.id == self.carId:
               return dir(Vehicle)
class State(object):
    def __init__(self,progress,estimatedTime,description,operationId):
        self.progress= progress
        self.estimatedTime = estimateTime
        self.description = description
        self.operationId = Operation.id
        
        def getProgress(self):
            return self.progress
        def getDescription(self):
            return self.description
            
class Customer(object):
    next_id = 0
    def __init__(self,name,address,phone) :
        self.name = name
        self.address = address
        self.phone = phone
        self.id = Customer.next_id
        Customer.next_id +=1
    def changeName(self,newname):
        self.name = newname
    def addCar():
        
        
class Vehicle(object):
    next_id = 0
    def __init__(self,licence_plate,model_name,kms,vid,color):
        self.licence_plate = licence_plate
        self.model_name = model_name
        self.kms = kms
        self.vid = vid
        self.color = color
        self.id = Vehicle.next_id
        Vehicle.next_id += 1
        
    def getHistory():
        
    def getCarDetails():
        
    def createQR():
        
    def getService():
        
        

class Agenda(object):
    calendar =[]
    def __init__(self,workingHours,busyHours):
        self.workingHours =workingHours
        self.busyHours = busyHours
        
    def getCalendar():
        return Appointmetn.calendar
    def updateBusyHours(self,newbusy):
        self.busyHours = newbusy
class Repair(Operation):
    def __init(self,cost,description,carId,delay,date,parts,hours)
        super().__init__(cost,description,carId,delay,date)
        self.parts = parts
        self.hours = hours
class Service(Operation):
     def __init(self,cost,description,carId,delay,date,info,hours)
         super().__init__(cost,description,carId,delay,date)
         self.info = info 
         self.hours = hours
            
        
    