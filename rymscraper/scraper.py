from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

class Scraper:
    def __init__(self):
        options = Options()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)

    def __del__(self):
        self.driver.quit()

    def get_albums_by_artist(self, artist):
        artist = "-".join(artist.lower().split())
        artist = ''.join(c for c in artist if c.isalnum() or c == '-')
        url = "https://rateyourmusic.com/artist/" + artist

        try:
            self.driver.get(url)
            time.sleep(0.2)
            try:
                show_more_button = self.driver.find_element(By.ID, 'disco_header_show_link_s')
                if show_more_button:
                    self.driver.execute_script("arguments[0].click();", show_more_button)
                    time.sleep(2)
            except:
                None
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            album_div = soup.find('div', id='disco_type_s')
            if album_div:
                albums = album_div.find_all('div', class_='disco_release')
                album_info_html = [
                    [a.find('a', class_='album'), 
                    a.find('div', class_='disco_avg_rating enough_data'), 
                    a.find('div', class_='disco_ratings')] for a in albums
                ]
                album_info = [
                    [(e.text.strip() if e and e.text is not None else None) for e in a]
                    for a in album_info_html
                ]
                return album_info
            else:
                return []

        except Exception as e:
            return f"An error occurred: {e}"

def main():
    scraper = Scraper()
    print(scraper.get_albums_by_artist("miles davis"))

if __name__ == "__main__":
    main()