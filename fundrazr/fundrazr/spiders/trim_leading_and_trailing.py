import csv
import pandas as pd
data = pd.read_csv('MonthDay_Year.csv')
data['goal']= data['goal'].str.strip("ofgoal")
data.to_csv('new.csv')
