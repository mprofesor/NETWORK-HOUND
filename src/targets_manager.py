import os

def update_targets_from_scan(devices, config_path='src/config.py'):
    if not devices:
        print("[INFO] Nie znaleziono żadnych urządzeń w sieci.")
        return

    print("\n[INFO] Znaleziono urządzenia:")
    for device in devices:
        print(f"- {device['ip']} ({device['mac']})")
    
    choice = input("\nCzy chcesz monitorować znalezione hosty? [t/n]: ").strip().lower()
    
    if choice != 't':
        print("[INFO] Używamy istniejącego pliku targets.txt.")
        return

    new_file = input("Podaj nazwę nowego pliku targets (np.targets_new.txt): ").strip()

    if not new_file.endswith('.txt'):
        new_file += '.txt'

    # Zapisujemy nowe targety
    with open(new_file, 'w') as f:
        for device in devices:
            f.write(device['ip'] + '\n')

    print(f"[INFO] Zapisano {len(devices)} adresów do pliku {new_file}.")

    # Podmieniamy config.py
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            lines = file.readlines()

        new_targets_file = None

        with open(config_path, 'w') as file:
            for line in lines:
                if line.startswith('TARGETS_FILE'):
                    file.write(f"TARGETS_FILE = '{new_file}'\n")
                    print(new_file)
                    new_targets_file = new_file # < = ZAPAMIĘTUJEMY
                    print(new_targets_file)
                else:
                    file.write(line)

        print(f"[INFO] Podmieniono TARGETS_FILE w {config_path} na {new_file}.")

        # DYNAMICZNE WGRANIE NOWEGO PLIKU!
        return new_targets_file
    else:
        print(f"[WARN] Nie znaleziono pliku {config_path}.")