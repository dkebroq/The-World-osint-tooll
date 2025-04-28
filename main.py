import phonenumbers
from phonenumbers import carrier, geocoder

def analyze_phone(phone):
    num = phonenumbers.parse(phone)
    print(f"Страна: {geocoder.description_for_number(num, 'ru')}")
    print(f"Оператор: {carrier.name_for_number(num, 'ru')}")

if __name__ == "__main__":
    analyze_phone("+79123456789")
