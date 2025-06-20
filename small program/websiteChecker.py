import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_website(csv_path : str)-> list[str]:
    websites : list[str]=[]
    with open(csv_path,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1] or 'http://' in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
        return websites


# test function reading file
#print(get_website('filename')) 
                
def get_user_agent()-> str:
    ua = UserAgent()
    return ua.chrome

#test function for borrower usage
#print(get_user_agent('filename'))


def get_status_description(statusCode: int) -> str:
     for vaule in HTTPStatus:
         if value = statusCode:
             description: str(f'({vaule} {vaule.name}) {vaule.description} ')
             return description
     return ' unknown code'
