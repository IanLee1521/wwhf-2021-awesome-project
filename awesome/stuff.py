import requests


def get_page_size(url):
    print(f"querying url: {url}")
    response = requests.get(url)

    print(f"Got status code: {response.status_code}")
    print(f"Page html is {len(response.text)} characters long")


def demo():
    get_page_size("https://wildwesthackinfest.com")
