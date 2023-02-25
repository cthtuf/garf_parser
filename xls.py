import xlsxwriter

from models import TableDataRecord


class Worksheet:
    """Helper class to work with xls Workbook."""

    FIRST_NAME_IDX = 'A'
    LAST_NAME_IDX = 'B'
    PATRONYMIC_IDX = 'C'
    DATE_BIRTH_IDX = 'D'
    DATE_DEATH_IDX = 'E'
    NOTE_IDX = 'F'

    def __init__(self, workbook_filename, worksheet_name):
        """Init variables."""
        self.workbook_filename = workbook_filename
        self.worksheet_name = worksheet_name
        self.workbook = None
        self.worksheet = None

    def __enter__(self):
        """Open Workbook and create worksheet."""
        self.workbook = xlsxwriter.Workbook(self.workbook_filename)
        self.worksheet = self.workbook.add_worksheet(self.worksheet_name)
        return self

    def __exit__(self, *args, **kwargs):
        """Close workbook."""
        self.workbook.close()

    def add_row(self, row_index: int, record: TableDataRecord) -> None:
        """Add row to worksheet."""
        self.worksheet.write(f"{self.FIRST_NAME_IDX}{row_index}", record.first_name)
        self.worksheet.write(f"{self.LAST_NAME_IDX}{row_index}", record.last_name)
        self.worksheet.write(f"{self.PATRONYMIC_IDX}{row_index}", record.patronymic)
        self.worksheet.write(f"{self.DATE_BIRTH_IDX}{row_index}", str(record.date_birth))
        self.worksheet.write(f"{self.DATE_DEATH_IDX}{row_index}", str(record.date_death))
        self.worksheet.write(f"{self.NOTE_IDX}{row_index}", record.note)
