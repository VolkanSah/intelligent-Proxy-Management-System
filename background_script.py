# background_script.py
import os
import random
import time

def read_proxies(file_path):
    with open(file_path, 'r') as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies]

def select_random_proxy(proxies):
    return random.choice(proxies)

def main():
    proxy_file = 'proxies.txt'
    if not os.path.exists(proxy_file):
        print(f"Proxy file '{proxy_file}' not found.")
        return

    proxies = read_proxies(proxy_file)
    if not proxies:
        print("No proxies found in the file.")
        return

    while True:
        selected_proxy = select_random_proxy(proxies)
        with open('current_proxy.txt', 'w') as file:
            file.write(selected_proxy)
        time.sleep(10)  # Sleep for 10 seconds before selecting a new proxy

if __name__ == "__main__":
    main()
