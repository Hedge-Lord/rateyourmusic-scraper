from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.window import WindowTypes
import time

class BasedLevel:
    def __init__(self, max_rating, basedness):
        self.max_rating = max_rating
        self.basedness = basedness

def evaluate_basedness(max_rating):
    if max_rating >= 4:
        return "Extremely Based."
    elif max_rating >= 3.85:
        return "Very Based."
    elif max_rating >= 3.7:
        return "Based."
    elif max_rating >= 3.5:
        return "Mildly Based."
    elif max_rating >= 3.3:
        return "Normal."
    elif max_rating >= 3:
        return "Acceptable."
    elif max_rating >= 2.5:
        return "Average."
    elif max_rating >= 2:
        return "Mildly Cringe?"
    else:
        return "Cringe."

def is_artist_based(artist):
    artist = "-".join(artist.lower().split())
    artist = ''.join(c for c in artist if c.isalnum() or c == '-')
    url = "https://rateyourmusic.com/artist/" + artist

    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(url)
        time.sleep(0.5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        album_div = soup.find('div', id='disco_type_s')

        if album_div:
            rating_elements = album_div.find_all('div', class_='disco_avg_rating enough_data')
            ratings = [r.text.strip() for r in rating_elements]
            max_rating = max([float(r) for r in ratings])
            return BasedLevel(max_rating, evaluate_basedness(max_rating))
        else:
            return BasedLevel(-1, "No Albums or Artist found.")

    except Exception as e:
        return f"An error occurred: {e}"
    
    finally:
        driver.quit()


def main():
    artist = input("Evaluate Artist: ")
    print(f"EXAMPLE RUN: Evaluating {artist} Basedness Level:")
    level = is_artist_based(artist)
    print("Max Album Rating:", level.max_rating)
    print("Basedness Level:", level.basedness)


if __name__ == "__main__":
    main()