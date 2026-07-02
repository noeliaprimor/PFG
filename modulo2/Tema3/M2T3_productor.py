import json
import os
import time
from datetime import datetime, timezone

import requests


INPUT_DIR = os.path.abspath("input/crypto_prices")
COINS = ["bitcoin", "ethereum", "solana", "cardano"]
CURRENCY = "eur"
SLEEP_SECONDS = 15
MAX_ITERATIONS = 20


def main():
    os.makedirs(INPUT_DIR, exist_ok=True)
    print("Escribiendo en:", INPUT_DIR)

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(COINS), "vs_currencies": CURRENCY}
    iterations = MAX_ITERATIONS if MAX_ITERATIONS is not None else 10**9

    for i in range(iterations):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            event_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            filename = os.path.join(INPUT_DIR, f"crypto_{int(time.time())}.json")

            with open(filename, "w", encoding="utf-8") as file:
                for coin, values in data.items():
                    event = {
                        "event_time": event_time,
                        "coin": coin,
                        "currency": CURRENCY,
                        "price": float(values[CURRENCY]),
                    }
                    file.write(json.dumps(event) + "\n")

            print(f"[{i + 1}] Fichero generado: {filename}")
        except Exception as exc:
            print("Error consultando CoinGecko o escribiendo el fichero:", exc)

        time.sleep(SLEEP_SECONDS)


if __name__ == "__main__":
    main()
