def filter_by_state(records_to_filter: list, state='EXECUTED')-> list:
    """Отфильтровать список словарей по полю 'state'"""
    result=[]
    for item in records_to_filter:
        if item['state'] == state:
            result.append(item)
    return result

def sort_by_date():
    pass