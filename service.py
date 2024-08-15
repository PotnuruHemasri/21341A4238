import requests
from storage import Storage

class AverageCalculator:
    def __init__(self, window_size):
        self.window_size = window_size
        self.storage = Storage()

    def process_request(self, type):
        url = self.get_url_for_type(type)
        print(f"Requesting URL: {url}")  # Debugging line
        response = requests.get(url)
        
        if response.status_code == 404:
            return {"error": "Endpoint not found"}, 404
        
        numbers = response.json().get('numbers', [])
        self.storage.update_window(numbers)
        avg = self.storage.calculate_average()

        return {
            "windowPrevState": self.storage.get_previous_state(),
            "windowCurrState": self.storage.get_current_state(),
            "numbers": self.storage.get_current_numbers(),
            "avg": avg
        }

    def get_url_for_type(self, type):
        base_url = 'http://20.244.56.144/test/'
        urls = {
            'p': 'primes',
            'f': 'fibo',
            'e': 'even',
            'r': 'rand'
        }
        return base_url + urls.get(type, '')
