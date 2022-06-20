# Code by @AmirMotefaker

# Youtube Comment Bot

# Step #2: Open Youtube site
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
browser.get("https://www.youtube.com")


# Step #3: Login with a username and password
def login_with_username_and_password(browser, username, password):
	
    # Type email
    email_input = browser.find_element_by_css_selector('input[type=email]')

    email = username
    for letter in email:
        email_input.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)

    # Click next
    next_button = browser.find_elements_by_css_selector("button")
    time.sleep(2)
    next_button[2].click()
    time.sleep(2)

    # Type password
    password_input = browser.find_elements_by_css_selector('input[type=password]')
    password = password
    for letter in password:
        password_input.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)
	
    # Click next
    next_button = browser.find_elements_by_css_selector("button")
    time.sleep(2)
    next_button[1].click()

    # Click Confirm
    confirm_button = browser.find_elements_by_css_selector("div[role=button]")
    time.sleep(2)
    if(len(confirm_button)>0):
        confirm_button[1].click()

        
#Step #4: Enter a search term
def enter_search_term(browser,search_term):
    # Enter text on the search term
    search_input = browser.find_element_by_id("search")
    for letter in search_term:
        search_input.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)

    search_input.send_keys(Keys.ENTER)


