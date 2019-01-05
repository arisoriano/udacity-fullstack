import fresh_tomatoes
import media

# Movie objects for 6 movies
toy_story = media.Movie(
    "Toy Story", "A story of a boy and his toys come to life",
    "https://bit.ly/2QWzgUz", "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar", "A marine on an alien planet",
    "https://bit.ly/2Pr05PG", "https://youtu.be/6ziBFh3V1aM")

school_of_rock = media.Movie(
    "School of Rock", "Using rock music to learn",
    "https://bit.ly/2GKCplu", "https://youtu.be/XCwy6lW5Ixc")

ratatouille = media.Movie(
    "Ratatouille", "A rat is a chef in Paris",
    "https://bit.ly/2LDbqHB", "https://youtu.be/NgsQ8mVkN8w")

midnight_in_paris = media.Movie(
    "Midnight in Paris", "Going back in time, a love story",
    "https://bit.ly/2ETo70f", "https://youtu.be/FAfR8omt-CY")

lotr = media.Movie(
    "Lord of the Rings",
    "Eight companions set out on a journey to destroy the One Ring",
    "https://bit.ly/2zKhRDI", "https://youtu.be/V75dMMIW2B4")

# Movie instances initialized into an array
movies = [
    toy_story, avatar, school_of_rock,
    ratatouille, midnight_in_paris, lotr]

# Invoke  HTML creation method
fresh_tomatoes.open_movies_page(movies)
