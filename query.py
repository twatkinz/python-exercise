from movies import Movies

movies = Movies('./movies.txt')


print("Choose an option:")

menu = {}
menu['q']="enter q for exit" 
menu['list']="enter list for listing all the movie names"
menu['search']="enter search for searching movies"
menu['cast']="enter cast for searching cast"

while True: 
    options=menu.keys()
    for entry in options: 
      print ('*', menu[entry])
    print('\n')

    x=input() 
    if x =='q': 
        break 
    elif x == 'list': 
        i = 1
        for title in movies._movies:
            print(i, title['name'])
            i += 1
        print('\n')
    elif x == 'search':
        print('Come back later \n')
    elif x == 'cast':
        print('Come back later \n')
    else: 
        print("Unknown option selected, try again \n")