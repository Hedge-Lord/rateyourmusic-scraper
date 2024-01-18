# EXAMPLE USE !
from rymscraper import scraper

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


def main():
    artist = input("Evaluate Artist: ")
    print(f"EXAMPLE RUN: Evaluating {artist} Basedness Level:")
    rymscraper = scraper.Scraper()
    info = rymscraper.get_artist_info(artist)
    albums = info['albums']
    max_rating = max([float(a[1]) for a in albums if a[1]])
    level = BasedLevel(max_rating, evaluate_basedness(max_rating))

    print("Highest Album Rating:", level.max_rating)
    print("Verdict:", level.basedness)

    yesno = input("View all albums and genres? y/n: ")
    if yesno == "n" or yesno != "y":
        print("byebye!")
        return
    else:
        for g in info['genres']:
            print(g)
        print("Albums: ")
        for a in albums:
            print(a[0])
            print("Rated:", a[1], "Ratings:", a[2])


if __name__ == "__main__":
    main()