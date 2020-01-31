#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:57:11 2020

@author: ep9k
"""

import requests
from bs4 import BeautifulSoup

#Corey Schafer's BeautifulSoup web scraper
#source = requests.get('http://coreyms.com').text
#
#soup = BeautifulSoup(source, 'html.parser')    #built in html parser from python standard library
#
#article = soup.find('article')
#for article in soup.find_all('article'):
#
#    headline = article.h2.a.text
#    print(headline)
#    
#    summary = article.find('div', class_='entry-content').p.text
#    print(summary)
#    
#    try:
#        vid_src = article.find('iframe', class_='youtube-player')['src']
#        vid_id = vid_src.split('/')[4]
#        vid_id = vid_id.split('?')[0]
#        
#        
#        yt_link = f'http://youtube.com/watch?v={vid_id}'
#        print(yt_link)
#       
#    except Exception:
#        pass
#    
#    
#    print()




##Start with a list of prominent employes of UVA, and VCU's president Michael Rao
#names = ['Tony Bennett', 'James E Ryan', 'Bronco Mendenhall', 'Carla Williams', 'Scott C Beardsley', 'Craig Benson', 
#         'Ian Baucom', 'Michael Rao']
#
#formatted_names_of_important_people = []
#
##start with a little string formatting. I am formatting each name so I can insert it into the URL
#for important_person in names:
#    important_person = important_person.replace(' ', '-')
#    important_person = important_person.lower()
#    formatted_names_of_important_people.append(important_person)

source = requests.get(f'https://data.richmond.com/salaries/2018/state/university-of-virginia/tony-bennett')

soup = BeautifulSoup(source.text, 'html.parser')
main_box = soup.find("div", class_='pay')
salary = main_box.find('h2').text
        




 
