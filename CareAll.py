# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:53:25 2020

@author: bines
"""

old={"alice":[67,4500],
     "kevin":[74,6500],
     "meghan":[65,5200]
     }
young={"nate":[21],
       "katy":[23],
       "melvin":[22]}
reviews={"alice":[7,"wonderfull person"],
         "meghan":[8,"really caring"],
         "kevin":[7,"Kind hearted"]}  
class person:   
      def user_info():
           global Name
           global Age
           global select
           Name    = input('Enter Your Name:')
           Age     = input('Enter your age:')
           purpose = input('Would you like to be a caregiver or taken care of(Enter 1 or 2):')
           if purpose == 2:
              wage = input('How much money can you offer the caregiver:')
              old[Name]=[Age,wage]
              young_table()
              select=input("Please enter the name of young person you choose ")
              for key in young.keys():
                  if key == select:
                     sub_menu(Name,key)



           elif purpose == 1:
              young[Name]=[Age]
              old_table()
              select=input("Please enter the name on person to explore further")
              for key in old.keys():
                  if key == select:
                     sub_menu(Name,key)

     def save_person(Name,select):
         persons={}
         persons[Name].append(select)


class menu():
      def old_table():
           print ('--------------------------------------------')
           print ("Name \t\t\tAge\t\tWage offered(Rs)\t\tRating")
           print ('--------------------------------------------')
           for key in old.keys():
               print (key + '\t\t'+ old[key][0][0]+'\t\t'+old[key][0][1]+'\t\t'+average_rating(key))

      def young_table():
           print ('------------------------------------------')
           print ("Name        Age     taking care of    Rating")
           print ('------------------------------------------')
           for key in young.keys():
               print (key + '\t\t'+ str(young[key][0][0])+'\t\t'+str(average_rating(key))

      def sub_menu(Name,select):
         print ("Averag rating :"+str(average_rating(Name))
         print ("____________________________________")
         print ("here are some reviews:"+
                   reviews[Name][0][1]+
                   reviews[Name][1][1]+
                   reviews[Name][2][1])
         a = input ("Do you wish to select this person ? yes/no")
         if a =="yes":
              save_person(Name,select)
              save_review(select)
         if a=="no":
              user_info()

class review():
      def save_review(Name):
           print ("please rate your your experience with this person. On a scale from 1 to 10")
           rating    = input ('1 being Worst and 10 being Wonderfull! :')
           review    = input ('Please describe your experience with this person in 100 words:')
           reviews[Name]=[rating,review]

      def average_rating(Name):
         y=0
         for x in range(len(reviews[Name])):
              y=y+reviews[Name][x][0]
         return y/len(reviews[Name])

      def show_reviews(Name):
          for x in range(len(reviews[Name])):
              print (reviews[Name][x][1])