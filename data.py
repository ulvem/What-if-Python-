# WRITE YOUR CODE HERE
# WRITE YOUR CODE HERE
fav_movies = [
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.8,
        "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "directors": ["Christopher Nolan"],
        "writers": ["Christopher Nolan"],
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "genres": ["Action", "Adventure", "Sci-Fi"]
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "rating": 8.7,
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "directors": ["Lana Wachowski", "Lilly Wachowski"],
        "writers": ["Lana Wachowski", "Lilly Wachowski"],
        "actors": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "genres": ["Action", "Sci-Fi"]
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "rating": 8.6,
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "directors": ["Christopher Nolan"],
        "writers": ["Jonathan Nolan", "Christopher Nolan"],
        "actors": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "genres": ["Adventure", "Drama", "Sci-Fi"]
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "description": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
        "directors": ["Christopher Nolan"],
        "writers": ["Jonathan Nolan", "Christopher Nolan"],
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "genres": ["Action", "Crime", "Drama"]
    }
]

# Using a for loop to print all movie titles
for movie in fav_movies:
    print(movie["title"])

# Using a while loop to print all movie titles
index = 0
while index < len(fav_movies):
    print(fav_movies[index]["title"])
    index += 1

# Calculate the average rating
total_rate = 0
for movie in fav_movies:
    total_rate += movie["rating"]

average_rate = total_rate / len(fav_movies)

# Print the average rating
print(f"The average rating of the movies is: {average_rate:.2f}")

# Find the newest movie
newest_movie = max(fav_movies, key=lambda movie: movie["year"])

# Print the title of the newest movie
print(f"The title of the newest movie is: {newest_movie['title']}")

# Initialize the stars_by_movies variable
stars_by_movies = ""

# Use nested loops to concatenate movie titles and their stars
for movie in fav_movies:
    stars_by_movies += f"{movie['title']}:\n"
    for actor in movie["actors"]:
        stars_by_movies += f"  - {actor}\n"
    stars_by_movies += "\n"

# Print the stars_by_movies variable
print(stars_by_movies)

