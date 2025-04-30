# NET-HOUND - network-discovery-monitor

NET-HOUND to program służący do skanowania i monitorowania sieci lokalnej.

## Widok projektu (struktura plików/folderów)

 network-monitor/\
│\
├── src/                          # Główne źródła kodu\
│   ├── monitor.py                # Terminalowe monitorowanie hostów (pingowanie)\
│   ├── network_mapper.py         # Skanowanie sieci (nmap)\
│   ├── network_visualizer.py     # Wizualizacja sieci (tekst/graf)\
│   ├── exporter.py               # Eksport do formatu GNS3/PT\
│   ├── utils.py                  # Wspólne funkcje pomocnicze\
│   └── config.py                 # Stałe konfiguracyjne (np. interwał pingowania)\
│\
├── logs/                         # Pliki logów\
│   └── monitor.log               # Log awarii (tworzony automatycznie)\
│\
├── targets.txt                   # Lista IP/hostname'ów do monitoringu (input)\
│\
├── requirements.txt              # Lista bibliotek do zainstalowania (pip)\
│\
├── README.md                     # Instrukcja projektu (opis działania, instalacji)\
│\
├── examples/                     # Przykładowe outputy, sample pliki, testowe sieci\
│   ├── sample_topology.json      # Przykład wyeksportowanej topologii\
│   ├── sample_targets.txt        # Przykład pliku targetów\
│\
└── setup.sh                      # Skrypt instalacyjny (setup, venv, pip install)\

## Opis folderów i plików

Ścieżka          | Co zawiera\
src/             | Wszystkie główne pliki źródłowe projektu (monitorowanie, mapowanie, eksportowanie).\
logs/            | Gromadzenie logów działania monitoringu (tworzone automatycznie).\
targets.txt      | Lista adresów do monitorowania.\
requirements.txt | Wszystkie wymagane biblioteki (ping3, nmap, networkx, itp.).\
examples/        | Przykładowe dane wejściowe/wyjściowe do testowania lub pokazywania w kursie.\
setup.sh         | Skrypt pomagający szybko postawić środowisko (np. dla użytkowników/kursantów).

