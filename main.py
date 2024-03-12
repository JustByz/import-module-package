import datetime
from tqdm import tqdm 
from application.db.people import get_employees
from application.salary import calculate_salary


for i in tqdm(range(10000)):
    pass


if __name__ == '__main__':
    print(datetime.date.today())
    print(calculate_salary())
    print(get_employees())