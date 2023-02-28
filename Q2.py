import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
plt.style.use("fivethirtyeight")


#Data Cleaning part
data = pd.read_csv('/home/saud/Downloads/my.csv')
total_data = pd.DataFrame(data)
total_data.dropna(inplace = True)
total_data.duplicated()


x_axis = 4
counter = x_axis
counter2 = 0

vari1  = total_data['Daily Oil Consumption (Barrels)']
vari2  = total_data['World Share']
vari3  = total_data['Yearly Gallons Per Capita']
vari4  = total_data['Price Per Gallon (USD)']
vari5  = total_data['Price Per Liter (USD)']
vari6  = total_data['Price Per Liter (PKR)']
vari7  = total_data['GDP Per Capita ( USD )']
vari8  = total_data['Gallons GDP Per Capita Can Buy']
vari9  = total_data['xTimes Yearly Gallons Per Capita Buy']
const =  total_data['Country']


def fun1(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('Daily Oil Consumption (Barrels)')
    plt.tight_layout()
    plt.show()

def fun2(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('World Share')
    plt.tight_layout()
    plt.show()

def fun3(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('Yearly Gallons Per Capita')
    plt.tight_layout()
    plt.show()

def fun4(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('Price Per Gallon (USD)')
    plt.tight_layout()
    plt.show()
    
def fun5(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('Price Per Liter (USD)')
    plt.tight_layout()
    plt.show()
    
def fun6(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('Price Per Liter (PKR)')
    plt.tight_layout()
    plt.show()
    
    
def fun7(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('GDP Per Capita ( USD )')
    plt.tight_layout()
    plt.show()


def fun8(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('Gallons GDP Per Capita Can Buy')
    plt.tight_layout()
    plt.show()
    

def fun9(counter,counter2):
    plt.plot(const[counter2:counter],vari1[counter2:counter], label='All Dev',color = 'red')
    plt.xlabel('Country')
    plt.ylabel('xTimes Yearly Gallons Per Capita Buy')
    plt.tight_layout()
    plt.show()
    

 


t_time = 0.5


for i in range(333):
    if i<=37:
        fun1(counter,counter2)
        counter2 = counter
        counter +=x_axis
        time.sleep(t_time)
    elif i<=72:
        if i==38:
            counter = x_axis
            counter2 =0
        fun2(counter,counter2)
        counter2 = counter
        counter = counter+x_axis
        time.sleep(t_time)
        
    elif i<=111:
        if i==73:
            counter = x_axis
            counter2 =0
        fun3(counter,counter2)
        counter2 = counter
        counter = counter+x_axis
        time.sleep(t_time)
    elif i<=148:
        if i==112:
            counter = x_axis
            counter2 =0
        fun4(counter,counter2)
        counter2 = counter
        counter = counter+x_axis
        time.sleep(t_time)
    elif i<=185:
        if i==149:
            counter = x_axis
            counter2 =0
        fun5(counter,counter2)
        counter2 = counter
        counter = counter+x_axis
        time.sleep(t_time)
    elif i<=222:
        if i==186:
            counter = x_axis
            counter2 =0
        fun6(counter,counter2)
        counter2 = counter
        counter = counter+x_axis
        time.sleep(t_time)
    elif i<=259:
        if i==223:
            counter = x_axis
            counter2 =0
        fun7(counter,counter2)
        counter2 = counter
        counter = counter+x_axis
        time.sleep(t_time)
    elif i<=296:
        if i==260:
            counter = x_axis
            counter2 =0
        fun8(counter,counter2)
        counter2 = counter
        counter = counter+x_axis
        time.sleep(t_time)
    elif i<=333:
        if i==297:
            counter = x_axis
            counter2 =0
        fun9(counter,counter2)
        counter2 = counter
        counter = counter+x_axis
        time.sleep(t_time)
        
        
        






