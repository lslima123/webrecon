import requests

def run(target):
    try:
        response = requests.get(target, timeout=5)

        return {
            "status_code": response.status_code,
            "server": response.headers.get("Server", "Unknown"),
            "powered_by": response.headers.get("X-Powered-By", "Unknown"),
        }

    except Exception as e:
        return {"error": str(e)}
