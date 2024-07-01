import pytest
from app import recommend

@pytest.mark.parametrize("movie, expected_movies", [
    ("John Carter", ["Star Trek: Insurrection", "Mission to Mars", "Captain America: The First Avenger", "Escape from Planet Earth", "Ghosts of Mars"]),
    # Boundary cases
    ("Avatar", ["Titan A.E.", "Small Soldiers", "Independence Day", "Aliens vs Predator: Requiem", "Ender's Game"]),
    ("Primer", ["Lovely & Amazing", "My Big Fat Greek Wedding 2", "I Don't Know How She Does It", "Hope Springs", "Extreme Movie"]),
])
def test_recommend(movie, expected_movies):
    # Call the recommend function with the given movie
    recommended_movies, _ = recommend(movie)

    # Check if the recommended movies match the expected movies
    assert recommended_movies == expected_movies


import pytest
from app import recommend


def test_consistency():
    # Define a list of movies to test
    movies_to_test = [
        "Avatar",
        # Add more movies as needed
    ]

    # Iterate over each movie in the list
    for movie in movies_to_test:
        # Call the recommend function to get recommended movies for the current movie
        recommended_movies, _ = recommend(movie)

        # Check if recommended_movies is not empty
        assert recommended_movies, f"No movies recommended for {movie}"

        # Initialize a counter to track the number of times "Avatar" appears in recommendations
        avatar_count = 1

        # Iterate over each recommended movie
        for recommended_movie in recommended_movies:
            # Call the recommend function to get recommended movies for the current recommended movie
            secondary_recommendations, _ = recommend(recommended_movie)

            # Check if the original movie "Avatar" is in the secondary recommendations
            if "Avatar" in secondary_recommendations:
                avatar_count += 1

        # Check if "Avatar" appears in recommendations of all recommended movies
        assert avatar_count == len(
            recommended_movies), f"Avatar not recommended in all secondary recommendations for {movie}"

