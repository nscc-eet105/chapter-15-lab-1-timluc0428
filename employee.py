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

#DONE create a dataclass that represents and Employee 
#   the dataclass should contain:
#DONE       attributes for Employee's name, hours worked, and hourly rate. 
#DONE       dataclass should contain properties to set and get all attributes.
#DONE       the dataclass should contain a calc_pay method that calculates and returns
#DONE           the Employee's pay.
#DONE           - Employee's pay is equal to the number of hourse worked times their hourly rate.

#DONE create a subclass of Employee named Salesperson. The dataclass should contain the
#DONE   the following:
#DONE   - Attributes for the 
#DONE       - Salesperson's weekly sales and 
#DONE       - commision percentage
#DONE   - The data class should contain properties to get and set its instance variables
#   - The class should contain a calc_pay method that calculates and returns the 
#       Salesperson's pay.
#       - A Sale'sperson's pay is equal to their pay as an Employee plus amount of 
#           commision earned all sales made (commission percent * sales).

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
    
# Testing
# The main class will create two instances from your Employee class and 
#   two instances from you Salesperson class.
#   - Do not modify the code for creating the instances of those classes
#   - If something doesn't work in that section, the problem is in the classes
#       you created.

# Demonstrate Polymorphism
# In bottom section of the main program do the following:
#   Add all four instances of people to a single list(This works because of polymorphism)
#   Use a single for loop to print the data from each object and the results of the 
#       calc_pay method for each of them.
