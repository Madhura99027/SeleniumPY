
#Selenium and python 
from selenium import webdriver
 
import getpass
import requests

import xlsxwriter
import pprint
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#Initialize variable to store username/email and password

userid = str(input("Enter email address or number with country code: "))
password = getpass.getpass('Enter your password:')


#opening chrome
driver=webdriver.Chrome(r" PATH TO CHROME DRIVER ")


driver.maximize_window()  #to maximize the chrome window


#open the required link from chrome
driver.get(r" URL ")  #r to overcome unicode error


#XPaths allow the script to determine the exact web element you want.
#double forward slash (//) means find an element anywhere on the page.
#The star (*) means find any element. The @ sign specifies the attribute you want.
driver.find_element_by_xpath("""   """).send_keys(userid)
driver.find_element_by_xpath("""   """).send_keys(password)

#to click login button
driver.find_element_by_xpath("""//*[@id="login-submit"]""").click()



workbook=xlsxwriter.Workbook('output.xlsx')  # creates a xlsx sheet with name mentioned
worksheet = workbook.add_worksheet() 
worksheet.write('A1', 'Sr no') 		#name for cloumn 1
worksheet.write('B1', 'Regno')    #name for cloumn 2
worksheet.write('C1', 'Name')     #name for cloumn 3


#we are closing the browser.
driver.close()  
workbook.close() 