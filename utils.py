import typing as t
from datetime import datetime

from natasha import DatesExtractor, MorphVocab, NamesExtractor


morph = MorphVocab()
names_extractor = NamesExtractor(morph)
dates_extractor = DatesExtractor(morph)
braces_re = r'[\(\)]'


def parse_date(source_dates: str) -> t.List[datetime]:
    """Parse dates in a string and return a list."""
    return [_.fact.as_json for _ in dates_extractor(source_dates)]


def parse_name(full_name: str) -> t.List[t.Dict[str, str]]:
    """Parse full name to first name, last name, partonymic."""
    return [_.fact.as_json for _ in names_extractor(full_name)]


def get_name(name: str) -> (str, str, str, str):
    """Get name and parse it to first_name , last_name, partonymic and notes."""
    names = parse_name(name)
    notes = []
    if len(names) != 1:
        notes.append('Check name.')
    try:
        name_dict = names[0]
    except IndexError:
        notes.append('Name not found.')
        name_dict = {}

    return name_dict.get('first'), name_dict.get('last'), name_dict.get('middle'), ', '.join(notes)


def get_dates(dates: str) -> ():
    """Get dates and return list of dates and notes."""
    notes = []
    dates = parse_date(dates)

    if len(dates) != 2:
        notes.append('Check dates.')

    try:
        date_birth, date_death = dates[0], dates[1]
    except IndexError:
        date_birth, date_death = {}, {}

    return (
        f'{date_birth.get("day")}-{date_birth.get("month")}-{date_birth.get("year")}',
        f'{date_death.get("day")}-{date_death.get("month")}-{date_death.get("year")}',
        ', '.join(notes),
    )
