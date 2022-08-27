# Code by AmirMotefaker

# Extract Title,Views,Channel Name,Subscribers & Comments & Save in CSV & HTML Table Using Pandas Library

"""
Main script to scrape the comments of any Youtube video.
 
Example:
    $ python main.py YOUTUBE_VIDEO_URL
"""
 
import csv
import io
from grpc import Channel
from selenium import webdriver
from selenium.common import exceptions
import sys
import time
import pandas as pd
 
 
def scrape(url):
    """
    Extracts the comments from the Youtube video given by the URL.
 
    Args:
        url (str): The URL to the Youtube video
 
    Raises:
        selenium.common.exceptions.NoSuchElementException:
        When certain elements to look for cannot be found
    """
 
    # Note: Download and replace argument with path to the driver executable.
    # Simply download the executable and move it into the webdrivers folder.
    driver = webdriver.Chrome('chromedriver')
 
    # Navigates to the URL, maximizes the current window, and
    # then suspends execution for (at least) 5 seconds (this
    # gives time for the page to load).
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
 
    try:
        # Extract the elements storing the video title and
        # comment section.
        title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
        comment_section = driver.find_element_by_xpath('//*[@id="comments"]')
        views = driver.find_element_by_xpath('//*[@id = "count"]/ytd-video-view-count-renderer/span[1]').text
        date = driver.find_element_by_xpath('//*[@id="info-strings"]/yt-formatted-string').text
        channel = driver.find_element_by_xpath('//*[@id="text"]/a').text
        subscribers = driver.find_element_by_xpath('//*[@id="owner-sub-count"]').text
        description = driver.find_element_by_xpath('//*[@id="description"]/yt-formatted-string').text
    except exceptions.NoSuchElementException:
        # Note: Youtube may have changed their HTML layouts for
        # videos, so raise an error for sanity sake in case the
        # elements provided cannot be found anymore.
        error = "Error: Double check selector OR "
        error += "element may not yet be on the screen at the time of the find operation"
        print(error)
 
    # Scroll into view the comment section, then allow some time
    # for everything to be loaded as necessary.
    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
    time.sleep(7)
 
    # Scroll all the way down to the bottom in order to get all the
    # elements loaded (since Youtube dynamically loads them).
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
 
    while True:
        # Scroll down 'til "next load".
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
 
        # Wait to load everything thus far.
        time.sleep(2)
 
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
 
    # One last scroll just in case.
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
 
    try:
        # Extract the elements storing the usernames and comments.
        username_elems = driver.find_elements_by_xpath('//*[@id="author-text"]')
        comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
    except exceptions.NoSuchElementException:
        error = "Error: Double check selector OR "
        error += "element may not yet be on the screen at the time of the find operation"
        print(error)
 
    print("> VIDEO TITLE: " + title + "\n")
    print("> VIEWS of Video: " + views + "\n")
    print("> Date: " + date + "\n")
    print(">Channel Name: " + channel + "\n")
    print(">Subscribers: " + subscribers + "\n")
    print(">Description: " + description + "\n")
 
    
    with io.open('basicinfo.csv','w',newline='',encoding="utf-16") as file:
        writer = csv.writer(file,delimiter=",",quoting=csv.QUOTE_ALL)
        writer.writerow(["Title","Views","Date","Channelname","subs","des"])
        writer.writerow([title,views,date,channel,subscribers,description])
        
 
    # to read csv file named "samplee"
    a = pd.read_csv("basicinfo.csv",encoding="utf-16")
 
# to save as html file
# named as "Table"
    a.to_html("basicinfo.htm")
 
    with io.open('comments.csv', 'w', newline='', encoding="utf-16") as file:
        writer = csv.writer(file, delimiter =",", quoting=csv.QUOTE_ALL)
        writer.writerow(["Username", "Comment"])
        for username, comment in zip(username_elems, comment_elems):
            writer.writerow([username.text, comment.text])
            
     # to read csv file named "sample"
    a = pd.read_csv("comments.csv",encoding="utf-16")
 
# to save as html file
# named as "Table"
    a.to_html("comments.htm")
            
 
    driver.close()
 
if __name__ == "__main__":
    scrape(sys.argv[1])
