from typing import Dict

import openpyxl

from helper.dataProvider.ConfigFileReader import ConfigFileReader


class ExcelFileManager:
    _excel_file_path: str = None

    @classmethod
    def _init_file_path(cls):
        if cls._excel_file_path is None:
            config = ConfigFileReader()
            cls._excel_file_path = config.get_excel_path()

    @classmethod
    def read_excel_data(cls) -> Dict[str, str]:
        """Reads Excel data into a dictionary (key-value pairs)."""
        cls._init_file_path()
        data_map = {}

        try:
            workbook = openpyxl.load_workbook(cls._excel_file_path)
            sheet = workbook.active #Gets first sheet

            for row in sheet.iter_rows(values_only=True):
                if row and len(row) >= 2 and row[0] and row[1]: #skip empty rows/cells
                    key = str(row[0]).strip()
                    value = str(row[1]).strip()
                    data_map[key] = value

        except Exception as e:
            raise RuntimeError(f"Error reading Excel file {cls._excel_file_path}: {str(e)}")

        return data_map