# Standard library
import re, os
from datetime import datetime
from enum import Enum

# requests
import requests
from colorama import Fore, init

init(autoreset=True)


class Months(Enum):
    Enero = 1
    Febrero = 2
    Marzo = 3
    Abri = 4
    Mayo = 5
    Junio = 6
    Julio = 7
    Agosto = 8
    Septiembre = 9
    Octubre = 10
    Noviembre = 11
    Diciembre = 12


def get_data(urls: dict) -> None:
    today = datetime.now()
    year_month = f"{today.year}-{Months(today.month).name}"
    date = today.strftime("%d-%m-%Y")

    try:
        for url in urls:
            if url:
                category = re.search(r"\w+\.csv$", url).group().split("_")[0]
                dir = f"./assets/{category}/{year_month}"
                if not os.path.exists(dir):
                    os.makedirs(dir)
                response = requests.get(url, allow_redirects=True)
                open(f"{dir}/{category}-{date}.csv", "wb").write(response.content)
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "Failed to establish a connection with:")
        print(url)
