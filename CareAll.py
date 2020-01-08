# loading data to old , young and reviews dictionaries
old={"alice":[67,4500],
     "kevin":[74,6500],
     "meghan":[65,5200]
     }
young={"nate":[21],
       "katy":[23],
       "melvin":[22]}
reviews={"alice":[7,"wonderfull person"],
         "meghan":[8,"really caring"],
         "kevin":[7,"Kind hearted"],
         "nate":[8,"Very Hardworking"],
         "katy":[4,"Bad manners"],
         "melvin":[2,"always late"]}



# A method to initialise the program , enter name age and other details.
def user_info():
    name,age = input('Enter your name and age : ').split()
    purpose = input('Would you like to be a Caregiver or taken care of (Enter 1 or 2 ) : ')
    if int(purpose) == 1:
        young[name]=age
        old_table()
        select = input('Please enter the name of person: ')
        for key in old.keys():
          if key == select:
            sub_menu(name,key)
    elif int(purpose) == 2:
        wage = input('How much money can you offer the care giver? ')
        old[name]=[age,wage]
        young_table()
        select=input("Please enter the name of young person you choose: ")
        for key in young.keys():
          if key == select:
            sub_menu(name,key)

# Save the person choosen by the user.

def save_person(name,select):
    persons=dict()
    if name not in persons:
        persons[name]=select
    else:
        persons[name]+=select

# All the tables are kept in a seperate class
# A table to display all the old people registered.
def old_table():
	print ('--------------------------------------------')
	print ("Name\t\t\tAge\t\tWage offered(Rs)\t\tRating")
	print ('--------------------------------------------')
	for key,value in old.items():
		    print (key + '\t\t'+ str(value[0])+'\t\t'+str(value[1])+'\t\t'+str(average_rating(key)))

# A table to display all the ypiung people registered.

def young_table():
    print('--------------------------------------------------')
    print('Name          Age      taking care of      Rating')
    print('--------------------------------------------------')
    for key,value in young.items():
        print(key+'\t\t'+str(value)+'\t\t'+str(average_rating(key)))

# To look at a persons ratings and reviews you have to select them by entering their name

def sub_menu(name,select):
    print("Average rating : "+str(average_rating(select)))
    print('---------------------------------------------')
    print('Here are some reviews :'+reviews[select][1])
    a = input("Do you wish to select this person? (1 or 2)")
    if a == '1':
        save_person(name,select)
        save_review(select)
    elif a == '2':
        user_info()

def average_rating(Name):
    b=0
    for _,y in reviews.items():
        b += y[0]
    return b/len(reviews)

def show_reviews(Name):
    for x in range(len(reviews[Name])):
        print(reviews[Name][x][1])


def save_review(name):
    print('Please rate your experience with this person. On a scale of 1 to 10')
    rating = input('1 being worst and 10 being wonderful! : ')
    review = input('Please describe your experience with this person in 100 words : ')
    if name not in reviews:
        reviews[name]=[rating,review]
    else:
        reviews[name]+=[rating,review]
    user_info()

user_info()
