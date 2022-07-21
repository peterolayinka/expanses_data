from abc import ABC, abstractmethod

class Extractor(ABC):
    @abstractmethod
    def get_data(self, path):
        raise NotImplementedError

    @abstractmethod
    def construct_query(self, path):
        raise NotImplementedError

    @abstractmethod
    def parse_query(self, path):
        raise NotImplementedError

    @abstractmethod
    def query(self, path):
        raise NotImplementedError

    @abstractmethod
    def filter_data(self, path):
        raise NotImplementedError

    @abstractmethod
    def aggregate_data(self, path):
        raise NotImplementedError
