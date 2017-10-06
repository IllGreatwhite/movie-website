import fresh_tomatoes
import media
# following are instances of Movie class
gladiator = media.Movie("Gladiator",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")

kajaki = media.Movie("Kajaki",
                     "https://upload.wikimedia.org/wikipedia/en/5/5b/Kajaki_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=ZAP-80toA44")

lone_survivor = media.Movie("Lone survivor",
                            "https://upload.wikimedia.org/wikipedia/en/b/bd/Lone_Survivor_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=VuIINk0IftU")

# fresh_tomatoes takes in a list and outputs html
movies = [gladiator, kajaki, lone_survivor]
# use .open_movies_page from fresh_tomatoes to activate web page
fresh_tomatoes.open_movies_page(movies)
