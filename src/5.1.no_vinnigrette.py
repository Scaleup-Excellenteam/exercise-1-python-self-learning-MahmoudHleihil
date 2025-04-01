import random
import datetime

"""
This module contains a function to generate a random date between two given dates.
"""
def no_vinnigrete(start: str, end: str):
    """
    Takes two dates in the format YYYY-MM-DD and returns a random date between them.
    """
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
    random_days = random.randint(0, (end_date - start_date).days)
    chosen_date = start_date + datetime.timedelta(days=random_days)
    print(chosen_date.strftime("%Y-%m-%d"))
    if chosen_date.weekday() == 0:  # 0 represents Monday
        print("I have no vinaigrette!")


if __name__ == '__main__':
    # Example usage
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    no_vinnigrete(start_date, end_date)
