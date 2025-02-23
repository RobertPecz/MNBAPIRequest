from datetime import datetime

import pandas as pd


class ExcelConverter:
    def __init__(self, api_data):
        self.api_data = api_data

    # Check whether an excel file is exist in the folder.
    def is_excel_file_exist(self):
        try:
            pd.ExcelFile("output.xlsx")
            return True
        except FileNotFoundError:
            print("The output.xlsx file not found, creating a new file")
            return False

    # Writing the data from the soap response into an excel file sheet.
    def excel_file_writer(self):
        df = pd.DataFrame(self.api_data)

        is_file_exist = self.is_excel_file_exist()
        if is_file_exist:
            with pd.ExcelWriter(
                path="output.xlsx", if_sheet_exists="new", mode="a", engine="openpyxl"
            ) as writer:
                df.to_excel(
                    writer,
                    index=False,
                    sheet_name=str(str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))),
                )
        else:
            with pd.ExcelWriter(path="output.xlsx", engine="openpyxl") as writer:
                df.to_excel(
                    writer,
                    index=False,
                    sheet_name=str(str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))),
                )
