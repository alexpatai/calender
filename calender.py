from os import read
import pandas
from datetime import date, datetime
import re

calender_file = "FH-Kalender_02_2021.csv"
read_data = pandas.read_csv(calender_file, index_col='start_date')
read_data = read_data.drop(columns=["alarm","recur_type","recur_end_date","recur_interval","recur_data"])
#print(read_data)

today = date.today()
print("Today: ", today)

def upcoming_event(today, dataframe):
    ret = []
    for entry in dataframe.iterrows():
        row = entry[0]
        row_str = datetime.strptime(row, '%d.%m.%Y')
        row_str = datetime.date(row_str)
        before = row_str < today
        if before == False:
            entry_str = entry[1].astype('string')
            subject = [entry_str[0],entry_str[2], entry_str[5], entry_str[7], entry_str[6]]
            ret.append(subject)
    
    return ret


def print_subjects(subjects):
    for sub in subjects:
        print(sub)


def get_next_event(subjects, today):
    same_day = False
    if subjects[0][4] == subjects[1][4]:
        same_day = True
        print("Same day!")

    if same_day == True:
        return [subjects[0], subjects[1]]
        
    else:
        return subjects[0]


subjects_to_come = upcoming_event(today, read_data)
#print_subjects(subjects_to_come)
next = get_next_event(subjects_to_come, today)
print(next)
