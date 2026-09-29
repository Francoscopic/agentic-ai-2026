import requests
import httpx

def get_public_ip_info():
    url = "https://api.ipify.org?format=json"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status() # raises HTTPError on 4xx/5xx
        return resp.json()
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None

def get_public_ip_info2():
    url = "https://api.ipify.org?format=json"
    with httpx.Client(timeout=5) as client:
        resp = client.get(url)
        resp.raise_for_status() # raises HTTPError on 4xx/5xx
        return resp.json()

if __name__ == "__main__":
    data = get_public_ip_info()
    print(data)
    data = get_public_ip_info2()
    print(data)