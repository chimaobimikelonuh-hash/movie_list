watchlist = []
watched = []
genres = set()

choice = ""
subchoice = ""

while True:
    print("----- MOVIE PROGRAM -----")
    print("1. Add a movie to watchlist")
    print("2. Mark a movie as watched")
    print("3. List movies")
    print("4. Shows unique genres")
    print("5. Summary")
    print("6. Exit")
    print("-------------------------")

    choice = input("Enter your choice: ")
    # 1. Add movie
    if choice == "1":
        title = input("Enter title of movie: ").strip().title()
        genre = input("Enter genre of movie: ").strip().title()
        year = input("Enter year: ").strip()

        movie = (title, genre, year)

        watchlist.append(movie)
        genres.add(genre)

    #2. Mark a movie as watched
    if choice == "2":
        subchoice = input("Enter the movie you want to mark: ").strip().title()
        subchoice1 = input("What year was the movie produced?: ").strip()
        found = None
        for movie in watchlist:
           if movie[0] == subchoice and movie[2] == subchoice1:
              found = movie
              break
        if found:
            watchlist.remove(found)
            watched.append(found)
            print("You have marked a movie!")
        else:
            print("Movie not found")

    #3. List of all movies
    if choice == "3":
        print(f"Watched movies: {watched}")
        print(f"Movies in watchlist: {watchlist}")

    #4. List of unique genres
    if choice == "4":
        print(f"Unique genres: {genres}")
    
    #5 Summary of movie list
    if choice == "5":
        print(f"Total genres: {len(genres)} ")

    if choice == "6":
        print("Bye Bye")
        break