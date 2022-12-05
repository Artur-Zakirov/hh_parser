import requests
from bs4 import BeautifulSoup
import json
import re


class HH_parser:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_vacations(self):
        url = self.url
        headers = self.headers
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')
        last_page = int(soup.find_all('a', class_='bloko-button')[-2].text)
        vacations_info = {'items': []}

        for page in range(last_page):
            page_url = f'{url}&page={page}&hhtmFrom=vacancy_search_list'
            response = requests.get(page_url, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')
            vacations = soup.find_all('div', class_='vacancy-serp-item-body__main-info')
            for vacation in vacations:
                city = vacation.find_all('div', class_='bloko-text')[-1]
                company = vacation.find_all('a', class_='bloko-link bloko-link_kind-tertiary')[0].text
                link = vacation.find_all('a', class_='serp-item__title')[0]
                salary = vacation.find_all('span', class_='bloko-header-section-3')
                if "," in city.text:
                    i = city.text.index(',')
                    city = city.text[:i]
                else:
                    city = city.text
                if not salary:
                    salary = '-'
                else:
                    salary = salary[0].text
                    salary = re.sub(r'\s+', ' ', salary)
                company = re.sub(r'\s+', ' ', company)

                if 'django' in link.text.lower() or 'flask' in link.text.lower():
                    vacation_info = {'link': link["href"], 'salary': salary, 'company': company, 'city': city}
                    vacations_info['items'].append(vacation_info)
                    print(f'{link.text}, {link["href"]}, {salary}, {company}, {city}')
        return vacations_info

    def write_json(self, vacations_file_name):
        vacations_info = self.get_vacations()
        with open(vacations_file_name, mode="w", encoding='utf-8') as json_file:
            json.dump(vacations_info, json_file, indent=4, ensure_ascii=False)
