import typing as t

import pandas as pd

from models import TableDataRecord
from utils import get_name, get_dates


class GARFPage:
    """Helper class to iterate and process rows on the GARF page."""

    DATABLOCK_IDX = 13
    NAMES_COL_IDX = 3
    DATES_COL_IDX = 4

    def __init__(self, data: t.List[pd.DataFrame]) -> None:
        self.datablock = data[self.DATABLOCK_IDX]
        self.names_col = self.datablock[self.NAMES_COL_IDX]
        self.dates_col = self.datablock[self.DATES_COL_IDX]
        self.rows_count = len(self.names_col)
        self.current_idx = 1

    def __iter__(self):
        """Iterate through all records on the page."""
        return self

    def _get_record(self, names: str, dates: str) -> TableDataRecord:
        """"""
        first_name, last_name, mid_name, name_note = '', '', '', ''
        date_birth, date_death, date_note = '', '', ''

        return TableDataRecord(
            first_name=first_name,
            last_name=last_name,
            patronymic=mid_name,
            date_birth=date_birth,
            date_death=date_death,
            note=', '.join((name_note, date_note))
        )

    def __next__(self) -> TableDataRecord:
        """Get the next row and convert it to TableDataRecord."""
        if self.current_idx < self.rows_count:
            record = self._get_record(
                names=self.names_col[self.current_idx-1],
                dates=self.dates_col[self.current_idx-1],
            )
            self.current_idx += 1
            return record

        raise StopIteration


class GARFSite:
    """Helper class to iterate through pages in the GARF site."""

    def __init__(self, url: str, pages_limit: int) -> None:
        self.pages_limit = pages_limit
        self.url = url
        self.idx = 1

    def _get_page(self, page_index: int) -> t.List[pd.DataFrame]:
        url = self.url.format(page=page_index)
        return pd.read_html(url)

    def __iter__(self):
        return self

    def __next__(self) -> GARFPage:
        while self.idx <= self.pages_limit+1:
            page = GARFPage(data=self._get_page(page_index=self.idx))
            self.idx += 1
            return page

        raise StopIteration
