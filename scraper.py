from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'                     

# driver = webdriver.Chrome('/path/to/chormedriver')
# In replit Chromedriver is already present on our path.

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos
if __name__=='__main__':
  print('Creating driver')
  driver = get_driver()

  print('Fetching trending videos')
  videos = get_videos(driver)
  #driver.get(YOUTUBE_TRENDING_URL)
  #print('Page title:', driver.title)

  #print('Get the video divs')
  #VIDEO_DIV_TAG = 'ytd-video-renderer'
  # video_divs = driver.find_elements_by_tag_name(VIDEO_DIV_TAG)
  #video_divs = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  print(f'Found {len(videos)} videos')
