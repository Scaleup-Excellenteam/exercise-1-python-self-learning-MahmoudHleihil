import random
import datetime

def random_date(start_date: str, end_date: str):
    """
    Takes two dates in the format YYYY-MM-DD and returns a random date between them.
    """
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    random_days = random.randint(0, (end - start).days)
    random_date = start + datetime.timedelta(days=random_days)
    
    print(random_date.strftime("%Y-%m-%d"))
    
    if random_date.weekday() == 0:  # 0 represents Monday
        print("I have no vinaigrette!")


if __name__ == '__main__':
    # Example usage
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    random_date(start_date, end_date)