import pytest
import requests_mock
from app import fetch_poster

# Define the base URL of the API
BASE_URL = 'https://api.themoviedb.org/3/'

def test_fetch_poster():
    # Define the URL of the movie endpoint
    movie_id = 19995
    movie_url = f'{BASE_URL}movie/{movie_id}'

    # Define the expected poster URL (complete URL including base URL)
    expected_poster_url = 'https://image.tmdb.org/t/p/w1280/kyeqWdyUXW608qlYkRqosgbbJyK.jpg'

    # Create a requests_mock instance
    with requests_mock.Mocker() as mocker:
        # Mock the response for the movie endpoint
        mocker.get(movie_url, json={'poster_path': 'kyeqWdyUXW608qlYkRqosgbbJyK.jpg'})

        # Call the fetch_poster function with the movie ID
        poster_url = fetch_poster(movie_id)
        print(poster_url)

        # Verify that the function returns the expected poster URL
        assert poster_url == expected_poster_url

# Run the test
if __name__ == "__main__":
    pytest.main()
