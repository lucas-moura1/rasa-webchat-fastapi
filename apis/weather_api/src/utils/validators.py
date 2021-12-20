from datetime import datetime
import logging

from fastapi import HTTPException

def valitate_data_request(city: str, day: str = "") -> None:
    logging.info("Validate request data")

    validate_city_exists(city)

    if day:
        validate_day(day)


def validate_city_exists(city: str) -> None:
    logging.debug("Validate city data")

    if not city:
        raise HTTPException(409, "Validate Error > Field city required")


def validate_day(day: str) -> None:
    logging.debug("Validate day data")

    if "amanh" in day or "hoje" in day or "None" in day:
        return

    weekday_today_int = datetime.now().isoweekday()

    user_forecasted_day = convert_week_day_in_int_day(day)

    lesser_equal_five_day = verify_if_lesser_equal_five_day(weekday_today_int, user_forecasted_day)

    if not lesser_equal_five_day:
        raise HTTPException(409, "Validate Error > Inform the forecasted weekday remembering that it's maximum 5 days")


def convert_week_day_in_int_day(day: str) -> int:
    int_day = 0

    if "segunda" in day:
        int_day = 1
    elif ("terca" or "terça") in day:
        int_day = 2
    elif "quarta" in day:
        int_day = 3
    elif "quinta" in day:
        int_day = 4
    elif "sexta" in day:
        int_day = 5
    elif ("sabado" or "sábado") in day:
        int_day = 6
    elif "domingo" in day:
        int_day = 7

    return int_day

def verify_if_lesser_equal_five_day(today: int, forecasted_day: int) -> bool:
    diff = forecasted_day - today

    if 0 < diff <= 5 or diff <= -2:
        return True
    else:
        return False
