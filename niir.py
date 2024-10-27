import requests

phone_number = input("Введите номер телефона в формате 9031234567: ")
url = "https://www.niir.ru/bdpn/bdpn-proverka-nomera/"

payload = {
    'num': phone_number
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:
    try:
        # Attempt to parse JSON
        data = response.json()
        print("Number:", phone_number)
        print("Carrier:", data.get("operator"))
        print("City:", data.get("territory"))
        print("INN:", data.get("inn"))
    except requests.JSONDecodeError:
        # If JSON decoding fails, print the raw response text for debugging
        print("Received response is not JSON. Raw response text:", response.text)
else:
    print("Error request:", response.status_code)
