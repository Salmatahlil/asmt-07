import datetime
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
    date: str
    
    def __str__ (self):
        return (f'{self.name} ({self.date})')

# obj = Holiday('salma', '2022-12-18')  
# print(obj)

# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
        self.innerHolidays = []
    
    def addHoliday(self, holidayObj):
        if type(holidayObj) != Holiday:
            print('Sorry, This is not a Holiday!')
            return 
        
        else:
            holidaylist = self.findHoliday(holidayObj.name, holidayObj.date)
            if holidaylist == False:
                self.innerHolidays.append(holidayObj)
                print(f' Success: {holidayObj} has been added to the holiday list!')
            else:
                print(f' Error: {holidayObj} is already on the list, try a different holiday!')          
        
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
    
    def findHoliday(self, HolidayName, Date):
        for i in self.innerHolidays:
            if i.name == Holidayname and i.date == Date:
                print(f'Success: {i} is found')
                return Holiday
            else:
                print(f' Sorry, that is not a Holiday!')
            
        # Find Holiday in innerHolidays
        # Return Holiday
    
    def removeHoliday(self, HolidayName, Date):
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
        with open(filelocation, 'r') as f:
            data = json.load(f)
            for i in data ['holidays']:
                new_holiday = Holiday(i['name'], i['date'])
                self.addHoliday(new_holiday)
            
            
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.
    
    def save_to_json(self, filelocation):
            h_dict = {}
            listdict = []
            for i in self.innerHolidays:
                h_dict = {'name': i.name, 'date': i.date}
                listdict.append(h_dict)
            with open(saveloc, 'w') as file:
                json.dump(listdict, file, indent = 4)
                 
#         with open(filelocation, 'w') as holidays.json:
#             temp = []
#             for i in self.innerHolidays:
#                 holiday = {'name': i.name, 'date': i.date}
#                 temp.append(holiday)
#                 json.dump(temp, holidays.json)
#                 holidays.json.write
# Write out json file to selected file.
# Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
# Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
# Check to see if name and date of holiday is in innerHolidays array
# Add non-duplicates to innerHolidays
# Handle any exceptions. 
    def scrapeHolidays():
        for i in range(2020, 2024):
            response = requests.get(f'https://www.timeanddate.com/holidays/us/{year}')
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', attrs = {'id':'holiday-table'})
            tbody = soup.find('tbody')
            
            # for row in body.final_all('tr'):
    
    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return len(self.innerHolidays)
    def filter_holidays_by_week(self, year, week_number):
        holidays = []
        holidays = list(filter)
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
    def displayHolidaysInWeek(self, holidayList):
        if len(holidayList) == None:
            print('No Holidays were found for that week.')
        else:
            for holiday in holidayList:
                print(holiday)
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

#    def getWeather(weekNum):
#         pass
#         # Convert weekNum to range between two days
#         # Use Try / Except to catch problems
#         # Query API for weather in that week range
#         # Format weather information and return weather string.

    def viewCurrentWeek(self):
        currentWeek = datetime.today().isocalendar().week
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        self.displayHolidaysInWeek(self.filter_holidays_by_week(datetime.today().year, currentweek))
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results

    def main():
        initList = HolidayList([])
        initList.scrapeHolidays()
        initList.read_json('holidays.json')

    print("Welcome to Holiday Manager! \n"\
      "============================")
    print(f' There are {len(initList.numHolidays)} Holidays stored in the system.')
    
    mainmenu = True
    saved = False
   
    while mainmenu:
          print(
        "Holiday Menu\n" \
        "================\n" \
        "1. Add a Holiday\n" \
        "2. Remove a Holiday\n" \
        "3. Save Holiday List\n" \
        "4. View Holidays\n" \
        "5. Exit\n"
    )
  
    menu_option = int(input('Enter the menu option you would like to go to: '))
  
    
    if menu_option == 1:
        print('Add a Holiday')
        holidayoption = str(input('Holiday: '))
        dateoption = input('Date (YYYY-MM-DD): ')
        initList.addHoliday(Holiday(holidayoption, dateoption))
    elif menu_option == 2:
        print('Remove a Holiday')
        holidayname = str(input('Holiday Name: '))
        initList.removeHoliday(holidayname)
    elif menu_option == 3:
        print("Save Holiday List")
        Save = str(input("Save your changes? [y/n]: "))
        if Save == "y":
            initList.save_to_json()
            print("Success! Your changes have been saved!")
            saved = True
        else:
            print("Changes were not saved.")
    elif menu_option == 4:
        print("View Holidays")
        yearoption = input("Which year?: ")
        weekoption = input("Which week? [1-52, leave blank for current week]: ")
        if weekoption == "":
            initList.viewCurrentWeek()
        else:
            print(f"These are the holidays for {yearoption} week {weekoption}:")
            initList.displayHolidaysInWeek(initList.filter_holidays_by_week(yearoption, weekoption))
    elif menu_option == 5:
        if saved == True:
            exit = input("Would you like to exit? [y/n]: ")
            if exit == 'y':
                print('Goodbye!')
                break
            elif exit == 'n':
                continue
        elif saved == False:
            unsavedExit = input("Would you like to exit? Your changes will be lost! [y/n]: ")
            if unsavedExit == 'y':
                print("Goodbye!")
                break
            elif unsavedExit == 'n':
                 continue



    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
   
    # 2. Load JSON file via HolidayList read_json function
   
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main()




