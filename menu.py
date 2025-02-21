import Api
import ExcelConverter


class Menu:

    def create_excel_data(self):
        api_handler = Api.APIHandler()
        api_data = api_handler.api_response_converter()
        excel_converter = ExcelConverter.ExcelConverter(api_data)
        excel_converter.excel_file_validator()
