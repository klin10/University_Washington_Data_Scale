import sys
import graph_toolz
import itertools

# code for six-degrees of Kevin Bacon

# call as "python3 <OPTION> <INPUT FILE> <THRESH>"
# <OPTION> is either "path", "bfs", or "justbuild". Read further to understand
# <INPUT FILE> is cleaned cast list
# <THRESH> is used to ignore movies with more than that many actors


what_should_this_do = sys.argv[1]

if what_should_this_do not in ["path", "bfs", "justbuild"]:
    print("Your option is illegal. Please choose one of ")
    print(" [\"path\", \"levels\", \"justbuild\"]")
else:
    f_input = open(sys.argv[2],'r', encoding="utf-8")
    thresh = int(sys.argv[3])

    all_cast = list()
    acted_in = dict()
    total = 0

    non_movies = ['Oscar\'s', 'Oscar', 'Hollywood', 'Sexiest', 'Awards', 'MTV',
                  'Movie Stars', 'Playboy', 'Blockbusters', 'Golden Globe',
                  'Saturday Night Live', 'Funny Females', 'Celebrity', 'SNL',
                  'Making', 'Shocking', 'Blockbuster', 'Concert','Gala',
                  'Red Carpet', 'Movies', '100', 'Donostia']


    # This part over here builds the graph
    for line in f_input.readlines():
        total = total + 1
        tokens = line.split('#') # Each line has # as delimiter
        person = tokens[0].strip() # First token/string before # is the person's name

        for i in range(1,len(tokens)):
            not_movie = False
            movie = tokens[i].strip()  # Determining every movie person has acted in
            if len(movie) == 0:
                continue

            for word in non_movies:
                if movie.find(word) != -1:  # Removing potential non-movies by finding substring in non-movies
                    not_movie = True
                    break
            if not_movie:
                continue

            all_cast.append((movie, person)) # all_cast is a list of tuples

    f_input.close()
    print("Created raw all_cast for every movie")

    all_cast.sort(key = lambda tup: tup[0]) # sort all_cast by the movie
    print("Sorted all_cast")

    cast = list()
    network = graph_toolz.Graph() # start empty graph

    # all_cast is now sorted by the movie. Thus, all actors in that movie appear contiguously in the all_cast. We simply pull out that list to build the graph. If movie has more than thresh credits, we ignore it
    prev = ' '  # initialization
    size = 0

    for i in range(0,len(all_cast)):
        movie = (all_cast[i])[0]
        person = (all_cast[i])[1]
        if movie == prev and i != len(all_cast)-1: # we've already seen this movie, and are thus continuing with the cast for the movie
            cast.append(person)  # adding person to cast of movie
            size = size+1 # tracking size of cast
            continue

        elif movie == prev and i == len(all_cast)-1: # special case for the last movie
            cast.append(person)
            size = size+1

        # if we get here, we're finished with this movie
        if size < thresh: # only consider movie is cast is smaller than thresh
            for actor in cast:
                if actor not in acted_in:
                    acted_in[actor] = set([prev])  # set up the credits for that actor
                else:
                    acted_in[actor].add(prev)
            for (person1, person2) in itertools.combinations(cast,2):
                network.addEdge(person1, person2)  # add edge for every pair of actors in movie

            prev = movie  # set up for next movie
            cast = [person]
            size = 1

    print(network.size()[0],"vertices. ",network.size()[1],"edges.")

    if what_should_this_do == "path":
        this_file = open("path.txt", "w")
        while True:
            src = input("Enter source: ")
            if src == 'q':
                break
            if src not in network.vertices:
                print("Not in network")
                continue

            dest = input("Enter destination: ")
            if dest not in network.vertices:
                print("Not in network")
                continue

            this_file.write('------------------------------------\n')
            this_file.write(src + "--->" + dest + "\n")
            this_file.write('------------------------------------\n')

            links = network.path(src, dest)
            if len(links) == 0:
                this_file.write("Path not found")
                print("Path not found")
                continue
            for i in range(0, len(links)-1): # printing out the actual path
                this_file.write(links[i]+ ' -- '+ links[i+1] + "\n")
                print(links[i]+ ' -- '+ links[i+1] + "\n")                
                movie_str = ''
                for movie in acted_in[links[i]].intersection(acted_in[links[i+1]]): # determining common movies between links[i] and links[i+1]
                    movie_str = movie_str + ' ' + movie + ';'
                this_file.write(movie_str + "\n")
                print(movie_str + "\n")                
                
    elif what_should_this_do == "levels":
        while True:
            src = input("Enter source: ")
            if src == 'q':
                break
            if src not in network.vertices:
                print("Not in network")
                continue

            level_sizes = network.levels(src)

            print(level_sizes)
