import ypData
import sys

keyword = raw_input("What would you like to search for? >> ").strip().lower()
keyword.replace(" ", "+")
city = raw_input("Enter a city to search near >> ").strip()
city.replace(" ", "+")
state = raw_input("Enter two letter format of state >> ")
pages = raw_input("Enter number of pages to search (10 max) >> ").strip()


#add parsing for spaces and add part about state

info_list = ypData.get_yp_data(keyword, city, state, pages)

print
print("Here are the top results for \"%s\" in %s, %s:" % (keyword, city, state))

for i in info_list:
   print i['name']
   print (i['street'] + ", " +  i['locality'] + ", " + i['region'])
   print i['phone']
   print


#print
#option = raw_input("Which of these places do you want to learn" +\
#                   " more about? >> ").strip()
#
#info = {}
#for i in info_list:
#   if i['name'] == option:
#   info = i
#      break
#
#while info == {}:
#   print "Sorry, your response could not be found"
#   option = raw_input("Try Again: >> ")
#
#   for i in info_list:
#      if i['name'] == option:
#         info = i
#         break
#
#print
#print info['name']
#print (info['street'] + ', ' + info['locality'] + ', ' + info['region'] +\
#      ' ' + info['zip'])
#print info['phone']
#print
