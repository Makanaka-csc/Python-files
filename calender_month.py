#Program  that accepts the name of a month and a year as input and prints out the calendar for that month
# Makanaka Mangwanda
# 03 April 2024

import math


def day_of_week(day, month, year):
    (d +[13*(m+1)/5]+y+[y/4]-[y/100]+[y/400])%7 
    return day_of_week
                     


def is_leap(year):
    if (year %100 ==0) or (year% 4 == 0 and year % 100 !=0):
        return True
    else:
        return False


def month_num(month_name):
    if month=='January':
        month ='1'
    if month=='February':
        month ='2'
    if month=='March':
        month ='3'
    if month=='April':
        month ='4'
    if month=='May':
        month ='5'
    if month=='June':
        month ='5'
    if month=='July':
        month ='7'
    if month=='August':
        month ='8'
    if month=='September':
        month ='9'
    if month=='October':
        month ='10'
    if month=='November':
        month ='11'
    if month=='December':
        month ='12'
        
    return month
    

def num_days_in(month_num, year):
    if month_num == '1':
        return 31
    if month_num =='2':
        if year==is_leap(year):
            return 29
        else:
            return 28
    if month_num=='3':
        return 31
    if month_num=='4':
        return 30
    if month_num=='5':
        return 31
    if mont_num=='6':
        return 30
    if month_num=='7':
        return 31
    if month_num=='8':
        month =31
    if month_num=='9':
        return 30
    if month_num=='10':
        return 30
    if month_num=='11':
        return 30
    if month_num=='12':
        return 31
        
    
    


def num_weeks(month_num, year):
    first_day == day_of_week(1,month,year)
    num_days == num_days_in(month_num,year)
    # get the number of weeks
    if (first_day + month_num-1)%7 == 0:
        return (first_day + month_num-1)//7
    else:
        return (first_day + month_num-1)//7+1
    
    


def week(week_num, start_day, days_in_month):
    
    
  


def main():
    month = input('Enter month:\n')
    year = input('Enter year:\n')


if __name__=='__main__':
    main()