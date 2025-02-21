import pandas as pd


class ExcelConverter:
    def __init__(self, api_data):
        self.api_data = api_data

    def excel_file_validator(self):
        df = pd.DataFrame(self.api_data)
        df.to_excel("output.xlsx", index=False, engine="openpyxl")
        # put new excel sheet


# import pandas as pd

# Create a DataFrame with some sample data
# data = {
#    'Date': ['2025-02-20', '2025-02-21', '2025-02-22'],
#    'Rate': [100, 105, 110]
# }

# df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
# df.to_excel('output.xlsx', index=False, engine='openpyxl')

# print("Excel file created successfully!")
