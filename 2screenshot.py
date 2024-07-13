from selenium import webdriver
from PIL import Image
import time

# sudo apt update
# sudo apt install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 libxss1 libappindicator1 libindicator7


def capture_youtube_screenshot(url, output_path):
    # Initialize the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--window-size=1920,1080")  # Set initial window size
    driver = webdriver.Chrome(options=options)

    try:
        # Open the YouTube page
        driver.get(url)

        # Scroll down to load all elements
        scroll_pause_time = 2
        screen_height = driver.execute_script("return window.innerHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == screen_height:
                break
            screen_height = new_height

        # Capture the screenshot of the entire page
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, total_height)
        screenshot = driver.get_screenshot_as_png()

        # Save the screenshot to a file
        with open(output_path, 'wb') as f:
            f.write(screenshot)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Replace this with the URL of the YouTube page you want to capture
    # youtube_url = 'https://www.youtube.com/watch?v=your_video_id'
    # youtube_url = 'https://www.youtube.com/watch?v=zU9y354XAgM'

    youtube_url = "https://davemateer.com"

    # Replace this with the desired output file path for the screenshot
    # screenshot_output_path = 'youtube_screenshot.png'
    screenshot_output_path = '/home/dave/code/yt-test/youtube_screenshot.png'

    capture_youtube_screenshot(youtube_url, screenshot_output_path)
