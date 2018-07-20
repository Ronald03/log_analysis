# DB Log Analysis
This python connects with database and adquires useful information about articles and authors, and finally exports it to a file.

## Install
 - Download python from [here](https://www.python.org/)
 - Fork and clone this repository [here](https://github.com/Ronald03/movie_trailers_website)
  
 
## How to use
- To read or modify the code, go to the directory where you cloned or downloaded the code
- Use python IDLE or a text editor (i.e. SublimeText 3) to inspect and modify the code
- To see the result of the code run the fresh_tomatoes.py file by pressing (F5) from the Python IDLE or from a terminal by going to the directory and typing 'python fresh_tomatoes.py'
- A browser tab should open with your Movie trailer page
 
### To add new movies
- Open the 'show_trailer.py' with a text editor or by ritgh clicking the file and choosing Edit with IDLE
- Use the format shown below:
 
```
new_movie = media.Movie("title",
                     "storyline of the movie",
                     "Link of the poster Image",
                     "Link of the Video trailer")

movies = [new_movie] //add your new movies separated by commas
fresh_tomatoes.open_movies_page(movies)
```
## License
This is .....**free to the public!**
