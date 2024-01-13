from scraper import Scraper

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
    scraper = Scraper()
    albums = scraper.get_albums_by_artist(artist)
    max_rating = max([float(a[1]) for a in albums if a[1]])
    level = BasedLevel(max_rating, evaluate_basedness(max_rating))

    print("Max Album Rating:", level.max_rating)
    print("Basedness Level:", level.basedness)


if __name__ == "__main__":
    main()