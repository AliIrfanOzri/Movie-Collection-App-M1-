#where to store movies : in List

# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_moives():
# You may want to create a function for this code
   title = input("Enter the movie title: ")
   director = input("Enter the movie director: ")
   year = input("Enter the movie release year: ")

   movies.append({
    'title': title,
    'director': director,
    'year': year
   })


def show_moive():
    for movie in movies:
        print(f"movie: {movie['title']}")
        print(f"directer: {movie['director']}")
        print(f"Relese Year: {movie['year']} ")

def find_movie():
    search = input("Enter Movie Name For Search")
    for movie in movies:
        if search == movie['title']:
            print(f"movie: {movie['title']}")
            print(f"directer: {movie['director']}")
            print(f"Relese Year: {movie['year']} ")

# Create other functions for:
#   - listing movies
#   - finding movies



user_input = {
    "a":add_moives,
    "f":find_movie,
    "l":show_moive

}

# And another function here for the user menu
def menu():
   selection = input(MENU_PROMPT)
   while selection != 'q':
       if selection in user_input:
           selection_function = user_input[selection]
           selection_function()
       else:
          print('Unknown command. Please try again.')

       selection = input(MENU_PROMPT)

menu()

