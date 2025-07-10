# Tim Lucas
# Lab 15-1
# 2025-07-09

from dataclasses import dataclass

@dataclass
class Employee:
    __name:str
    __hours_worked:float = 0.0
    __hourly_rate:float = 0.0
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
            
    @property
    def hours_worked(self):
        return self.__hours_worked
    
    @hours_worked.setter
    def hours_worked(self, value):
        self.__hours_worked = value

    @property
    def hourly_rate(self):
        return self.__hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, value):    
        self.__hourly_rate = value

    def calc_pay(self):
        return self.hourly_rate * self.hours_worked
    

@dataclass
class Salesperson(Employee):

    __weekly_sales:float = 0.0
    __commission_percentage:float = 0.0

    @property
    def weekly_sales(self):
        return self.__weekly_sales
    
    @weekly_sales.setter
    def weekly_sales(self, value):
        self.__weekly_sales = value

    @property
    def commission_percentage(self):
        return self.__commission_percentage
    
    @commission_percentage.setter
    def commission_percentage(self, value):
        self.__commission_percentage = value    

    def calc_pay(self):
        base_pay = Employee.calc_pay(self)
        commission_pay = self.weekly_sales * self.commission_percentage
        return  base_pay + commission_pay
    

