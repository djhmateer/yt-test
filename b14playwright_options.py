# playwright install  
# getting chrome 127.0.

from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     # page.goto("http://playwright.dev")
#     # page.goto("https://www.youtube.com/watch?v=ScMzIvxBSi4")
#     page.goto("https://www.youtube.com/watch?v=ScMzIvxBSi4")


#     # print(page.title())
#     # page.screenshot(path="screenshot.png")
#     page.screenshot(path="screenshot.png", full_page=True)

#     browser.close()


with sync_playwright() as p:
    browser = p.chromium.launch()
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
    
    context = browser.new_context(
        # passing a different user agent
        user_agent=ua,
        
        # forcing a larger viewport to make facebook play well
        # https://playwright.dev/docs/next/emulation#viewport
        viewport={"width":1200, "height":2000}
        )

    page = context.new_page()

    # a public facebook post
    page.goto("https://www.youtube.com/watch?v=ScMzIvxBSi4")

    page.screenshot(path="screenshot.png")

    browser.close()