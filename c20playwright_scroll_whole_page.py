from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the YouTube video
    page.goto('https://www.youtube.com/watch?v=LkPDz_MHIEY')

    #dm added this
    page.wait_for_selector('button[aria-label="Reject the use of cookies and other data for the purposes described"]')
    page.click('button[aria-label="Reject the use of cookies and other data for the purposes described"]')

    # Scroll to the bottom of the page to load all content
    auto_scroll(page)

    page.wait_for_timeout(5000)  # Wait for 5 seconds

    scroll_with_mouse_wheel(page)

    # auto_scroll(page)
    # page.wait_for_timeout(5000)  # Wait for 5 seconds
    
    scroll_with_mouse_wheel(page)
    scroll_with_mouse_wheel(page)
    scroll_with_mouse_wheel(page)
    scroll_with_mouse_wheel(page)
    scroll_with_mouse_wheel(page)

    page.wait_for_timeout(1000)  # Wait for 5 seconds

    # Take a full page screenshot
    page.screenshot(path='youtube_video_full_page.png', full_page=True)

    # Close the browser
    browser.close()

def scroll_with_mouse_wheel(page):
    # Scroll down the page to force loading more comments
    previous_height = page.evaluate("document.body.scrollHeight")
    while True:
        # Scroll down using the mouse wheel
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(1000)  # Wait for comments to load
        
        # Check the new scroll height
        new_height = page.evaluate("document.body.scrollHeight")
        
        if new_height == previous_height:
            break  # Exit loop if no new content is loaded
        
        previous_height = new_height

def auto_scroll(page):
    page.evaluate("""
            () => {
            return new Promise((resolve, reject) => {
                let totalHeight = 0;
                const distance = 100;
                const delay = 100;
                const scrollInterval = setInterval(() => {
                    const { scrollHeight } = document.body;
                    window.scrollBy(0, distance);
                    totalHeight += distance;

                    if (totalHeight >= scrollHeight) {
                        clearInterval(scrollInterval);
                        resolve();
                    }
                }, delay);

                // Extra check to ensure we've really hit the bottom
                setTimeout(() => {
                    const checkScrollEnd = () => {
                        if (document.body.scrollHeight === totalHeight) {
                            clearInterval(scrollInterval);
                            resolve();
                        } else {
                            totalHeight = document.body.scrollHeight;
                        }
                    };
                    setInterval(checkScrollEnd, delay);
                }, delay);
            });
        }
    """)

def main():
    with sync_playwright() as playwright:
        run(playwright)

# Run the script
if __name__ == "__main__":
    main()
