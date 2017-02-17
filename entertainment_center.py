import media
import fresh_tomatoes

#Create instances of favorite movies
men_of_honor = media.Movie("Men Of Honor",
                        "The story of Carl Brashear, the first African American, then also the first amputee, US Navy Diver and the man who trained him.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc1Njk1NTE3NF5BMl5BanBnXkFtZTgwNjAyMzcxMTE@._V1_.jpg",
                        "https://www.youtube.com/watch?v=E21xH5vg0yo")

step_brothers = media.Movie("Step Brothers",
                           "Two aimless middle-aged losers still living at home are forced against their will to become roommates when their parents marry.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcwNzUzMjU1OV5BMl5BanBnXkFtZTcwMTM0NDQ2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=CewglxElBK0")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=Q8g9zL-JL8E")


# Create list of movie instances
movie_list = [men_of_honor, step_brothers, the_matrix]

# Generate movie page HTML and show in browser tab
fresh_tomatoes.open_movies_page(movie_list)
