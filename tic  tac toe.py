#functions ================))))))
#import calendar
#print(calendar.weekheader(3))
#print()

#print(calendar.firstweekday())
#print()

#print(calendar.month(2020 , 3 , ))

#print(calendar.monthcalendar(2020 , 3))
#print(calendar.calendar(2020))

#day_of_the_week = calendar.weekday(2020 , 3 , 8)
#print(day_of_the_week)

#is_leap = calendar.isleap(2020)
#print(is_leap)

#how_many_leap_days = calendar.leapdays(2000,2021)
#print(how_many_leap_days)

#primitive data types:==============)))))
#int 12354..
#float 0.2,-0.45
#strings "under coatations"
#boolean true or false first letter capital.

#casting:    =====================)))))))

#strings in python==============))))
#s ="hello maam"
#print(s[1])


#lists in python: =========))))))
#collections of things in order is called a list.
#l = [1,2,3]
#l2 =[1,"string","slkd",4.3,True,[1,2,3]]
#print(l2)
#print(l)
#indexing is possible like we can printl[0] to l[5] elleemenet.
#numbers = [6,4,2,9,12]
#print(numbers)
#numbers.sort()
#print(numbers)
#for numbers in numbers:
    #print(numbers)
#names = ["joe","jhon","james"]
#print(names)
#names.append("gary")
#names.insert(1,"gary")
#names.remove("joe")
#names.reverse()
#print(names)

#index slicing: ============))))))))
#indexing,slicing,striding
#if we us ea negeative indexing then the count satrats from back:
#digits = [0,1,2,3,4,5,6,7,8,9]
#print(digits[-2])
#print(digits[0:8]#this is slicing in python)
#name = "first last"
#print(name[::3])
#this is called striding in python.
#for i in range(len(digits)):
    #print(digits[0:i])
#window_size = 5
#for i in range(len(digits) -(window_size-1) ):
    #print(digits[i:i+window_size])#dynamic slicing.

#slpliting and joining
#problems = "broke, pale, short, nerdy"
#print(problems)

#l = problems.split(", ")
#print(l)

#joined = " and ".join(l)
#print(joined)
#csv = ",".join(l)
#print(csv)

#tupples in python: ================))))))
#python tupples data types:
#tuples are similar to list but have parenthesis:
#t = [1,2,3,4]
#credit_card1= (1234123412341234,"joe rogan","11/20",123)
#credit_card2 = (1234123412341234,"joe rogan","11/20",123)
#credit_cards = [credit_card1 , credit_card2]
#print(credit_cards)

#unpacking of tupples:
#person1=("nancy-pants",25,"pizza")
#person2 =("joe-shirt",20,"pasta")
#people = (person1,person2)

#name,age,favfood = person
#print(name)
#print(age)
#print(favfood)

#for name,age,favfood in people:
    #print(name)
    #print(age)
    #print(favfood)
    #print()

#sets in python:  =============)))))))))))
#python sets data type:
#l =[1,2,3,3,4,4,4,5,"abc","abc"]

#no_duplicate_set = set(l)

#print(no_duplicate_set)

#no_duplicate_list = list(no_duplicate_set)

#l = no_duplicate_list
#print(l)
#s = {"blueberry", "rasberry"}
#s.add("blueberry")
#print(s)

#library1 = {"harry pottar","hunger games","lord of the rings"}
#library2 = {"harry pottar","romeo and juliet"}

#all_books_in_town = library1.union(library2)
#at_both_library = library1.intersection(library2)
#diff = library1.difference(library2)
#clearence = library1.clear()
#print(clearence)


#dictionaries in python:   =========))))))]
#dictionaries datastructure
#the left one is called the key and right one is the value:
#groceries = {"banana": 5,"oranges": 3}

#print(groceries["banana"])
#we can also use.get:
#print(groceries.get("hello"))


#contacts = {
    #"joe":{"phone":1234567,"email":"joe@hapsikabacha"},
    #"jane":{"phone":67890678,"email":"jane@hapsi ki bachi"}
#}
#print(contacts["jane"])

#sentence = "my name is the abhishek bisht"

#word_counts = {
    #"i":1,
    #"my":1,
    #"the":3
#}
#print(word_counts)
#word_counts["abhishek"] = 2
#print(word_counts)#thats how u add in the dictionary
#word_counts["the"] = word_counts["the"] = 1
#sorting a dictinary:
#dict.items()this gives the list of all the tupples
#print(word_counts.items())
#dict.keys()
#print(word_counts.keys())
#dict.values()
#print(word_counts.values())

