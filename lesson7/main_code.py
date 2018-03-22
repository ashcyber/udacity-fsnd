"""
    Udacity fsnd
    practice problem 1
    lesson 7

"""
import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

logan = media.Movie("Logan",
                    "American superhero film, produced by Marvel Entertainment, TSG Entertainment and The Donners' Company",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

infinity_war = media.Movie("Infinity War",
                            "Marvel's Studios Avengers: Infinity War",
                            "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                            "https://www.youtube.com/watch?v=QwievZ1Tx-8")

pacific_rim = media.Movie("Pacific Rim Uprising",
                            "American science-fiction action film directed by Steven S. DeKnight (in his feature-film directorial debut) ",
                            "https://upload.wikimedia.org/wikipedia/en/2/2e/Pacificrim2-poster.jpg",
                            "https://www.youtube.com/watch?v=_EhiLLOhVis")

sherlock_gnomes = media.Movie("Sherlock Gnomes",
                            "3D computer-animated comedy film directed by John Stevenson",
                            "https://upload.wikimedia.org/wikipedia/en/2/25/Sherlock_Gnomes.png",
                            "https://www.youtube.com/watch?v=TR-sefx8ncI")

tomb_raider = media.Movie("Tomb Raider",
                            "Tomb Raider is a 2018 action adventure film directed by Roar Uthaug",
                            "https://upload.wikimedia.org/wikipedia/en/b/bd/Tomb_Raider_%282018_film%29.png",
                            "https://www.youtube.com/watch?v=8ndhidEmUbI")


movies = [avatar, logan, infinity_war, pacific_rim,sherlock_gnomes,tomb_raider ]
fresh_tomatoes.open_movies_page(movies)
