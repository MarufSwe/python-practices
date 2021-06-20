import datetime
print(datetime.datetime.today()) #todays date & time
print(datetime.date.today())  #todays time
print(dir(datetime))

maruf = datetime.date(1995, 7, 12)  #Birth day of mine
print(maruf.day)
print(maruf.strftime("%A, %B, %d, %Y")) # %A = day name, %B = Month name, %d = date, %Y = year name

message = "Maruf was born on: {:%A, %B, %d, %Y}."
print(message.format(maruf))


print("==============Date, Time, DateTime================")

birth_date = datetime.date(1995, 7, 12)  # year, month, date
birth_time = datetime.time(10, 30, 59)  # hours, minutes, seconds
married_time = datetime.datetime(2021, 7, 12, 10, 30, 59)

print('Maruf Born Date is: ',birth_date)
print('Maruf Born Time is: ',birth_time)
print('Maruf Married Date & Time is: ',married_time)
print('Maruf Married Year   is: ',married_time.year)


print("==============Convert String to Datetime================")

my_birthday = "12/07/1995"
string_convert_datetime = datetime.datetime.strptime(my_birthday, "%m/%d/%Y")
print(string_convert_datetime)