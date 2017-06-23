import fresh_tomatoes
import media

# The following 6 movies are instances of the Movie class
blade_runner = media.Movie("Blade Runner",
							"https://madspoon.net/images/filmovi/blade-runner.jpeg",
							"https://www.youtube.com/watch?v=W_9rhPDLHWk",
							1982,
							"Ridley Scott",
							"Neo-noir science fiction",
							media.Movie.VALID_RATINGS[3])

robocop = media.Movie("Robocop",
						"https://www.theterminatorfans.com/wp-content/uploads/2013/09/RoboCop-1987-Poster.jpg",
						"https://www.youtube.com/watch?v=qaNRzjGsOeA",
						1987,
						"Paul Verhoeven",
						"Cyberpunk action",
						media.Movie.VALID_RATINGS[3])

kill_bill = media.Movie("Kill Bill",
						"https://img.csfd.cz/files/images/user/profile/159/451/159451641_729a41.jpg",
						"https://www.youtube.com/watch?v=7kSuas6mRpk",
						2003,
						"Quentin Tarantino",
						"Martial arts action",
						media.Movie.VALID_RATINGS[3])

ghost_in_the_shell = media.Movie("Ghost in the Shell",
								"https://68.media.tumblr.com/bbf0183b4e3d85f806930d0dbc4dc756/tumblr_n9c3rc55Bp1qbluruo2_r1_1280.jpg",
								"https://www.youtube.com/watch?v=Dfqnbp8AJ9U",
								1995,
								"Mamoru Oshii",
								"Science fiction",
								media.Movie.VALID_RATINGS[3])

akira = media.Movie("Akira",
					"https://i443.photobucket.com/albums/qq155/ACNRVP/Kaneda/Kaneda%20Out%20of%20The%20Box/akiraMoviePoster1.jpg",
					"https://www.youtube.com/watch?v=pC6Qk5XxGIY",
					1988,
					"Katsuhiro Otomo",
					"Science fiction",
					media.Movie.VALID_RATINGS[3])

spirited_away = media.Movie("Spirited Away",
							"https://upontheshelfreviews.files.wordpress.com/2016/04/600full-spirited-away-poster.jpg",
							"https://www.youtube.com/watch?v=ByXuk9QqQkk",
							2001,
							"Hayao Miyazaki",
							"Fantasy",
							media.Movie.VALID_RATINGS[1])

# List of movies containing the 6 movies above
movies = [blade_runner, robocop, kill_bill, ghost_in_the_shell, akira, spirited_away]

# Call the open_movies_page function with the movies list as an argument
fresh_tomatoes.open_movies_page(movies)

