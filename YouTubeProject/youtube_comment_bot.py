# Code by AmirMotefaker

# Youtube Comment Bot

# Step #2: Open Youtube site
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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


# Step #4: Enter a search term
def enter_search_term(browser,search_term):
    # Enter text on the search term
    search_input = browser.find_element_by_id("search")
    for letter in search_term:
        search_input.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)

    search_input.send_keys(Keys.ENTER)


# Step #5: Click on a video
thumbnails = browser.find_elements_by_css_selector("ytd-video-renderer")
    for index in range(1,6):
        thumbnails[index].click()


# Step #6: Enter a comment
def enter_comment(browser, comment):
    comment_input = browser.find_element_by_css_selector("ytd-comment-simplebox-renderer")

    entering_comment_actions = ActionChains(browser)

    entering_comment_actions.move_to_element(comment_input)
    entering_comment_actions.click()

    for letter in comment:
        entering_comment_actions.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        entering_comment_actions.pause(wait_time)

    entering_comment_actions.perform()

    time.sleep(1)

    send_comment_button = browser.find_element_by_id("submit-button")
    send_comment_button.click()


browser = webdriver.Chrome('./chromedriver')
browser.get("https://www.youtube.com")

# Click Agree and Sing In
click_on_agree_and_signin(browser)

# Sign In
login_with_username_and_password(browser, "your_username_here", "your_password_here")

all_search_terms =['make money online','online marketing']
for search_term in all_search_terms:
    enter_search_term(browser, search_term)
    time.sleep(2)

    thumbnails = browser.find_elements_by_css_selector("ytd-video-renderer")

    for index in range(1,6):
        thumbnails[index].click()
        time.sleep(6)

        enter_comment(browser,"your comment here")
        browser.execute_script("window.history.go(-1)")
        thumbnails = browser.find_elements_by_css_selector("ytd-video-renderer")


time.sleep(1)
browser.close()

def click_on_agree_and_signin(browser):
    agree_button= browser.find_element_by_css_selector('button')
    time.sleep(2)
    agree_button.click()

    signin_buttons= browser.find_elements_by_css_selector('yt-button-renderer')
    time.sleep(6) # Wait longer so the message pops up
    while(len(signin_buttons)== 0):
        signin_buttons= browser.find_elements_by_css_selector('yt-button-renderer')
        time.sleep(1)

    signin_buttons[1].click()
