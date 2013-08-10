"""
Module with different functions to format strings to have a standard in the
json file. 

"""

from datetime import date
from re import search

def format2date(day, month = None):
    """
    Returns a string formated like this: "day.month" as "25.07"

    """
    
    if month:
        return "%.2i.%.2i" %(int(day), int(month))
    
    else:
        day_month_list = day_and_month.split(search("\D",
                                                    day_and_month).group())

        return "%.2i.%.2i" %(int(day_month_list[0]), int(day_month_list[1]))




