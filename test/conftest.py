import pytest
from helper.pandas_extractor import PandasExtractor

@pytest.fixture
def app():
    from app import app
    return app

@pytest.fixture(scope='module')
def pandas_extractor():
    extractor = PandasExtractor("test/data/test_expanses.csv")
    return extractor
