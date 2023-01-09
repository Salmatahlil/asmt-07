from datetime import datetime, date
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass




# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------


@dataclass
class Holiday:
    name: str
    date: datetime.date
    
    def __str__ (self):
        return (f'{self.name} ({self.date})')  

     
          

# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------

class HolidayList:
    def __init__(self):
        self.innerHolidays = []

    def addHoliday(self, holidayObj):
        type(holidayObj)
        if type(holidayObj) != Holiday:
            print('Sorry, This is not a Holiday')
            return
        self.innerHolidays.append(Holiday(holidayObj.name, holidayObj.date))
        print(f"Success! {holidayObj} is laready on the list, try a different holiday!")


    def findHoliday(self, HolidayName, Date):
        for i in self.innerHolidays:
            if i.name == HolidayName and i.Date == Date:
                print(f"Success! {i} is found!")
                return Holiday
            else:
                print("Sorry, that is not a holiday")

    def removeHoliday(self, HolidayName):
        holiday_remove = self.findHoliday(Holidayname, Date)
        if holiday_remove in self.innerHolidays:
            self.innerHoliday.remove(holiday_remove)
            print(f' Sucess: Holiday has been removed.')
        else:
            print(f' Error: That Holiday is not in the list, try again!')
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
    def read_json(self, filelocation):
        with open(filelocation) as f:
            data = json.load(f)
            print(data)
            for i in range(len(data)):
                new_holiday = Holiday(data[i]['name'], data[i]['date'])
                self.addHoliday(new_holiday)



    def save_to_json(self, filelocation):
            h_dict = {}
            listdict = []
            for i in self.innerHolidays:
                h_dict = {'name': i.name, 'date': i.date}
                listdict.append(h_dict)
            with open(saveloc, 'w') as file:
                json.dump(listdict, file, indent = 4)


        
#     def scrapeHolidays(self):
#         for i in range(2020, 2024):
#             response = requests.get(f'https://www.timeanddate.com/holidays/us/{year}')
#             soup = BeautifulSoup(response.text, 'html.parser')
#             table = soup.find('table', attrs = {'id':'holiday-table'})
#             tbody = soup.find('tbody')
        

    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return (len(self.innerHolidays))
    
    def filter_holidays_by_week(self, year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Cast filter results as list
        holidays = list(filter(lambda x: datetime.strptime(x.date, '%Y-%m-%d').isocalendar()[0] == int(year) and datetime.strptime(x.date, '%Y-%m-%d').isocalendar()[1] == int(week_number), self.innerHolidays))
        # return your holidays
        return holidays
        # Week number is part of the the Datetime object

    def displayHolidaysInWeek(self, holidayList):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        for i in holidayList:
            print(str(i))
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    #def getWeather(weekNum):
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek(self):
        # Use the Datetime Module to look up current week and year
        currentWeek = datetime.today().isocalendar().week
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        self.displayHolidaysInWeek(self.filter_holidays_by_week(datetime.today().year, currentWeek))
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results


def main():

    # 1. Initialize HolidayList Object
    initList = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    initList.read_json('holidays.json')
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
#     initList.scrapeHolidays()
    # 3. Create while loop for user to keep adding or working with the Calender
    mainmenu = True
    savedWork = False

    print("Welcome to Holiday Manager!")
    print("===================")
    print(f"There are {initList.numHolidays()} holidays stored in the system.")
 
    
    while mainmenu:
    # Display User Menu (Print the menu)
        print("Holiday Menu")
        print("===================")
        print("1. Add a Holiday")
        print("2. Remove a holiday")
        print("3. Save Holiday List")
        print("4. View Holidays")
        print("5. Exit")
        menu_option = int(input("Please type the menu option number you'd like to go to: "))
        if menu_option == 1:
            print("Add a Holiday")
            print("===================")
            holidayChoice = str(input("Holiday: "))
            dateChoice = input("Date (YYYY-MM-DD): ")
            initList.addHoliday(Holiday(holidayChoice, dateChoice))
        elif menu_option == 2:
            print("Remove a Holiday")
            print("===================")
            holidayNameChoice = str(input("Holiday Name: "))
            initList.removeHoliday(holidayNameChoice)
        elif menu_option == 3:
            print("Saving Holiday List")
            print("===================")
            wantSave = str(input("Save your changes? [Y/N]: "))
            if wantSave == "Y":
                initList.save_to_json(filelocation)
                print("Success! Your changes have been saved!")
                savedWork = True
            else:
                print("Changes were not saved.")
        elif menu_option == 4:
            print("View Holidays")
            print("===================")
            yearChoice = input("Which year?: ")
            weekChoice = input("Which week? [1-52, leave blank for current week]: ")
            if weekChoice == "":
                initList.viewCurrentWeek()
            else:
                print(f"These are the holidays for {yearChoice} week {weekChoice}:")
                initList.displayHolidaysInWeek(initList.filter_holidays_by_week(yearChoice, weekChoice))
        elif menu_option == 5:
            if savedWork == True:
                exitChoice = input("Are you sure you want to exit? [Y/N]: ")
                if exitChoice == 'Y':
                    print('Goodbye!')
                    break
                elif exitChoice == 'N':
                    continue
            elif savedWork == False:
                unsavedExitChoice = input("Are you sure you want to exit? Your changes will be lost! [Y/N]: ")
                if unsavedExitChoice == 'Y':
                    print("Goodbye!")
                    break
                elif unsavedExitChoice == 'N':
                    continue





           




    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main()




