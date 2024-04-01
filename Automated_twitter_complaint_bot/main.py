from selenium import webdriver
from selenium.webdriver.common.by import By
import tweepy
import time

# Already deleted the bot feel free to try :)
api_key = "IPthcheuVg8q8ebajNGsCWj7H"
api_secret = "u50JgBi9aaycePHaWW0l1KCpqfCGbEwgh5DXqbsHX0HfDqmVah"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAADZxtAEAAAAA64T4try%2FfNNpu8ax7thB5O1lifs%3DLl9TREcOA0Tb9I5HcRfQqkIMrWmWm8hHtDRQep18IiQ0KH0zFf"
access_token = "1773701469612482560-55otwPEcQMbRRN5TmxmqwazhZ0VTUG"
access_token_secret = "2HuuOplJHL3NJjreFic4OmhTHvnvYgnymVZzpt8fRkjSB"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.download = ""
        self.upload = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.pl/")
        start_test = self.driver.find_element(By.XPATH, value="//*[@id='tester']/div[1]/div/div/div")
        cookie_div = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
        time.sleep(6)
        cookie_div.click()
        time.sleep(5)
        start_test.click()
        time.sleep(90)

        download_speed_div = self.driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/span')
        upload_speed_div = self.driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[3]/div[4]/div/span')
        self.download = download_speed_div.text
        self.upload = upload_speed_div.text
        self.driver.quit()

    def make_twitter_complaint(self):
        client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

        client.create_tweet(text=f"Hej dostawco internetu, moj internet to {self.download} downloadu i {self.upload} uploadu")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.make_twitter_complaint()
