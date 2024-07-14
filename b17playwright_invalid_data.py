# playwright install  
# getting chrome 127.0.

# from playwright.sync_api import sync_playwright

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


from playwright.sync_api import sync_playwright
from pathlib import Path

with sync_playwright() as p:
    # username = Path('secrets/proxy-username.txt').read_text()
    # password = Path('secrets/proxy-password.txt').read_text()
    browser = p.chromium.launch(    
                # Playwright runs in headless mode by default
                # some sites eg Facebook, may not like this
                # https://playwright.dev/docs/next/debug#headed-mode
                # we need to run using a virtual xserver
                headless=False,
                # Lets use a proxy to appear as if we're coming from a different IP address
                # each time
                # proxy={
                #     "server": 'http://zproxy.lum-superproxy.io:22225',
                #     "username": username,
                #     "password": password
                # },

                # Start the headed browser window Maximised so that we can get a 1200x2000 viewport
                args=['--start-maximized']
            )

    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
    
    context = browser.new_context(
        user_agent=ua,
        viewport={"width":1200, "height":2000}
        )

    page = context.new_page()

    # a public facebook post
    # url = "https://www.facebook.com/djhmateer/posts/pfbid0WK2FACHyfyBi1Lg9intnH3SmLHNRYDTfzmGZgjFqSoQAnitAz8ZVdRF1nqmx9JX1l"

    # shows user agent and IP address
    # url = "http://whatsmyuseragent.org/"

    # placeholder 
    # url = "https://www.youtube.com/watch?v=ScMzIvxBSi4"

    url = "https://www.youtube.com/watch?v=LkPDz_MHIEY"
    page.goto(url)

        # Wait for the consent popup and click the "Accept all" button
    # page.wait_for_selector('ytd-button-renderer.style-scope.ytd-consent-bump-v2-lightbox')
    # page.click('ytd-button-renderer.style-scope.ytd-consent-bump-v2-lightbox')


    page.wait_for_selector('button[aria-label="Reject the use of cookies and other data for the purposes described"]')
    page.click('button[aria-label="Reject the use of cookies and other data for the purposes described"]')


        # Wait for the video player to load
    # page.wait_for_selector('video')

    # Optionally, you can play the video to make sure it loads
    # page.click('button[aria-label="Play"]')

    # Wait for a few seconds to let the video load and play
    page.wait_for_timeout(5000)  # Wait for 5 seconds

    page.screenshot(path="screenshot.png")

    browser.close()