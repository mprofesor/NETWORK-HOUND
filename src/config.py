# Stałe konfiguracyjne (np.interwał pingowania)

# monitor.py


# Czas w sekundach między kolejnymi pingami (starsza infrastruktura może wymagać zwiększenie parametru)
PING_INTERVAL = 10  

# Timeout dla pojedynczego pinga (większa sieć i starsza infrastruktura może wymagać zwiększenia parametru)
TIMEOUT = 2         

# Ścieżka do pliku z hostami do monitorowania
TARGETS_FILE = 'targets.txt'

# Ścieżka do pliku logów
LOG_FILE = 'logs/monitor.log'