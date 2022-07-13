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
            
            
            def skip_buttons(): Some options will be present asking to ‘save The Password’ and to ‘Turn On Notifications’. We deal with those options here by selecting                  ‘Not Now’ for them all. Thus declare the function skip_buttons.
            
            browser.find_element_by_xpath(“//div[@class=’cmbtv’]/button[@type=’button’]”).click(): When the screen goes to the second page, you select the option ‘Not                  now’ by giving this command. @class denotes the name of the class and @type denotes the type of the button or any HTML tag.
                 The same concept is extended to the Notifications option in the third page.
                 
                 
            def navigate_to_sender(): To find the chat option and the text area for that chat, we declare this function.
         
            browser.find_element_by_css_selector().click(): It is the same as finding by Xpath, only that it uses a CSS path.
            
            browser.find_elements_by_xpath: This function is similar to find element with the difference being the data it returns. This function returns a list of all                  elements containing the same tag. Here we use it to return a list of all the conversations with other users.
            
            length = len(elements): To determine the conversations between the user and their friends.
            
            for i in range(length): Since all the usernames are found in the div tag starting from 1 upto to total number of elements.
            
            find_user =…….div[{}]: Insertion of the div component using format operator.
            
            f find_user.text == username: Since we chat with many people at different times, what remains as the first chat may not always be the first chat. Hence we                  compare if the text present in the div tag is the same as the username provided by the user.
            
            
            def send_jokes(time_between_jokes): To send the jokes to the user, we use this function with the parameter being the time delay between messages (jokes).
            
            message_entry: Locate the text area using find_element_by_css_selector. There are many alternate ways to locate a tag, details of which are given in the                    documentation.
            
            while True: Setting the loop to infinity causes it to send the message without a break. If you wish to terminate the process, you can raise a keyboard                      interrupt in the terminal.
            
            joke = jokes(): Calling jokes() function to obtain a joke.
            
            message_entry.send_keys(): Similar to username and password input, where send_keys places the required details in the text area. Time.ctime gives the                        current date, day and time with seconds. This part is optional.
            
            for i in range(length): Since all the usernames are found in the div tag starting from 1 upto to total number of elements.
            
            find_user =…….div[{}]: Insertion of the div component using format operator.
            
            if find_user.text == username: Since we chat with many people at different times, what remains as the first chat may not always be the first chat. Hence we                  compare if the text present in the div tag is the same as the username provided by the user.
            
            browser.find_element_by_xpath(): Find the send button and send the message by giving the option click()
            
            time.sleep(time_between_jokes): Waits until the time expires by pausing the process i.e., sleeping and then repeating execution since it is in a loop.
            
            

            
            
            


