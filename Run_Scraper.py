# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:49:54 2022

@author: gorke
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/gorke/Desktop/Portfolio/ds_salary_project/chromedriver.exe"

df = gs.get_jobs('data scientist',5, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

