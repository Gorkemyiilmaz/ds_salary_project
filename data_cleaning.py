# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 21:45:25 2022

@author: gorke
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')



#salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)


df = df[df['Salary Estimate'] != '-1'] #Removing the null values in Salary Estimate
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_KD = salary.apply(lambda x: x.replace('K','').replace('$',''))

minus_hr = minus_KD.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[-1]))
df['average_salary'] = (df.min_salary+df.max_salary)/2

#company name text only
df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field
df['Job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
#print(df.Job_state.value_counts()) -> to see how many jobs in each state

#age of company
df['company_age'] = df.Founded.apply(lambda x: x if x <1 else 2022 - x)

#parsing of job description (python, r studio, spark, powerbi, aws, excel)
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['rstudio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['powerbi_yn'] = df['Job Description'].apply(lambda x: 1 if 'powerbi' in x.lower() or 'power bi' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() or 'Amazon Web Services' in x.lower() else 0)
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)


df.to_csv('Salary_data_clean.csv')









