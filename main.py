#  -----------------------------------------------
#  curriculum vitae:
#  https://apibot.josdanind.com/assets/show/cv.pdf
#  -----------------------------------------------

# Standard library
import re

# Pandas
import pandas as pd

# Environment Variables
from config import DATA_SOURCES, DATABASE_URL

# Database connect
from db import init_db

# Utils
from utils import get_data, process_data, locate_files

# get data and create directories
get_data(DATA_SOURCES)

# Return Engine and create tables
engine = init_db(DATABASE_URL)

path = "assets"
files_dir = locate_files(path)

# get the path of the most current files
files = [files_dir[file]["latest_file"] for file in files_dir.keys()]

# get dataframes with required fields
dataframes = [process_data(file) for file in files]

# Process data to create info table and main table data persistence - //start
columns = ["categoria", "provincia"]
rows = []

for df, file in zip(dataframes, files):
    for column in columns:
        d = {
            "cantidad": df[column].value_counts().size,
            "total_registros": df[column].shape,
            "archivo csv": re.search(r"\w+[0-9\-]+.csv", file).group(),
        }

        rows.append(pd.DataFrame(d, index={column}))

    df.to_sql("places", engine, if_exists="append", chunksize=500, index=False)
    df.to_sql("places", engine, if_exists="append", chunksize=500, index=False)

df_info = pd.concat(rows)
df_info.to_sql("info", engine, if_exists="replace")
# -// end
