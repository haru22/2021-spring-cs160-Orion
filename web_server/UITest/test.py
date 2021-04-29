from selenium import webdriver
import pytest
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "./myenv/chromedriver"
driver = webdriver.Chrome(PATH)

# def test_register_less_6_characters():

#     driver = webdriver.Chrome(PATH)
#     driver.get('http://127.0.0.1:3000/register')

#     driver.find_element_by_name("firstName").send_keys("testFirstName")
#     driver.find_element_by_name("lastName").send_keys("testLastName")
#     driver.find_element_by_name("email").send_keys("test7@g.com")
#     driver.find_element_by_name("password").send_keys("12345")
#     driver.find_element_by_name("passwordConfirm").send_keys("12345")
#     register_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     register_button.click()
#     error_message = driver.find_element_by_xpath("//*[@id='login-card']/div")
#     assert error_message.text == "Password should be atleast 6 characters"
    
#     time.sleep(2)
#     driver.quit()

# def test_register_same_email():
    
#     driver.get('http://127.0.0.1:3000/register')

#     # register page test
#     driver.find_element_by_name("firstName").send_keys("testFirstName")
#     driver.find_element_by_name("lastName").send_keys("testLastName")
#     driver.find_element_by_name("email").send_keys("test5@g.com")
#     driver.find_element_by_name("password").send_keys("123456")
#     driver.find_element_by_name("passwordConfirm").send_keys("123456")
#     register_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     register_button.click()
#     error_message = driver.find_element_by_xpath("//*[@id='login-card']/div")
#     assert error_message.text == "Email is already registered"
    
#     time.sleep(2)
#     driver.quit()

# def test_rediret_to_login():
     
#     driver.get('http://127.0.0.1:3000/register')

#     # register page test
#     driver.find_element_by_name("firstName").send_keys("testFirstName")
#     driver.find_element_by_name("lastName").send_keys("testLastName")
#     driver.find_element_by_name("email").send_keys("test11@g.com")
#     driver.find_element_by_name("password").send_keys("123456")
#     driver.find_element_by_name("passwordConfirm").send_keys("123456")
#     register_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     register_button.click()

#     # login page test
#     driver.find_element_by_name("email").send_keys("test6@g.com")
#     driver.find_element_by_name("password").send_keys("123456")
#     # login_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     time.sleep(2)
#     assert driver.current_url == "http://127.0.0.1:3000/login"

#     time.sleep(2)
#     driver.quit()

# def test_rediret_to_home():
#     driver.get('http://127.0.0.1:3000/login')
#     driver.find_element_by_name("email").send_keys("test6@g.com")
#     driver.find_element_by_name("password").send_keys("123456")
#     login_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     login_button.click()
#     time.sleep(5)
#     assert driver.current_url == "http://127.0.0.1:3000/home"
#     time.sleep(2)
#     driver.quit()

# def test_register_missing_firstName():
#     driver.get('http://127.0.0.1:3000/register')

#     driver.find_element_by_name("lastName").send_keys("testLastName")
#     driver.find_element_by_name("email").send_keys("test100@g.com")
#     driver.find_element_by_name("password").send_keys("123456")
#     driver.find_element_by_name("passwordConfirm").send_keys("123456")
#     register_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     register_button.click()
#     error_message = driver.find_element_by_xpath("//*[@id='login-card']/div")
#     assert error_message.text == "Please fill in all fields"
    
#     time.sleep(2)
#     driver.quit()

# def test_register_missing_lastName():
#     driver.get('http://127.0.0.1:3000/register')

#     driver.find_element_by_name("firstName").send_keys("testFirstName")
#     driver.find_element_by_name("email").send_keys("test100@g.com")
#     driver.find_element_by_name("password").send_keys("123456")
#     driver.find_element_by_name("passwordConfirm").send_keys("123456")
#     register_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     register_button.click()
#     error_message = driver.find_element_by_xpath("//*[@id='login-card']/div")
#     assert error_message.text == "Please fill in all fields"
    
#     time.sleep(2)
#     driver.quit()

# def test_register_missing_email():
#     driver.get('http://127.0.0.1:3000/register')

#     driver.find_element_by_name("firstName").send_keys("testFirstName")
#     driver.find_element_by_name("lastName").send_keys("testLastName")
#     driver.find_element_by_name("password").send_keys("123456")
#     driver.find_element_by_name("passwordConfirm").send_keys("123456")
#     register_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     register_button.click()
#     error_message = driver.find_element_by_xpath("//*[@id='login-card']/div")
#     assert error_message.text == "Please fill in all fields"
    
#     time.sleep(2)
#     driver.quit()

# def test_register_missing_pw():
#     driver.get('http://127.0.0.1:3000/register')

#     driver.find_element_by_name("firstName").send_keys("testFirstName")
#     driver.find_element_by_name("lastName").send_keys("testLastName")
#     driver.find_element_by_name("email").send_keys("test100@g.com")
#     driver.find_element_by_name("passwordConfirm").send_keys("123456")
#     register_button = driver.find_element_by_xpath("//*[@id='btn-override']")
#     register_button.click()
#     error_message = driver.find_element_by_xpath("//*[@id='login-card']/div")
#     assert error_message.text == "Please fill in all fields"
    
#     time.sleep(2)
#     driver.quit()

# def test_google_auth():
#     driver.get('http://127.0.0.1:3000/login')
#     google_login = driver.find_element_by_link_text("Sign in with Google")
#     google_login.click()
#     driver.find_element_by_name("identifier").send_keys("haruna.yamakawa@sjsu.edu")
#     driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()


# def test_facebook_auth():
#     driver.get('http://127.0.0.1:3000/login')

#     facebook_login = driver.find_element_by_link_text("Sign in with Facebook")
#     facebook_login.click()

#     driver.find_element_by_name("email").send_keys("y.a.m.aa@docomo.ne.jp")
#     driver.find_element_by_name("pass").send_keys("08670867")
#     driver.find_element_by_name("login").click()

#     time.sleep(5)
#     assert driver.current_url == "http://localhost:3000/home#_=_"
    # driver.quit()

def test_logout():
    driver.get('http://127.0.0.1:3000/login')
    driver.find_element_by_name("email").send_keys("test6@g.com")
    driver.find_element_by_name("password").send_keys("123456")
    login_button = driver.find_element_by_xpath("//*[@id='btn-override']")
    login_button.click()
    time.sleep(2)
    logout_button = driver.find_element_by_link_text("Logout")
    logout_button.click()
    time.sleep(2)
    assert driver.current_url == "http://127.0.0.1:3000/login"
    driver.quit()


# time.sleep(4)
# # logout
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
#     )
    
#     element.click()

# except:
#     driver.quit()


# # google auth test
# time.sleep(4)
# google_login = driver.find_element_by_link_text("Sign in with Google")
# google_login.click()
# driver.find_element_by_name("identifier").send_keys("haruna.yamakawa@sjsu.edu")
# driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()



# # try:
# #     element = WebDriverWait(driver, 3).until(
# #         EC.presence_of_element_located((By.LINK_TEXT, "Next"))
# #     )
# #     element.click()

# #     # click logout button
# #     element = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
# #     )
# #     element.click()


# # except:
#     # driver.quit()

# time.sleep(2)
# driver.quit()

