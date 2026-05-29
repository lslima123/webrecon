import json

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def banner():
    console.print(
        Panel.fit(
            "[bold cyan]WebRecon[/bold cyan]\n"
            "[dim]Lightweight Web Reconnaissance Framework[/dim]",
            border_style="cyan"
        )
    )


def show_headers(headers):
    console.print("\n[bold green]HTTP Information[/bold green]\n")

    console.print(f"[cyan][+][/cyan] Status Code : {headers.get('status_code')}")
    console.print(f"[cyan][+][/cyan] Server      : {headers.get('server')}")
    console.print(f"[cyan][+][/cyan] Powered By  : {headers.get('powered_by')}")


def show_table(title, items):
    if not items:
        return

    table = Table(title=title)

    table.add_column("Status", style="green")
    table.add_column("Path", style="white")

    for item in items:
        table.add_row(
            str(item["status"]),
            item["path"]
        )

    console.print()
    console.print(table)


def show_summary(results):
    total = 0

    for module in results.values():
        data = module.get("data")

        if isinstance(data, list):
            total += len(data)

    console.print(
        f"\n[bold yellow][!][/bold yellow] Total Findings: {total}"
    )


def show_report(data):
    banner()

    console.print(f"\n[bold]Target:[/bold] {data['target']}")

    results = data["results"]

    headers = results.get("headers", {}).get("data", {})
    discovery = results.get("discovery", {}).get("data", [])
    bruteforce = results.get("bruteforce", {}).get("data", [])

    show_headers(headers)

    show_table("Endpoint Discovery", discovery)

    show_table("Bruteforce Discovery", bruteforce)

    show_summary(results)


def save_json(data, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
