import requests
import time
import sys

def progress_bar(sent, total, bar_length=30):
    filled = int(bar_length * sent / total)
    bar = "█" * filled + "-" * (bar_length - filled)
    percent = (sent / total) * 100
    print(f"\r[{bar}] {sent}/{total} Requests ({percent:.1f}%)", end="")

def send_requests():
    url = input("URL eingeben: ").strip()
    total_requests = int(input("Wie viele Requests senden? "))

    sent_requests = 0
    success = 0
    failed = 0

    print("\nStarte Requests...\n")

    for i in range(total_requests):
        try:
            r = requests.get(url, timeout=5)
            success += 1
        except:
            failed += 1

        sent_requests += 1
        progress_bar(sent_requests, total_requests)
        time.sleep(0.0005)  # kleine Pause für sauberes Testing

    print("\n\n✅ Fertig!")
    print(f"Gesendet: {sent_requests}")
    print(f"Erfolgreich: {success}")
    print(f"Fehlgeschlagen: {failed}")

def main():
    while True:
        send_requests()
        restart = input("\nNochmal starten? (y/n): ").lower()
        if restart != "y":
            print("Beendet.")
            sys.exit()

if __name__ == "__main__":
    main()
