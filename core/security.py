def analyze_security_headers(headers):
    """
    Analisa headers HTTP de segurança e retorna presença/ausência.
    Não faz I/O, apenas processamento de dados.
    """

    SECURITY_HEADERS = {
        "Content-Security-Policy": {
            "severity": "HIGH",
            "description": "Prevents XSS and injection attacks"
        },
        "X-Frame-Options": {
            "severity": "HIGH",
            "description": "Prevents clickjacking attacks"
        },
        "Strict-Transport-Security": {
            "severity": "HIGH",
            "description": "Forces HTTPS usage (HSTS)"
        },
        "X-Content-Type-Options": {
            "severity": "MEDIUM",
            "description": "Prevents MIME type sniffing"
        },
        "Referrer-Policy": {
            "severity": "LOW",
            "description": "Controls referrer leakage"
        }
    }

    present = []
    missing = []

    for header, meta in SECURITY_HEADERS.items():
        if header in headers:
            present.append({
                "header": header,
                "severity": meta["severity"],
                "description": meta["description"],
                "value": headers.get(header)
            })
        else:
            missing.append({
                "header": header,
                "severity": meta["severity"],
                "description": meta["description"]
            })

    return {
        "present": present,
        "missing": missing
    }
