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
        print('please enter the search term:')
        y = input()
        i = 0
        for j in movies._movies:
            if y.casefold() in j['name'].casefold():
                print(j['name'])
                i += 1
        if i == 0:
            print('No results found')
        print('\n')
    elif x == 'cast':
        print('please enter the search term:')
        y = input()
        i = 0
        for j in movies._movies:
            for k in j['cast']:
                if y.casefold() in k.casefold():
                    print(j['name'])
                    print(f'[\'{k}\']')
                    i += 1
        if i == 0:
            print('No results found')
        print('\n')
    else: 
        print("Unknown option selected, try again \n")