from year import what_is_year_now
import pytest
from unittest.mock import patch
import json

TEST_JSON_2019_DMY = {
    "$id": "1",
    "currentDateTime": "01.11.2019",
    "utcOffset": "00:00:00",
    "isDayLightSavingsTime": False,
    "dayOfTheWeek": "Tuesday",
    "timeZoneName": "UTC",
    "currentFileTime": 132513099673251225,
    "ordinalDate": "2020-336",
    "serviceResponse": None,
}

TEST_JSON_2019_SLASH_FORMAT = {
    "$id": "1",
    "currentDateTime": "01/11/2019",
    "utcOffset": "00:00:00",
    "isDayLightSavingsTime": False,
    "dayOfTheWeek": "Tuesday",
    "timeZoneName": "UTC",
    "currentFileTime": 132513099673251225,
    "ordinalDate": "2020-336",
    "serviceResponse": None,
}


def test_current_year_ymd_format():
    actual = what_is_year_now()
    expected = 2020
    assert actual == expected


def test_prev_year_dmy():
    with patch.object(json, "load", return_value=TEST_JSON_2019_DMY):
        actual = what_is_year_now()
    expected = 2019
    assert actual == expected


def test_prev_year_slashed():
    with patch.object(json, "load", return_value=TEST_JSON_2019_SLASH_FORMAT):
        with pytest.raises(ValueError):
            what_is_year_now()
