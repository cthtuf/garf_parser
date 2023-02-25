#@title GARF SNAPSHOT
import os

from xls import Worksheet
from garf import GARFSite

workbook_filename = os.getenv('XLS_FILENAME', 'list_add_on.xlsx')
worksheet_name = os.getenv('XLS_SHEET_NAME', 'Список личных дел')
garf_pages_limit = os.getenv('GARF_PAGES', 1)
garf_url = os.getenv('GARF_URL', 'http://opisi.garf.su/default.asp?base=garf&menu=2&v=5&node=151&fond=982&opis=3087&co=746055&cd=3024700&cp={page}')


def main():
    # Open workbook and create worksheet. It would be closed automatically
    with Worksheet(workbook_filename=workbook_filename, worksheet_name=worksheet_name) as worksheet:
        current_idx = 1
        # For each page on the GAFR site
        for garf_page in GARFSite(url=garf_url, pages_limit=garf_pages_limit):
            # For each row in the table on the page
            for record in garf_page:
                # Put row data to the worksheet
                worksheet.add_row(current_idx, record)
                print(f'Processed {record.__dict__}')
                current_idx += 1


if __name__ == '__main__':
    main()
