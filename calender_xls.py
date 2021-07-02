import pandas
from datetime import date, datetime
from crawler import *
from difflib import get_close_matches

calender_file = "Termine_02_07_2021.xls"
read_data = pandas.read_excel(calender_file)
read_data = read_data.drop(columns=["Anmerkung", "StundeVon", "StundeBis"])

today = date.today()
print("Today: ", today)


def events_to_come(dataframe, today_param):
    ret = []
    for entry in dataframe.iterrows():
        row = str(entry[1][0])
        row_str = datetime.strptime(row, '%d.%m.%Y')
        row_str = datetime.date(row_str)
        before = row_str < today_param
        if not before:
            entry_str = entry[1].astype('string')
            subject = [entry_str[0], entry_str[1], entry_str[2], entry_str[3], entry_str[6]]
            ret.append(subject)
    return ret


def print_subjects(subjects):
    for sub in subjects:
        print(sub)
        print("\n")


def get_next_event(subjects):
    same_day = False
    if subjects[0][0] == subjects[1][0]:
        same_day = True
    if same_day:
        return [subjects[0], subjects[1]]
    else:
        return subjects[0]


def correct_names(next_events_param):
    for event in next_events_param:
        if event[4] == "Object Oriented Programming Lab":
            event[4] = "Objektorientierte Paradigmen"
        elif event[4] == "Business English":
            event[4] = "Business English - Mittermaier"
        elif event[4] == "Objektorientierte Paradigmen":
            event[4] = "Objektorientierte Paradigmen"
    return next_events_param


def get_next_links(upcoming, pairs):
    ret = []
    upcoming_courses = []
    for elem in upcoming:
        upcoming_courses.append(elem[4])
    for pair in pairs:
        if get_close_matches(pair["Name"], upcoming_courses, cutoff=0.6):
            ret.append(pair)
    return ret


def place_course_details_into_dataset(next_event, pairs):
    for elem in pairs:
        for n in next_event:
            found = str(elem["Name"]).find(n[4])
            if found != -1:
                elem["Name"] = n
    return pairs


subjects_to_come = events_to_come(read_data, today)
subjects_to_come = correct_names(subjects_to_come)
next_events = get_next_event(subjects_to_come)
next_events = correct_names(next_events)
driver = login()
course_list = get_course_ids(driver)
links = provide_course_link(driver)
dicts = get_course_name_from_link(driver, links)
set_of_events = get_next_links(next_events, dicts)
set_of_events = place_course_details_into_dataset(next_events, set_of_events)
print_subjects(set_of_events)
driver.close()
