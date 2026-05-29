import requests
from concurrent.futures import ThreadPoolExecutor


def check_path(base_url, path):
    url = f"{base_url}/{path}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code in [200, 401, 403]:
            return {
                "path": f"/{path}",
                "status": response.status_code
            }

    except requests.RequestException:
        pass

    return None


def run(target, config=None):
    wordlist = config.get("wordlist", [])
    threads = config.get("threads", 10)

    if target.endswith("/"):
        target = target[:-1]

    found = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(
            lambda p: check_path(target, p.strip()),
            wordlist
        )

        for r in results:
            if r:
                found.append(r)

    return found
