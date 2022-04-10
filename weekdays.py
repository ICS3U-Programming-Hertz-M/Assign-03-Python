#!/usr/bin/env python3
# Created by Hertz Antonella
# Created 10 April 2022
# This is a programs compares user number to the 7 days of the week


user_numb = input("Enter a number representing days of the week:")

# Ask the user to enter a week bumber

user_numb = int(user_numb)

# Check the user number  and display the output


def find_weekday(weekday):
    weekdays = {
        1: "{} is monday.".format(weekday),
        2: "{} is tuesday.".format(weekday),
        3: "{} is wednesday.".format(weekday),
        4: "{} is Thursday.".format(weekday),
        5: "{} is Friday.".format(weekday),
        6: "{} is saturday.".format(weekday),
        7: "{} is sunday.".format(weekday),

    }
    return weekdays.get(weekday, "Error.{} is not a weekday number".
                        format(weekday))


if __name__ == "__main__":
    print(find_weekday(user_numb))
    print("play again")
