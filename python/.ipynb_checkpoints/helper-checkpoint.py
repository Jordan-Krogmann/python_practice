#class string_help
import pandas as pd


def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""

    df = pd.DataFrame()
    #df.columns = ["file_name", "string_to_search", "line_number"]
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
                dic_results = {"file_name":file_name, "string_to_search":string_to_search, "line_number":line_number}
                df = df.append(dic_results, ignore_index = True)
                #print(dic_results)
                #print(type(dic_results))
                #print(df)
    # Return list of tuples containing line numbers and lines where string is found
    return df.copy()