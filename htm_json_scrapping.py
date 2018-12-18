#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 09:45:52 2018

Name : Reading tables from a web page.
Description : HTML table data from a webpage is loaded to JSON object using BeautifulSoup and further loaded and displayed in tabular form using PrettyTable library. 
Input : Provided the html page.
Output : Display the HTML table data in python.

@author: akshay
"""
import json
import bs4
import urllib.request
from prettytable import PrettyTable

response = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_districts_of_Uttarakhand")
html_doc = response.read()
soup = bs4.BeautifulSoup(html_doc, 'html.parser')
table = soup.find('table',attrs = {"class": 'wikitable sortable'})
headings = [th.find(text=True).replace("\n","") for th in table.find("tr").find_all("th")]
dataset = []
for row in table.find_all("tr")[1:]:
    dataset.append([td.find(text=True).replace("\n","") for td in row.find_all("td")])
print(headings)
final_data = []
with open('list_of_data.json', 'w') as File:
    for i in range(len(dataset)):
        data = {}
        for j in range(len(headings)):
            data[headings[j]] = dataset[i][j]
        final_data.append(data)


    json.dump(final_data, File)
    
with open('list_of_data.json', 'r') as File:
    file = json.load(File)

final_table = PrettyTable()

final_table.field_names = headings
for index in range(len(file)):
    final_table.add_row([file[index]["Code"], file[index]["District"], file[index]["Headquarters"], file[index]["Population (As of  2011"],
                   file[index]["Area (km²)"], file[index]["Density (/km²)"], file[index]["Division"], file[index]["Map"]])

print(final_table.get_string())
    