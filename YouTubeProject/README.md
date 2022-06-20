**How To Build a YouTube Comment Bot**

**Table of Contents:**

    Step #0: Overview

    Step #1: Install Selenium

    Step #2: Open Youtube site

    Step #3: Login with a username and password

    Step #4: Enter a search term

    Step #5: Click on a video

    Step #6: Enter a comment

    Step #7: Go back

    Step #8: Put it all together

Step #0: Overview

**Important: When running a selenium bot against a site like Youtube, it’s important to simulate human behavior to avoid being detected and banned. Therefore, adding pauses when typing or clicking is crucial to replicating what a user would do.**


Step #1: Install Selenium

You can install selenium executing the following command from your terminal:

            pip install selenium
            
To use selenium you also need a driver, which is basically a browser. You could just use your already installed browser or download a driver. I would recommend downloading a driver to avoid messing up your browser settings. You can download a driver following the link below:

Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads

Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox: https://github.com/mozilla/geckodriver/releases

Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/

