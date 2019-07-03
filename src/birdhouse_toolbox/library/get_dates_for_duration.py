import maya


def get_dates_for_duration(start_date_str, **duration):
    start_date = maya.when(start_date_str, timezone="UTC")
    end_date = start_date.add(**duration).subtract(days=1)
    return (start_date, end_date)
