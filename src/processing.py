def filter_by_state(records_to_filter: list[dict], state: str = 'EXECUTED') -> list:
    """Отфильтровать список словарей по полю 'state'"""
    result = []
    for item in records_to_filter:
        if item['state'] == state:
            result.append(item)
    return result


def sort_by_date(records_to_sort: list, reverse: bool = True) -> list:
    """Отсортировать записи в заданном порядке по полю 'date'"""
    result = sorted(records_to_sort, key=lambda x: x['date'], reverse=reverse)
    return result
