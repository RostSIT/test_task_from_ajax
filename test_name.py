from scanner_handler import CheckQr
import pytest


class TestCheckQr(CheckQr):
    def test_mocking_check_in_db(self, mocker):
        with mocker.patch("scanner_handler.CheckQr.check_in_db", retu)
