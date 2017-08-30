'''
This program counts the thursdays in an given month and outputs the number to a user

'''

#allows me to run it from the comand line
import sys
#allows python to recognize dates
import datetime


def main(year, month):
    try:
        # dictonary indicates how many days there are in each month
        dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day = 1
        thurs_count = 0
        #while loop that counts thursdays each month
        while day <= dict[int(month)]:
            weekday = datetime.date(year, month, day).weekday()
            if weekday == 3:
                thurs_count += 1
            day += 1
        year = str(year)
        month = str(month)
        thurs_count = str(thurs_count)
        output = (thurs_count, month, year)
        output = str(output)
        #writes the number of thursdays to a output file
        with open('month_length.txt', 'w') as file:
            file.write(output)
    except:
        print("your year or month values were not valid, please try again")

# declares the main function
if __name__ == "__main__":
    main(int(sys.argv[1]),int(sys.argv[2]))


