# Program to transform a date and time from 24-hour to 12-hour format
# Makanaka Mangwanda
# 18 March 2024

#get the input from the user
date_time =input('Enter the date and time (yyyy-mm-dd hh:mm):\n')

suffix = ''
month_l=''

#slice the input from user
year = date_time[ :4]
year = date_time[2:4]

date_time=date_time[5:]


month = date_time[:2]
date_time=date_time[3:]

day = date_time[0:2]

hours = date_time[3:5]

minutes = date_time[6:8]


#conbert hours to 12-hour formart   
hours = int(hours) 
if hours < 12:
    Time_of_day='am'
elif hours == 12:
    Time_of_day='pm'
else:
    Time_of_day='pm'
    hours>12
    hours %= 12
        
       

# month name  
if month=='01':
    month_l='January'
if month=='02':
    month_l='February'
if month=='03':
    month_l='March'
if month=='04':
    month_l='April'
if month=='05':
    month_l='May'
if month=='06':
    month_l='June'
if month=='07':
    month_l='July'
if month=='08':
    month_l='August'
if month=='09':
    month_l='September'
if month=='10':
    month_l='October'
if month=='11':
    month_l='November'
if month=='12':
    month_l='December'

# suffixes of the day
day = int(day)
if 4<=day<=20 or 24<=day<=30:
    suffix = 'th'
if day==1 or day==21 or day==31:
    suffix = 'st'
if day==2 or day==22:
    suffix = 'nd'
if day==3 or day==23:
    suffix = 'rd'

print(str(hours)+":"+minutes+" "+Time_of_day + " "'on the ' + str(day)+suffix +" "'of '+ month_l + " "+ "'"+year + " ")


