# Standard library
import re, os

# Utils
from .get_data import Months

# Pandas
import pandas as pd

a, b = "áéíóúüñÁÉÍÓÚÜÑ", "aeiouunAEIOUUN"
trans = str.maketrans(a, b)

# required fields
fields = [
    "cod_localidad",
    "id_provincia",
    "id_departamento",
    "categoria",
    "provincia",
    "localidad",
    "nombre",
    "domicilio",
    "codigo postal",
    "numero telefono",
    "mail",
    "web",
]


def rename_columns(columns: list) -> list:
    for i, item in enumerate(columns):
        lower = item.lower().translate(trans)

        match lower:
            case "cod_loc":
                columns[i] = "cod_localidad"
            case "direccion":
                columns[i] = "domicilio"
            case "cp":
                columns[i] = "codigo_postal"
            case "telefono":
                columns[i] = "numero_telefono"
            case _:
                if re.match(r"^id", lower):
                    columns[i] = lower.replace("id", "id_")
                else:
                    columns[i] = lower

    return columns


# return a dataframe with the required fields
def process_data(path: str):
    df = pd.read_csv(path)
    columns = rename_columns(list(df.columns))
    df.columns = columns

    for column in columns:
        if not column in fields:
            df.drop([column], axis=1, inplace=True)

    return df


# return a dictionary with:
# the existing categories, their directories and subdirectories
# and their respective files
# also the path of the files to proccess (latest files)
def locate_files(path: str) -> list:
    dirs = os.walk(path)

    categories = {
        k: {"latest_file": f"{path}/{k}/", "history": {}} for k in next(dirs)[1]
    }

    for dir in dirs:
        category = re.search(r"/\w+$", dir[0])

        if category:
            name = category.group().replace("/", "")
            date_o = ""
            date_h = ""
            for k in dir[1]:
                date_o = k

                if not date_h:
                    date_h = k

                categories[name]["history"].update({k: []})

                v_o = date_o.split("-")
                v_h = date_h.split("-")

                if int(v_o[0]) > int(v_h[0]):
                    date_h = date_o

                if Months[v_o[1]].value > Months[v_h[1]].value:
                    date_h = date_o

            categories[name]["latest_file"] += date_h + "/"
            lastet_month = date_h

        files = dir[2]

        if files:
            month_year = re.search(r"\d+-\w+$", dir[0]).group()
            for file in files:
                categories[name]["history"][month_year].append(file)

            last_month = categories[name]["history"].get(lastet_month)

            if last_month:
                categories[name]["latest_file"] += last_month[-1]

    return categories
