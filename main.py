import random
import time
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_port():
    return random.randint(1, 65535)

def random_protocol():
    return random.choice(["TCP", "UDP", "ICMP"])

def generate_packet():
    return {
        "src_ip": random_ip(),
        "dst_ip": random_ip(),
        "src_port": random_port(),
        "dst_port": random.choice([22, 443, 80, 53, 25]),
        "protocol": random_protocol()
    }

def generate_packets(n):
    return [generate_packet() for _ in range(n)]

def display_packets(packets):
    table = Table(title="Generated Network Packets", box=box.ROUNDED, show_lines=True)
    table.add_column("No.", justify="center")
    table.add_column("Source IP", style="cyan")
    table.add_column("Destination IP", style="green")
    table.add_column("Src Port", justify="center")
    table.add_column("Dst Port", justify="center")
    table.add_column("Protocol", style="yellow")

    for i, p in enumerate(packets, start=1):
        table.add_row(str(i), p['src_ip'], p['dst_ip'], str(p['src_port']), str(p['dst_port']), p['protocol'])

    console.print(table)

def firewall_rules(packets):
    table = Table(title="Firewall Rule Results", box=box.ROUNDED, show_lines=True)
    table.add_column("Packet No.", justify="center")
    table.add_column("Decision", style="bold magenta")
    table.add_column("Reason", style="white")

    allowed = blocked = dropped = 0

    for i, p in enumerate(packets, start=1):
        if p['dst_port'] in (80, 443):
            if p['src_ip'] != '192.168.1.5':
                table.add_row(str(i), "[green]ALLOWED[/green]", f"Port {p['dst_port']} is allowed")
                allowed += 1
            else:
                table.add_row(str(i), "[red]BLOCKED[/red]", f"Blocked IP {p['src_ip']}")
                blocked += 1
        else:
            table.add_row(str(i), "[yellow]DROPPED[/yellow]", f"Port {p['dst_port']} not allowed")
            dropped += 1

    console.print(table)

    console.print(f"\n[bold green]Summary:[/bold green] {allowed} allowed, [red]{blocked} blocked[/red], [yellow]{dropped} dropped[/yellow]")

def save_log(packets):
    with open("firewall_log.txt", "a") as f:
        f.write(f"\n---- Log at {time.strftime('%Y-%m-%d %H:%M:%S')} ----\n")
        for p in packets:
            f.write(f"{p}\n")
    console.print("[cyan]\nLog saved to 'firewall_log.txt'[/cyan]\n")

def main():
    console.rule("[bold blue]Simple Packet Generator & Firewall Simulator[/bold blue]")

    # === Welcome + Continue/Exit prompt ===
    console.print("\n[bold green]Welcome to Basic Firewall Simulator[/bold green]")
    start_choice = console.input("\n[bold cyan]Press [b]C[/b] to Continue or [b]E[/b] to Exit: [/bold cyan]").strip().lower()
    if start_choice == "e":
        console.print("\n[red]Exiting. Goodbye![/red]")
        console.rule("[bold blue]Program Ended[/bold blue]")
        return
    elif start_choice != "c":
        console.print("\n[red]Invalid choice. Exiting.[/red]")
        console.rule("[bold blue]Program Ended[/bold blue]")
        return
    # === end Program ===

    try:
        n = int(console.input("\n[bold yellow]How many random packets you want to generate? [/bold yellow]"))
    except ValueError:
        console.print("[red]Invalid input! Please enter a number.[/red]")
        return

    console.print(f"\n[bold green]Generating {n} packets...[/bold green]")
    time.sleep(1)
    packets = generate_packets(n)
    display_packets(packets)

    choice = console.input("\n[bold cyan]Do you want to apply firewall rules? (y/n): [/bold cyan]").lower().strip()
    if choice == "y":
        console.print("\n[bold magenta]Applying firewall rules...[/bold magenta]\n")
        time.sleep(1)
        firewall_rules(packets)
        
        save_choice = console.input("\n[bold yellow]Save log to file? (y/n): [/bold yellow]").lower().strip()
        if save_choice == "y":
            save_log(packets)
    elif choice == "n":
        console.print("\n[green]Okay, exiting...[/green]")
    else:
        console.print("[red]Invalid choice. Please type 'y' or 'n'.[/red]")

    console.rule("[bold blue]Program Ended[/bold blue]")

if __name__ == "__main__":
    main()
