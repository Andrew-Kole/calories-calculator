import requests
from selectorlib import Extractor


class Temperature:
    """
    Represents temperature extracted from timeanddate.com/weather webpage.
    """

    header = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://www.timeanddate.com/weather/'
    yaml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.lower().replace(' ', '-')
        self.city = city.lower().replace(' ', '-')

    def _build_url(self):
        """builds url for request"""
        url = f'{self.base_url}{self.country}/{self.city}'
        return url

    def _scrape(self):
        """makes request and get needed content"""
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yaml_path)
        r = requests.get(url, headers=self.header)
        all_content = r.text
        raw_content = extractor.extract(all_content)
        return raw_content

    def get_temperature(self):
        """Getting actual temperature"""
        extracted = self._scrape()
        if extracted['temp'] is not None and extracted['temp'] != 'N/A':
            result = float(extracted['temp'].replace('\xa0°C', '').strip())
            return result
        else:
            return None


if __name__ == '__main__':
    temperature = Temperature("Ukraine", "Odesa")
    print(temperature.get_temperature())
