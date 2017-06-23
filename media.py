import webbrowser

class Movie():
	"""This class stores movie related information."""

	# Class variable containing valid movie ratings
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	# __init__ function containing instance variables for the Movie class
	def __init__(self, movie_title, poster_image, trailer_youtube, release_date, director, genre, rating):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_date = release_date
		self.director = director
		self.genre = genre
		self.rating = rating

