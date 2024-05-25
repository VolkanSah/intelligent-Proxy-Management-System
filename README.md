# Proxy-Management-System
##### Rebuild 2024/05
A cool intelligent Proxy Management System for your Python scripts as SecurityAdmin / Hacker / Wardriver 

This project provides a way to manage and use proxies in your Python scripts without having to modify each script individually. It consists of a background script that selects a proxy from a list and saves it to a file, and a helper module that your scripts can use to retrieve the current proxy.

## Components

1. **`background_script.py`**: A script that runs in the background, selecting a random proxy from a list every few seconds.
2. **`proxy_helper.py`**: A module that provides functions to retrieve the current proxy.
3. **`main_script.py`**: An example script that demonstrates how to use the proxy helper module.
4. **`proxies.txt`**: A text file containing a list of proxies in the `ip:port` format.

## Setup

1. **Create the proxies list:**
   
   Create a file named `proxies.txt` in the same directory as your scripts. Add your proxies in the `ip:port` format, one per line e.g:
   ```
   192.168.1.1:8080
   192.168.1.2:8080
   192.168.1.3:8080
   ```
  ###### ^^This is only example IPs please use External Proxy IP:Ports! 
  
2. **Background Script:**

This script reads the proxies from `proxies.txt` and writes a randomly selected proxy to `current_proxy.txt` every 10 seconds.

```python
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

 ```
## Proxy Helper Module:

This module provides functions to get the current proxy.  
```python
# proxy_helper.py
def get_current_proxy():
    try:
        with open('current_proxy.txt', 'r') as file:
            proxy = file.read().strip()
        return proxy
    except FileNotFoundError:
        print("Proxy file not found.")
        return None

def get_proxies_dict():
    proxy = get_current_proxy()
    if proxy:
        return {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',
        }
    return None
 ```

### Example Script:

This script will use now the proxy_helper.py module to make a request using the current proxy.

```python
# main_script.py
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
```

## Usage

#### Start the background script:

```
      python background_script.py
```
#### Run your main script:

```
    python main_script.py
```
The background_script.py will run in the background, updating the current_proxy.txt file with a new proxy every 10 seconds. Your main script will read the current proxy from this file and use it for making requests.
Customization

    You can adjust the proxy selection interval by changing the time.sleep(10) line in background_script.py.
    Add more error handling as needed, especially for network requests in main_script.py.

## Copyright
- [VolkanSah on Github](https://github.com/volkansah)
- [Developer Site](https://volkansah.github.io)
- [Become a 'Sponsor'](https://github.com/sponsors/volkansah)
- [Source of this resposerity](https://github.com/VolkanSah/intelligent-Proxy-Management-System)
## License
This project is licensed under the MIT 

