# main_script.py
# this is an example script
import requests
from proxy_helper import get_proxies_dict

def main():
    proxies = get_proxies_dict()
    if proxies:
        response = requests.get('http://example.com', proxies=proxies)
        print(response.text)
    else:
        print("No proxy found or proxy file is missing.")

if __name__ == "__main__":
    main()
