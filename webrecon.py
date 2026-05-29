import argparse

from core.engine import ScanEngine

from core.headers import run as headers
from core.discovery import run as discovery
from core.bruteforce import run as bruteforce

from core.report import show_report, save_json


def main():
    parser = argparse.ArgumentParser(
        description="WebRecon - Web Reconnaissance Tool"
    )

    parser.add_argument(
        "target",
        help="Target URL"
    )

    parser.add_argument(
        "--wordlist",
        help="Wordlist file for bruteforce discovery",
        required=False
    )

    parser.add_argument(
        "--threads",
        help="Number of threads",
        type=int,
        default=10
    )

    args = parser.parse_args()

    # =========================
    # ENGINE
    # =========================

    engine = ScanEngine(args.target)

    engine.register("headers", headers)
    engine.register("discovery", discovery)

    # =========================
    # OPTIONAL BRUTEFORCE
    # =========================

    if args.wordlist:
        try:
            with open(args.wordlist, "r") as f:
                wordlist = f.readlines()

            engine.register(
                "bruteforce",
                bruteforce,
                {
                    "wordlist": wordlist,
                    "threads": args.threads
                }
            )

        except FileNotFoundError:
            print("[-] Wordlist file not found")

    # =========================
    # RUN
    # =========================

    result = engine.run()

    show_report(result)

    save_json(result)

    print("\n[+] JSON report saved as report.json")


if __name__ == "__main__":
    main()
