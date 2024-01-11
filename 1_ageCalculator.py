import time
class Person:
    def __init__(self, name, country, date, month, year):
        self.name = name
        self.country = country
        self.date = date
        self.month = month
        self.year = year


    def calculate_age(self):
        current_year, current_month, current_day = time.localtime()[:3]

        if (current_month, current_day) < (self.month, self.date):
            age_years = current_year - self.year - 1
            age_months = (current_month + 12) - self.month
        else:
            age_years = current_year - self.year
            age_months = current_month - self.month

        return age_years, age_months

def main():
# Declaring variables for error checking 
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    isLeap = False

# Asking for user input
    name = input("Enter name: ")
    country = input("Enter country: ")

# loop for checking errors in year input
    while True:
        year = int(input("Enter year of birth: "))
        if year > time.localtime().tm_year:
            print("Invalid Year")
        else:
            if (year % 4==0 and year % 100 !=0) or year % 400 == 0:
                isLeap = True
            break
        
# loop for checking errors in month input
    while True:
        month = int(input("Enter birth month number : "))
        if month in months:
            break
        else:
            print("Invalid month!")
    
# loop for checking errors in day input
    while True:
        day = int(input("Enter day of birth: "))
        if month in days_31:
            if day >= 1 and day <= 31:
                break
            else:
                print(f"Error: Month {month} doesn't have {day} days")
        elif month in days_30:
            if day >= 1 and day <= 30:
                break
            else:
                print(f"Error: {month} doesn't have {day} days")
        elif month == 2:
# conditional checking for february if it's a leap year or not
            if isLeap:
                if day >= 1 and day <= 29:
                    break
                else:
                    print(f"Error: February doesn't have {day} days")
            else:
                if day >=1 and day <=28:
                    break
                else:
                    print(f"Error: February doesn't have {day} days")
            
# creating object of Person class
    p2 = Person(name, country, day, month, year)
    print(f"Age: {p2.calculate_age()[0]} years, {p2.calculate_age()[1]} months")


# Running program only if it's the main program open
if __name__ == "__main__":
    main()