# proxy_helper.py
def get_current_proxy():
    try:
        with open('proxies.txt', 'r') as file:
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
