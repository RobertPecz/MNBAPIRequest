from datetime import date

import logic.Api as Api
import logic.ExcelConverter as ExcelConverter


class Menu:

    # Calling the soap request and put the data from the response into the excel converter.
    def create_excel_data(self, start_date, end_date):
        if start_date > end_date:
            raise AttributeError("Start date can't be a later date than the end date.")
        elif start_date > str(date.today()):
            raise AttributeError("Today date can't be a future date.")
        api_handler = Api.APIHandler()
        api_data = api_handler.api_response_converter(start_date, end_date)

        excel_converter = ExcelConverter.ExcelConverter(api_data)
        excel_converter.excel_file_writer()
