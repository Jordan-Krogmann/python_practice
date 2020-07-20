
import pandas as pd
import os

from helper import search_string_in_file

df = pd.DataFrame()
files = os.walk(".")
for p, _, f_list in files:
    for file_name in f_list:
        if file_name.endswith(".js"):
            tmp_df = search_string_in_file(os.path.join(p, file_name), "banana")
            df = pd.concat([df,tmp_df])

df
