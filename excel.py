'''
Handles Excel document
'''
import pandas as pd

def get_xl(file, new_file):
    "Make Excel file ready for analysis"

    data = pd.read_excel(file, header=None)
    # If file has a header -> delete it.
    if (data.iloc[0, 0] == "Feedback" or data.iloc[0, 1] == "Score"
            or data.iloc[0, 2] == "Magnitude"):
        data = data.drop(data.index[0])
    # Delete all columns except 1st
    data = data.drop(data.iloc[:, 1:], axis=1)
    # Rename 1st column
    data.rename(columns={0: "Feedback"}, inplace=True)
    # Insert 2 more columns
    data.insert(1, "Score", True)
    data.insert(2, "Magnitude", True)
    # Drop rows(index) with any empty cells
    data.dropna(axis='index', inplace=True)
    # Create new excel file to store the results
    data.to_excel(new_file, index=None, header=True)
    data = pd.read_excel(new_file)

    return data, len(data.index)
