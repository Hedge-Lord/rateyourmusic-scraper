import pytest

@pytest.mark.parametrize("artist, num_albums", [("miles davis", 62), ("kendrick lamar", 5)])
# @pytest.mark.skip(reason="takes too long")
def test_get_album_by_artist(artist, num_albums, rymscraper):
    a = rymscraper.get_artist_info(artist)['albums']
    # print(a)
    assert len(a) == num_albums

def test_artist_search(rymscraper):
    assert rymscraper.get_artist_url("aphex twin") == "https://rateyourmusic.com/artist/aphex-twin"
