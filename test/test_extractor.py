import pytest
from helper.extractor import Extractor

def test_abstract_extractor_get_data_raise_error():
    Extractor.__abstractmethods__=set()
    extractor = Extractor()
    with pytest.raises(NotImplementedError):
        extractor.get_data({})


def test_abstract_extractor_construct_query_raise_error():
    Extractor.__abstractmethods__=set()
    extractor = Extractor()
    with pytest.raises(NotImplementedError):
        extractor.construct_query({})


def test_abstract_extractor_parse_query_raise_error():
    Extractor.__abstractmethods__=set()
    extractor = Extractor()
    with pytest.raises(NotImplementedError):
        extractor.parse_query({})


def test_abstract_extractor_query_raise_error():
    Extractor.__abstractmethods__=set()
    extractor = Extractor()
    with pytest.raises(NotImplementedError):
        extractor.query({})


def test_abstract_extractor_filter_data_raise_error():
    Extractor.__abstractmethods__=set()
    extractor = Extractor()
    with pytest.raises(NotImplementedError):
        extractor.filter_data({})


def test_abstract_extractor_aggregate_data_raise_error():
    Extractor.__abstractmethods__=set()
    extractor = Extractor()
    with pytest.raises(NotImplementedError):
        extractor.aggregate_data({})
