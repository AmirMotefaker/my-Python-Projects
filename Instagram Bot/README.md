# Instagram Bot

>> Step by Step:

##   1. Importing libraries:

            from selenium import webdriver: Selenium is a package we will use to control the web browser and automate sending the messages. To use a browser, we import                   webdriver from selenium. For further reading: selenium docs.
            
            import time: To display the time the automated message was sent, we use Time library. Since this step is optional, it can be removed if not needed.
            
            import random: To obtain a random joke, we need a random integer indicating a joke. Thus we can achieve the functions of random using this library.
            
            import requests: To extract the jokes from the website, we need the requests library to retrieve data from the website.
            
            from bs4 import BeautifulSoup: To scrape the data from the obtained website, we make use of this library. For further reading: beautiful soup docs.
            
            
            
##   2. Declaring the necessary functions to automate Instagram messages using Python:

            def jokes(): Declaration of the function for jokes
            
            result = requests.get(‘https://bestlifeonline.com/one-liner-jokes/’): Connect to the website for jokes and check the status code. If the status code is 200                  or similar, then we can parse through the HTML outline of the webpage. Find another webpage if status code is 403 which means forbidden.
            
            soup = BeautifulSoup(result.content, ‘html.parser’): To scrape data, we must be able to parse through the HTML outline of the webpage. We do that using                      beautiful soup. The first parameter is the content of the web page which contains html tags as well as textual information displayed to the user and                    the second parameter indicates the type of parsing that has to be done.
            
            joke_number: Select a random integer within a given range (starting and ending value included) using the function randint.
            
            joke = soup.ol.find_all(“li”) [joke_number]: Extract the list item-li under ordered list tag-ol, using find_all. This obtain the needed joke by indexing                    it.
            
            eturn joke.text: The joke obtained will contain tags as well. Thus we return only the textual part by giving joke.text
            
            
            def login_to_instagram(): Declaration of the function for logging in to instagram.
            
            Username=browser.find_element_by_name(“username”): This is the name of the input box for username input. Obtain the element containing the given name to                    send the username.
            
            Username.send_keys(“put_username_here”): Now that we have the input text area for the username, we can send the username using send_keys.
                 The same holds for password field
                 
            browser.find_element_by_xpath(“//button[@type=’submit’]”).click(): To submit the credentials and login to instagram, we find the login button. Xpath is the                  path starting from the HTML tag upto the element. // is similar to relative path. Thus we find the button that has the type submit and click on it to                  login.
            
            

            
            
            


