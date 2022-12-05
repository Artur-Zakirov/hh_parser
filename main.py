from web.hh_classes import HH_parser


if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'
    }
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
    file_name = 'new_vacations.json'
    hh_parser = HH_parser(url=url, headers=headers)
    hh_parser.write_json(file_name)
