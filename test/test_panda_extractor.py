
def test_pandas_extractor_can_filter_expanse(pandas_extractor):
    print("test_pandas_extractor_filter_expanse")
    expected_data = [
        {
            "amount": 1200.0,
            "date": "2021-10-02 00:00:00",
            "departments": "IT",
            "member_name": "Sam",
            "project_name": "Gaama",
        },
        {
            "amount": 929.0,
            "date": "2021-11-05 00:00:00",
            "departments": "HR",
            "member_name": "Sam",
            "project_name": "Alph-23",
        },
    ]

    params = {"amount[lt]": "1400", "member_name": "'Sam'"}
    data = pandas_extractor.filter_data(params)
    data_dict = data.to_dict(orient="records")
    for item in data_dict:
        item['date'] = str(item['date'])

    assert data_dict == expected_data


def test_pandas_extractor_can_filter_and_sort_expanse(pandas_extractor):
    expected_data = [
        {
            "amount": 929.0,
            "date": "2021-11-05 00:00:00",
            "departments": "HR",
            "member_name": "Sam",
            "project_name": "Alph-23",
        },
        {
            "amount": 1200.0,
            "date": "2021-10-02 00:00:00",
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
    data = pandas_extractor.filter_data(params)
    data_dict = data.to_dict(orient="records")
    for item in data_dict:
        item['date'] = str(item['date'])

    assert data_dict == expected_data


def test_pandas_extractor_filter_return_error(pandas_extractor):
    expected_data = {"error": "name 'Sam' is not defined"}

    params = {"amount[lt]": "1400", "member_name": "Sam"}
    data = pandas_extractor.filter_data(params)

    assert data == expected_data


def test_pandas_extractor_can_get_single_expanse(pandas_extractor):
    expected_data = [{
        "amount": 929.0,
        "date": "2021-11-05 00:00:00",
        "departments": "HR",
        "member_name": "Sam",
        "project_name": "Alph-23",
    }]

    params = {"fields": 'amount=929.0,departments="HR",member_name="Sam"'}
    data = pandas_extractor.filter_data(params)
    data_dict = data.to_dict(orient="records")
    data_dict[0]['date'] = str(data_dict[0]['date'])

    assert data_dict == expected_data


def test_pandas_extractor_can_aggregate_data(pandas_extractor):

    expected_data = [
        {"amount": 42000.0, "departments": "Finance"},
        {"amount": 48458.0, "departments": "HR"},
        {"amount": 32957.0, "departments": "IT"},
        {"amount": 10040.0, "departments": "Marketing"},
        {"amount": 82552.0, "departments": "Sales"},
    ]

    params = {"by": "departments"}
    data = pandas_extractor.aggregate_data(params)
    data_dict = data.to_dict(orient="records")

    assert data_dict == expected_data


def test_pandas_extractor_clean_currecy(pandas_extractor):
    expected_data = 20000.0

    currency_string = "€20,000"
    data = pandas_extractor.clean_currency(currency_string)

    assert data == expected_data

def test_pandas_extractor_returned_already_clean_currecy(pandas_extractor):
    expected_data = 20000

    currency_string = 20000
    data = pandas_extractor.clean_currency(currency_string)

    assert data == expected_data
