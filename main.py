from selenium import webdriver
import os
geko_path =("geckodriver.exe")
def start_bot(username,password):
  browser = webdriver.Firefox(geko_path)
  browser.get('https://www.google.com')
  print(browser.title)
  browser.find_element_by_name('id/class/username').send_keys(username)
  browser.find_element_by_name('id/class/password').send_keys(password)
  browser.find_element_by_name('id/class/login').click()
username = input("Enter the username:") 
password = input("Enter the password:")

start_bot(username,password)