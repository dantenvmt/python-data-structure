from datetime import date
import	pandas as pd
from os import path
class Appointment(object):
	def __init__(self,day,month,year,description):
		self.description=description
		self.date=date(year,month,day)
  
	def __unicode__(self):
		return self.description
      
	def occursOn(self,day,month,year):
		if self.date == date(year,month,day):
			return True
		else:
			return False
      
class Onetime(Appointment):
	def __init__(self,day,month,year,description):
		super(Onetime,self).__init__(day,month,year,description)
      
	def __unicode__(self):
		return self.description
      
      
class Daily(Appointment):
	def __init__(self,day,month,year,description):
		super(Daily,self).__init__(day,month,year,description)
      
	def __unicode__(self):
		return self.date.day, self.description,self.date.month, self.date.year

	def occursOn(self,day,month,year):
		return True
	def clear(self):
		del Daily
      
      
class Monthly(Appointment):
	def __init__(self,day,month,year,description):
		super(Monthly,self).__init__(day,month,year,description)
      
	def __unicode__(self):
		return self.description, self.day,self.month, self.year
      
   	
	def occursOn(self,day,month,year):
		if self.date.day == day:
			return True
		else:
			return False



      
appList = []
#daily
appList.append(Daily(1, 1, 2013, "general"))
appList.append(Daily(2, 1, 2013, "chiropractic"))
appList.append(Daily(3, 1, 2013, "pediatric"))
appList.append(Daily(4, 1, 2013, "heart"))
appList.append(Daily(5, 1, 2013, "gastro"))
#monthly
appList.append(Monthly(15, 12, 2012, "skin"))
appList.append(Monthly(16, 2, 2013, "osteo"))
appList.append(Monthly(17, 2, 2013, "heart"))
appList.append(Monthly(18, 2, 2013, "gastro"))
appList.append(Monthly(19, 2, 2013, "chiropractic"))
#onetime
appList.append(Onetime(15, 12, 2019, "chiropractic"))
appList.append(Onetime(5, 3, 2013, "general"))
appList.append(Onetime(7, 4, 2016, "gastro"))
appList.append(Onetime(1, 9, 2017, "heart"))
appList.append(Onetime(8, 3, 2014, "skin"))

def main():
    d = ''
    while d == '':
        print ('Choose one of the following:')
        print ('A. 	See all current Appointments')
        print ('B.	See all current Appointments on a given date')
        print ('C. 	Make a new Appointment')
        print ('D.	Cancel an existing Appointment')
        print ('E. 	See Appointments according to description')
        print ('F.	Reload Appointment data from a File')
        print ('G.	Exit the Program')
        option = input ('Please Enter Your Choice: ')
        if option.lower () == 'g':
            exit ()
        elif option.lower() == 'a':
            d = sub1()
        elif option.lower() == 'b':
            d = sub2()
        elif option.lower() == 'c':
            d = sub3()
        elif option.lower() == 'd':
            d = sub4() 
        elif option.lower() == 'e':
            d = sub5()
        elif option.lower() == 'f':
            d = sub6()               
        else:
            print ('Invalid selection!')
    return d
saved = "The file has been exported"
def sub1():
	a = []
	for app in appList:
		a.append([app.description, app.date, type(app).__name__])
	df = pd.DataFrame(a, columns = ['description', 'date','type'])
	print(df)
	option = input("Do you want to save it in a file? Y or N ")
	if option.lower() == 'y':
		filename = input("What's your file name? ")
		typ = input("txt or csv? ")
		df.to_csv(filename+"."+typ, index = False, header=True)
		print(saved)
		main()
	elif option.lower()== 'n':
		main()
	else:
		print('please input the right option')
		sub1()
def sub2():
	a = []
	day = int(input("Enter the day: "))
	month = int(input("Enter the month: "))
	year = int(input("Enter the year: "))
	for app in appList :
		if app.occursOn(day,month,year) :
			a.append([app.description, app.date, type(app).__name__])
	df = pd.DataFrame(a, columns = ['description', 'date','type'])
	print(df)
	option = input("Do you want to save it in a file? Y or N ")
	if option.lower() == 'y':
		filename = input("What's your file name? ")
		typ = input("txt or csv? ")
		df.to_csv(filename+"."+typ, index = False, header=True)
		print(saved)
		main()
	elif option.lower()== 'n':
		main()
	else:
		print('please input the right option')
		sub1()
def sub3():
	a = input('Please select the following type \nOnetime \nMonthly \nDaily \nor b to back to main menu \n')
	if a.lower() == 'onetime':
		day = int(input("Enter the day: "))
		month = int(input("Enter the month: "))
		year = int(input("Enter the year: "))
		description = str(input("Enter the description: "))
		appList.append(Onetime(day,month,year,description))
		main()
	elif a.lower() == 'monthly':
		day = int(input("Enter the day: "))
		month = int(input("Enter the month: "))
		year = int(input("Enter the year: "))
		description = str(input("Enter the description: "))
		appList.append(Monthly(day,month,year,description))
		main()
	elif a.lower() == 'daily':
		day = int(input("Enter the day: "))
		month = int(input("Enter the month: "))
		year = int(input("Enter the year: "))
		description = str(input("Enter the description: "))
		appList.append(Daily(day,month,year,description))
		main()
	elif a.lower() == 'b':
		main()
	else:
		print('please input the right option')
		sub3()
def sub4():
	day = int(input("Enter the day: "))
	month = int(input("Enter the month: "))
	year = int(input("Enter the year: "))
	a = input("An appointment will be removed, continue? Y or N or b to back " )
	if a.lower() == 'y':
		for app in appList:
			if app.date.year == year and app.date.month == month and app.date.day ==day:
				appList.remove(app)
	elif a.lower() == 'n':
		sub4()
	elif a.lower() == 'b':
		main()
	else:
		print("enter the right value")
		sub4()
	main()
def sub5():
	a = []
	description = input('Enter the description: ')
	for app in appList:
		if app.description.lower() == description.lower():
			a.append([app.description, app.date, type(app).__name__])
	df = pd.DataFrame(a, columns = ['description', 'date','type'])
	print(df)
	main()
def sub6():
	a = input("Enter the file name: ")
	if path.isfile(a):
		df = pd.read_csv(a)
		b = df.values.tolist()
		appList.clear()
		for i in range(len(b)):
			description = b[i][0]
			date = b[i][1]
			typ = b[i][2]
			new = date.split('-')
			year, month, day = new
			year = int(year)
			month = int(month)
			day = int(day)
			if typ.lower() =='daily':
				appList.append(Daily(day, month, year, description))
			elif typ.lower() =='monthly':
				appList.append(Monthly(day, month, year, description))
			elif typ.lower() =='onetime':
				appList.append(Onetime(day, month, year, description))
		print("File loaded sucessfully")
	else:
		print("wrong file name")
		sub6()
	main()
main()