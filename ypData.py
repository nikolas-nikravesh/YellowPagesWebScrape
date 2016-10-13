import sys
import requests
from bs4 import BeautifulSoup


def get_yp_data(key, city, state, num_pages):

   url = "http://www.yellowpages.com/search?search_terms=" + \
          key + "&geo_location_terms=" + city + "%2C+" + state

   info_list = []

   for i in range(0, int(num_pages)):
      page_num = i
      page = "&page=" + str(page_num)
      r = requests.get(url + page)

      soup = BeautifulSoup(r.content, "lxml")

      info = soup.findAll("div", {"class": "info"})
      street = "Not Found"
      loc = "Not Found"
      zipCode = "Not Found"
      region = "Not Found"
      phone = "Not Found"

      for item in info:
         name = item.find("a", {"class": "business-name"}).text.strip()

         addr = item.find("p", {"class": "adr"})

         try:
            street =  addr.find("span", {"class": "street-address"}).text.strip()
         except:
            pass

         try:
            loc = addr.find("span", {"class": "locality"}).text.replace(',','').strip()
         except:
            pass

         try:
            region = addr.find("span", {"itemprop": "addressRegion"}).text.strip()
         except:
            pass

         try:
            zipCode = addr.find("span", {"itemprop": "postalCode"}).text.strip()
         except:
            pass

         try:
            phone = item.find("div", {"itemprop": "telephone"}).text.strip()
         except:
            pass


         info_dict = {'name': name, 'street': street, 'locality': loc, 
                      'region': region, 'zip': zipCode, 'phone': phone}

         info_list.append(info_dict)


   return info_list
