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


def send_error_mock(counting_point, right_most_digit, method):
    with mock.patch.object(CheckQr, method, new=new_send_error):
        invalid_qr_length(counting_point, right_most_digit)
        assert m_error[
                   0] == f"Error: Wrong qr length {len(str(counting_point))}", f"{m_error} - this is not error message"


def color(counting_point, right_most_digit, col):
    with mock.patch.object(CheckQr, 'check_in_db', new=new_check_in_db_for_test_color):
        length = str(qr(counting_point, right_most_digit))
        obj = CheckQr()
        obj.check_scanned_device(length)
        assert obj.color == col, f"Length {length} != {col}"


def invalid_qr_length(counting_point, right_most_digit):
    with mock.patch.object(CheckQr, 'check_in_db', new=new_check_in_db_for_invalid_qr_length):
        length = str(qr(counting_point, right_most_digit))
        obj = CheckQr()
        obj.check_scanned_device(length)
        assert obj.color == red or green or fw, f"Length is invalid for qr"


def valid_qr_length(counting_point, right_most_digit):
    with mock.patch.object(CheckQr, 'check_in_db', new=new_check_in_db_for_test_color):
        global length
        length = str(qr(counting_point, right_most_digit))
        obj = CheckQr()
        obj.check_scanned_device(length)


def test_red_color():
    color(100, 999, red)


def test_green_color():
    color(10000, 99999, green)


def test_fw_color():
    color(1000000, 9999999, fw)


def test_negative_color_testing():
    invalid_qr_length(10, 99)


def test_send_error():  # Test 'Error: Wrong qr length' message
    send_error_mock(10, 20, 'send_error')


def can_add_device_mock(counting_point, right_most_digit):
    with mock.patch.object(CheckQr, 'can_add_device', new=new_send_error):
        valid_qr_length(counting_point, right_most_digit)
        assert m_error[0] == f"hallelujah {length}", f"{m_error} this is not 'hallelujah' message"


def can_add_device_mock_not_in_db(counting_point, right_most_digit):
    with mock.patch.object(CheckQr, 'send_error', new=new_send_error):
        invalid_qr_length(counting_point, right_most_digit)
        assert m_error[0] == f"Not in DB", f"{m_error} this is not 'Not in DB' message"


def test_can_add_device():  # Test 'hallelujah' message
    can_add_device_mock(100, 200)


def test_can_add_device_not_in_db():  # Test'Not in DB' message
    can_add_device_mock_not_in_db(100, 200)
    assert m_error[0] == "Not in DB", f"this is not 'Not in DB'message"
