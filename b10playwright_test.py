# playwright install  
# getting chrome 127.0.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    # page.goto("http://playwright.dev")
    # page.goto("https://www.youtube.com/watch?v=ScMzIvxBSi4")
    page.goto("https://www.youtube.com/watch?v=ScMzIvxBSi4")


    # print(page.title())
    # page.screenshot(path="screenshot.png")
    page.screenshot(path="screenshot.png", full_page=True)
    browser.close()