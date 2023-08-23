from time import sleep
from os import system


CONVERSION_DICT: dict[str: int] = {
    's': 1,
    'm': 60,
    'h': 3600,
    'd': 86400,
    'w': 604800
}
VALID_UNITS: str = ', '.join(f'"{unit}"' for unit in CONVERSION_DICT.keys())


def get_delay() -> int:
    delay_time_input: str = input('Enter delay time: ')
    delay_time_seconds: int = _convert_to_seconds(delay_time_input)
    return delay_time_seconds


def _convert_to_seconds(delay_time_str) -> int:
    try:
        current_time_unit = delay_time_str[-1].lower()
        if '.' in delay_time_str:
            delay_time_float = float(delay_time_str[:-1])
            return _convert_decimal_to_seconds(delay_time_float, current_time_unit)
        
        delay_time_int = int(delay_time_str[:-1])
        return _convert_integer_to_seconds(delay_time_int, current_time_unit)
    
    except ValueError:
        print(f'Inputs must be numbers (integer or decimal) ending in one of the following: {VALID_UNITS}')
        return get_delay()


def _convert_decimal_to_seconds(decimal_part, unit):
    if unit in CONVERSION_DICT:
        return int(decimal_part * CONVERSION_DICT[unit])
    raise ValueError()


def _convert_integer_to_seconds(integer_part, unit):
    if unit in CONVERSION_DICT:
        return integer_part * CONVERSION_DICT[unit]
    raise ValueError()


def sleep_after_delay(delay_time) -> None:
    sleep(delay_time)
    system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')


if __name__ == '__main__':
    DELAY: int = get_delay()
    sleep_after_delay(DELAY)