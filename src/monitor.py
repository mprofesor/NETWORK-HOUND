# \              \
# \\\ MONITOR.PY \\\  Terminalowe monitorowanie hostów (pingowanie)
# \  \           \  \

import asyncio
import logging
from ping3 import ping
from utils import load_targets, log_status
from config import *
import socket
from network_mapper import scan_network, print_network, build_graph
from targets_manager import update_targets_from_scan


# Co tu się dzieje:

    # Funkcja przyjmuje host (czyli IP albo hostname w formie tekstu).
    # await asyncio.to_thread(...) — uruchamia funkcję ping() w osobnym wątku (żeby nie blokować całego programu na czas oczekiwania pinga).
    # ping(host, timeout=TIMEOUT) — wysyła żądanie ECHO do hosta z ustawionym timeoutem.
    # Jeśli response jest nie-None (czyli host odpowiedział), zwraca True.
    # Jeśli response == None lub jest błąd — zwraca False.
    # Jeżeli coś pójdzie nie tak (np. błędny adres) — złapie wyjątek i zapisze go do logu.

async def ping_host(host: str) -> bool:
    try:
        # Run ping in a separate thread
        response = await asyncio.to_thread(ping, host, timeout=TIMEOUT)
        
        # Check if the response is None (ping failed)
        if response is None:
            logging.error(f"Ping to {host} failed: Timeout or unreachable")
            return False
        
        # If response is False, this is another form of failure
        if response is False:
            logging.error(f"Ping to {host} failed: Ping response was False")
            return False

        # Successful ping, log RTT
        logging.info(f"Ping to {host} successful, RTT: {response} ms")
        return True
        
    except socket.timeout:
        logging.error(f"Ping to {host} failed: Timeout occurred")
        return False
    except socket.gaierror:
        logging.error(f"Ping to {host} failed: DNS resolution error")
        return False
    except Exception as e:
        logging.error(f"Unexpected error pinging {host}: {e}")
        return False


# Co tu się dzieje:

 # Funkcja dostaje listę hosts (np. ['192.168.1.1', 'google.com']).
    # while True: — nieskończona pętla: cały czas pingujemy co określony czas.
    # tasks = [ping_host(host) for host in hosts] — dla każdego hosta tworzy zadanie pingowania.
    # await asyncio.gather(*tasks) — czeka aż wszystkie pingi się zakończą jednocześnie.
    # Dla każdego hosta i wyniku:
       # log_status() — zapisujemy do loga (utils.py).
       # print() — wyświetlamy wynik w terminalu: [OK] lub [FAIL].
    # Na koniec robimy pauzę na PING_INTERVAL sekund przed kolejną turą.

async def monitor_hosts(hosts: list):
    while True:
        tasks = [ping_host(host) for host in hosts]
        results = await asyncio.gather(*tasks)
        #print(results) # debug

        for host, status in zip(hosts, results):
            #log_status(host, status)
            #print (status) # debug
            print(f"[{'OK' if status else 'FAIL'}] {host}")

        await asyncio.sleep(PING_INTERVAL)

#Co tu się dzieje:

  # Konfigurujemy system logowania:
   #    Wszystko zapisuje się do pliku logs/monitor.log.
   #    Format loga: czas + poziom błędu + wiadomość.
   # load_targets('targets.txt') — ładuje listę hostów do monitorowania z pliku.
   # Jeśli nie ma hostów → wypisz ostrzeżenie i wyjdź.
    # Jeśli są hosty:
     #   Poinformuj użytkownika, ile hostów jest monitorowanych.
     #   Uruchom monitor_hosts() asynchronicznie (asyncio.run(...)).

def main():
    devices = scan_network('192.168.0.1/24')
    print_network(devices)
    build_graph(devices)

    new_targets = update_targets_from_scan(devices)


    # Podmianka ścieżki dynamicznie
    if new_targets:
        targets = new_targets  # <-- Ładujemy zaktualizowane targets!
    else:
        targets = TARGETS_FILE # Standardowo

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    hosts = load_targets(targets)
    if not hosts:
        print("No hosts to monitor. Please check targets.txt")
        return
    
    print(f"Monitoring {len(hosts)} hosts every {PING_INTERVAL} seconds...")

    asyncio.run(monitor_hosts(hosts))


if __name__ == "__main__":
    main()

