import logic.Api as Api
import logic.ExcelConverter as ExcelConverter


class Menu:

    def create_excel_data(self, start_date, end_date):
        api_handler = Api.APIHandler()
        api_data = api_handler.api_response_converter(start_date, end_date)

        excel_converter = ExcelConverter.ExcelConverter(api_data)
        excel_converter.excel_file_validator()
