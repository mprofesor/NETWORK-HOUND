# \            \
# \\\ UTILS.PY \\\  Wspólne funkcje pomocnicze
# \  \         \  \

import logging

def load_targets(filepath: str) -> list:
    """
    Wczytuje IP/hosty z pliku tekstowego.
    
    Args:
        filepath (str): Ścieżka do pliku tekstowego z listą hostów.

    Returns:
        list: Lista hostów jako stringi.
    """
    try:
        with open(filepath, 'r') as file:
            targets = [line.strip() for line in file if line.strip()]
        return targets
    except FileNotFoundError:
        logging.error(f"Targets file not found: {filepath}")
        return []
    except Exception as e:
        logging.error(f"Error reading targets file {filepath}: {e}")
        return []
    
def log_status(host: str, status: bool):
    """
    Zapisuje status hosta (UP/DOWN) do pliku logów.

    Args:
        host (str): IP lub hostname hosta.
        status (bool): True jeśli host odpowiada, False jeśli nie.
    """
    status_str = "UP" if status else "DOWN"
    logging.info(f"{host}" is {status_str})