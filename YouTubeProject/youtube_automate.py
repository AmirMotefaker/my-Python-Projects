# Code by AmirMotefaker

# Automate Youtube

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
import time
 
 
def automateYoutube(searchtext):
   
    # giving the path of chromedriver to selenium webdriver
    path = "chromedriver"
 
    url = "https://www.youtube.com/"
     
    # opening the youtube in chromedriver
    driver = webdriver.Chrome(path)
    driver.get(url)
 
    # find the search bar using selenium find_element function
    driver.find_element_by_name("search_query").send_keys(searchtext)
 
    # clicking on the search button
    driver.find_element_by_css_selector(
        "#search-icon-legacy.ytd-searchbox").click()
 
    # For finding the right match search
    WebDriverWait(driver, 0).until(expected_conditions.title_contains(MyText))
 
    # clicking on the match search having same as in searched query
    WebDriverWait(driver, 30).until(
        expected_conditions.element_to_be_clickable((By.ID, "img"))).click()
 
    # while(True):
    #     pass
 
 
speak = sr.Recognizer()
try:
    with sr.Microphone() as speaky:
       
        # adjust the energy threshold based on
        # the surrounding noise level
        speak.adjust_for_ambient_noise(speaky, duration=0.2)
        print("listening...")
         
        # listens for the user's input
        searchquery = speak.listen(speaky)
         
        # Using google to recognize audio
        MyText = speak.recognize_google(searchquery)
        MyText = MyText.lower()
 
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
 
except sr.UnknownValueError:
    print("unknown error occurred")
 
# Calling the function
automateYoutube(MyText)
