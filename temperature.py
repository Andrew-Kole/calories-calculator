import requests
from selectorlib import Extractor


class Temperature:
    """
    Represents temperature extracted from timeanddate.com/weather webpage.
    """

    def __init__(self, country, city):
        self.country = country
        self.city = city

    @property
    def get(self):
        h = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
        r = requests.get(f'https://www.timeanddate.com/weather/'
                         f'{self.country.lower().replace(" ", "-")}/'
                         f'{self.city.lower().replace(" ", "-")}',
                         headers=h)
        content = r.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        extracted = extractor.extract(content)
        if extracted['temp'] is not None and extracted['temp'] != 'N/A':
            result = float(extracted['temp'].replace('\xa0°C', ''))
            return result
        else:
            return None


temperature = Temperature("Ukraine", "Odesa")
print(temperature.get)
