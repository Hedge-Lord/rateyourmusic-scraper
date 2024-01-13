import pytest

@pytest.mark.parametrize("artist, num_albums", [("miles davis", 62), ("kendrick lamar", 5)])
def test_get_album_by_artist(artist, num_albums, rymscraper):
    a = rymscraper.get_albums_by_artist(artist)
    # print(a)
    assert len(a) == num_albums