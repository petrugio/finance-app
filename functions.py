import numpy as np
from termcolor import colored


def normalize_percent(raw_input):
    return round(raw_input * 100, 2)


def format_percent(raw_input: np.float64):
    if raw_input > 0:
        return colored(f"{raw_input} %", 'green')
    else:
        return colored(f"{raw_input} %", 'red')
