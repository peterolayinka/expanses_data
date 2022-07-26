import pdb
from flask import url_for
from unittest.mock import patch


def mock_data_path():
    mock_read_csv = patch("app.get_path").start()
    mock_read_csv.return_value = "test/data/test_expanses.csv"


def test_expanses_data_could_be_access_successfully(client):
    mock_data_path()
    expected_data = [
        {
            "amount": 1200.0,
            "date": "Sat, 02 Oct 2021 00:00:00 GMT",
            "departments": "IT",
            "member_name": "Sam",
            "project_name": "Gaama",
        },
        {
            "amount": 929.0,
            "date": "Fri, 05 Nov 2021 00:00:00 GMT",
            "departments": "HR",
            "member_name": "Sam",
            "project_name": "Alph-23",
        },
    ]

    params = {"amount[lt]": "1400", "member_name": "'Sam'"}
    resp = client.get(url_for("expanses_data", **params))

    assert resp.status_code == 200
    assert resp.json == expected_data


def test_expanses_data_could_be_sorted_by_date_successfully(client):
    mock_data_path()
    expected_data = [
        {
            "amount": 929.0,
            "date": "Fri, 05 Nov 2021 00:00:00 GMT",
            "departments": "HR",
            "member_name": "Sam",
            "project_name": "Alph-23",
        },
        {
            "amount": 1200.0,
            "date": "Sat, 02 Oct 2021 00:00:00 GMT",
            "departments": "IT",
            "member_name": "Sam",
            "project_name": "Gaama",
        },
    ]

    params = {
        "amount[lt]": "1400",
        "member_name": "'Sam'",
        "sort": "date",
        "order": "desc",
    }
    resp = client.get(url_for("expanses_data", **params))
    assert resp.status_code == 200
    assert resp.json == expected_data


def test_expanses_data_could_be_access_successfully(client):
    mock_data_path()
    expected_data = {
        "amount": 929.0,
        "date": "Fri, 05 Nov 2021 00:00:00 GMT",
        "departments": "HR",
        "member_name": "Sam",
        "project_name": "Alph-23",
    }

    params = {"fields": 'amount=929.0,departments="HR",member_name="Sam"'}
    resp = client.get(url_for("expanses_data", **params))

    assert resp.status_code == 200
    assert resp.json == expected_data


def test_expanses_data_return_empty_response(client):
    mock_data_path()
    expected_data = {}

    params = {"fields": 'amount=3000.0,departments="HR",member_name="Sam"'}
    resp = client.get(url_for("expanses_data", **params))

    assert resp.status_code == 200
    assert resp.json == expected_data


def test_expanses_data_return_error(client):
    mock_data_path()

    expected_data = {"error": "name 'Sam' is not defined"}

    params = {"amount[lt]": "1400", "member_name": "Sam"}
    resp = client.get(url_for("expanses_data", **params))

    assert resp.status_code == 400
    assert resp.json == expected_data

def test_aggregate_endpoint_could_be_accessed_successfully(client):
    mock_data_path()

    expected_data = [
        {"amount": 42000.0, "departments": "Finance"},
        {"amount": 48458.0, "departments": "HR"},
        {"amount": 32957.0, "departments": "IT"},
        {"amount": 10040.0, "departments": "Marketing"},
        {"amount": 82552.0, "departments": "Sales"},
    ]

    params = {"by": "departments"}
    resp = client.get(url_for("aggregate", **params))

    assert resp.status_code == 200
    assert resp.json == expected_data
