#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

# now Firefox will run in a virtual display. 
# you will not see the browser.
browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get('http://mazii.net/#search/k/%E5%90%88')
print browser.page_source
browser.quit()

display.stop()