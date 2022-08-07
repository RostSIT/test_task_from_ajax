from scanner_handler import CheckQr
import mock
import random

red = 'Red'
green = 'Green'
fw = 'Fuzzy Wuzzy'


def qr(counting_point, right_most_digit):
    q = random.randint(counting_point, right_most_digit)
    return q


def new_check_in_db_for_test_color(cls, *args, **kwargs):
    return True


def new_check_in_db_for_invalid_qr_length(cls, *args, **kwargs):
    return False


def new_send_error(cls, *args, **kwargs):
    global m_error
    m_error = args

    return m_error