#for deleting..
#we can pop off any element by using its key in the pop function
#print(word_counts)
#word_counts.pop("i")
#print(word_counts)
#print(word_counts)
#word_counts.popitem()
#print(word_counts)
#this pops out an arbitary element;
#word_counts.clear()#it will wipe out the whole dictionary:

#print(dictsorted() (word_counts.values())) doubt bc>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#mutability with python:================))))))))))))))))ex - list,dictionaries,ordered and unordered
#tupple is imutable:int,float,boolean

#t = (1,2,[1,2,3])
#print(t)
#t[2][0] = 7
#print(t)


#list compreehnsions  in python:==================))))))))))))))))

#names = ["jennifer","suzan","james","sophie"]

#l = []

#for person in names:
    #l.append(person)
#print(l)
#in this we placed all the items from the previous list to the newly created list l by appendding persons in the list:

#print([person for person in names])#this is the list comprehension:


#l = []

#for person in names:
    #l.append(person + "dumped me.")
#print([person +"dumped me." for person in names])

#movies_an_rating = {"interstelaar":9,"dark knight":8,"50 shades":3,"50 shadesdarker":2 ,"50 shades darkest":1}

#l = []
#for movie in movies_an_rating:
    #if movies_an_rating[movie] >6:
        #l.append(movie)
#print(l)
#or
#print([movie for movie in movies_an_rating if movies_an_rating[movie]>6])
#regex with python and creating email scraper:=====))))))))))))))

#doubt
#import re
#text = "random string.My123@website.com. some meore text. your_name.8_8_a@company.net"

#pattern = re.compile(" [a-zA-Z0-9\.\-\+]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

#result  = pattern.findall(text)

#print(result)

#date time modules with python:========))))))))))))))))))
#how can we take a string and convert it into day time:
#import datetime
#import pytz

#today = datetime.date.today()
#print(today)

#birthday = datetime.date(1994,7,14)
#print(birthday)

#find days since birth
#days_since_birth = (today-birthday).days
#print(days_since_birth)

#addding 10 days to current day
#tdelta = datetime.timedelta(days = 10)
#print(today+tdelta)

#print(today.month)
#tuesday =1
#print(today.weekday())
#monday  = 0 and sunday = 6

#print(datetime.time(7,2,20,15))
#dateime.date(y,m,d)
#datetime.time(h,m,s,ms)
#datetime.datetime(y,m,d,h,m,s,ms)

#add 10 hours to your current date
#hour_delta = datetime.timedelta(hours = 10)
#print(datetime.datetime.now()+hour_delta)

#datetime.datetime.now(tz = pytz.utc)

#string formating with dates
#datetime_pacific = datetime_today.astimezone(pytz.timezone("us/pacific"))
#datetime_pacific.strftime
#print(datetime_pacific)
#for tz in pytz.all_timezones:
    #print(tz)

#print(datetime_pacific.strftime("%b %d,%y"))



#web scraping with puthon:=========)))))))
#yetto be learnt


#zip fuctions in puthon:==========)))))))))))))))))))


#this is also called self document code
#list1 = [1,2,3,4,5]
#list2 = ["one","two","three","four","five"]

#zipped = list(zip(list1,list2))
#print(zipped)

#unzip this mojo is just like zip but inorder to unzip it we require to put an *


#unzziped = list(zip(*zipped))
#print(unzziped)

#for (l1,l2) in zip (list1,list2):
    #print(l1)
    #print(l2)

#items = ["apple","banana","orange"]
#counts = ["3 ,6 ,4"]
#prices = ["0.99","0.25","0.50"]


#sentences = list(zip(items,counts,prices))
#for (item,count,price) in zip(items,counts,prices ):
    #item, count, price = str(item), str(count), str(price)
    #sentence = "I bought "+ count +' ' + item +  's at '+ price + " cents each."
    #sentences.append(sentence)
#print(sentences)


#tic tac toe  aapppp:===========)))))))))))))))))


#global vareiables
#game board


board = ["-","-","-",
        "-","-","-",
        "-","-","-",]
#if game still going
game_still_going = True

#who won
winner = None

#whoes turn?
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
   #display initial board
   display_board()

while game_is_still_going:

    handle_turn(current_player)

    check_if_game_over()

    flip_player()

#the agame has ended

 if winner = "X" or winner = "O":
      print(winner+ "won")
 elif winner = None:
     print("tie")




def handle_turn(player):
    position = input("choose a position from 1-9:")
    position = int(position) - 1

    board[position] = "X"

    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()



def check_if_win():
    #cheeck rows
    #check colomns
    #check diagonals
    return

def check_if_tie():
    return

def flip_player():
    return
play_game()







