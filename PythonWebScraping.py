#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:57:11 2020

@author: ep9k
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


source = requests.get(f'https://data.richmond.com/salaries/2018/state/university-of-virginia/tony-bennett')

soup = BeautifulSoup(source.text, 'html.parser')

container = soup.find_all("div", class_='container')    #class_, because 'class' is a reserved word in python

container = container[1]

job_title = container.find_all('span', class_='small text-muted')

#row_12 = container.find_all('div', class_='row col-12')
#
#col_12_lg_8 = row_12[0].find_all('div', class_='col-12 col-lg-8')
#
#job_title = col_12_lg_8[0].find('span', class_='small text-muted')
#
#job_title = job_title.text
#
#print(job_title)













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




##Start with a list of prominent employees at UVA
#names = ['Tony Bennett', 'James E Ryan', 'Bronco Mendenhall', 'Carla Williams', 'Scott C Beardsley', 'Craig Benson', 'Ian Baucom']

#names = ['Tony Bennett']
#
#formatted_names_of_important_people = []
#
##start with a little string formatting. I am formatting each name so I can insert it into the URL
#for important_person in names:
#    important_person = important_person.replace(' ', '-')
#    important_person = important_person.lower()
#    formatted_names_of_important_people.append(important_person)
#
##using f strings to insert name into source URL
#
##for name in formatted_names_of_important_people:
##    print(name)
##    source = requests.get(f'https://data.richmond.com/salaries/2018/state/university-of-virginia/{name}')
##    soup = BeautifulSoup(source.text, 'html.parser')
##
##    main_box = soup.find("div", class_='pay')
##    salary = main_box.find('h2').text
##    
##    print(salary)
#    
#
#####START HERE. FIND JOB (ex: Basketball coach) in class 'small text-muted'
#for name in formatted_names_of_important_people:
#    source = requests.get(f'https://data.richmond.com/salaries/2018/state/university-of-virginia/{name}')
#    soup = BeautifulSoup(source.text, 'html.parser')
#
#    main_box = soup.find_all("div", class_='col-12 col-lg-8')
#    test = main_box[0].find('b', class_='small text-muted')
#    print(test)

    
    
 
