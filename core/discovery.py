import requests

COMMON_PATHS = [
    "/robots.txt",
    "/sitemap.xml",
    "/admin",
    "/login",
    "/wp-admin",
    "/backup",
    "/.git/",
    "/.env"
]

def run(base_url):
    if base_url.endswith("/"):
        base_url = base_url[:-1]

    found = []

    for path in COMMON_PATHS:
        url = base_url + path

        try:
            response = requests.get(url, timeout=5)

            if response.status_code in [200, 301, 302, 401, 403]:
                found.append({
                    "path": path,
                    "status": response.status_code
                })

        except requests.RequestException:
            continue

    return found
