from scanner_handler import CheckQr
from faker import Faker
import mock
import pytest


def new_loaddata(cls, *args, **kwargs):
    # Your custom testing override
    return True


def test_SomeProductionProcess():
    with mock.patch.object(CheckQr, 'check_in_db', new=new_loaddata):
        obj = CheckQr()
        a = obj.check_in_db(qr='123')
        assert a == True, "a = False"


def qr(qrl):
    fake = Faker()
    red_qr = fake.password(qrl)
    return red_qr

print(qr(3))
def test_red_color():
    with mock.patch.object(CheckQr, 'check_in_db', new=new_loaddata):
        r = "123"
        obj = CheckQr()
        obj.check_scanned_device(r)
        assert obj.color == 'Red', f"Len {r} != Red"
# print('\n', qr(3), '\n')

# def test_Green_color(self):
#     color_qr = self.check_scanned_device(qr(5))
#     assert color_qr == 'Green'
#
#
# def test_Fuzzy_Wuzzy_color(self):
#     color_qr = self.check_scanned_device(qr(7))
#     assert color_qr == 'Fuzzy Wuzzy'
