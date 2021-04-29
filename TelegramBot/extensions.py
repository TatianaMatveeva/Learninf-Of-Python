import requests
import json
from config import money


class ConvertionException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base = money[base.lower()]
        except KeyError:
            raise ConvertionException(f"Валюта {base} не найдена!")

        try:
            base_formatted = money[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            quote_formatted = money[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        if base_formatted == quote_formatted:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f"https://api.exchangeratesapi.io/latest?base={base_formatted}&symbols={quote_formatted}")
        resp = json.loads(r.content)
        new_price = resp['rates'][quote_formatted] * amount
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {quote} : {new_price}"
        return message
