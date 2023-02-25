import dataclasses as dc


@dc.dataclass
class TableDataRecord:

    first_name: str
    last_name: str
    patronymic: str
    date_birth: str
    date_death: str
    note: str
