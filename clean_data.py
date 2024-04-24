import pandas as pd


path = "Books_Data_Clean.xlsx"
df = pd.read_excel(path)

def CleanSpecialChars(column_name):
    clean_df = df[~df[column_name].str.contains(r'[^\x00-\x7F]', na=False)]
    clean_df.to_excel(path, index=False)

# CleanSpecialChars("Book Names")
CleanSpecialChars("Author")