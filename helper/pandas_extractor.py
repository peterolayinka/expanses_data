import pdb
import pandas as pd

from .extractor import Extractor


class PandasExtractor(Extractor):
    data = None
    substitutions = {
        "[gte][=]": " >= ",
        "[lte][=]": " <= ",
        "[gt][=]": " > ",
        "[lt][=]": " < ",
        "[eq][=]": " == ",
        "[neq][=]": " != ",
        "[in][=]": " in ",
        "[=]": " == ",
    }
    query_text = None
    sort = None
    order = None
    fields = None

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.data = self.get_data()

    def get_data(self):
        """
        Reads the data from the csv file and returns a pandas dataframe.
        """
        data = pd.read_csv(self.path)
        data["amount"] = data["amount"].apply(self.clean_currency).astype(float)
        data["date"] = pd.to_datetime(data["date"])
        return data

    def replace_tags(self, data, tags):
        """
        Replace tags in the data with a subtitute value.
        """
        for key, value in tags.items():
            data = data.replace(key, value)
        return data

    def construct_query(self, query_string):
        """
        Constructs a query string from the request query string.
        """
        if type(query_string) is dict:
            query_list = [
                self.replace_tags("[=]".join(x), self.substitutions)
                for x in query_string.items()
            ]
        else:
            query_list = [
                self.replace_tags(x.replace("=", "[=]"), self.substitutions)
                for x in query_string.split(",")
            ]

        query = " & ".join(query_list)
        self.query_text = query
        return query

    def parse_query(self, query_string):
        """
        Parse the query string and return a query string
        """
        new_query = {**query_string}
        if "sort" in new_query:
            self.sort = new_query.pop("sort")
        if "order" in new_query:
            self.order = new_query.pop("order")
        if "fields" in new_query:
            self.fields = new_query.pop("fields")
            return self.construct_query(self.fields)

        return self.construct_query(new_query)

    def clean_currency(self, x):
        """If the value is a string, then remove currency symbol and delimiters
        otherwise, the value is numeric and can be converted
        """
        if isinstance(x, str):
            tags = {
                "$": "",
                "€": "",
                ",": "",
            }
            x = self.replace_tags(x, tags)
            return float(x)
        return x

    def query(self, query):
        """
        Query the dataframe and return a dataframe
        or an error message form the query.
        """
        try:
            return self.data.query(query)
        except Exception as e:
            return {"error": str(e)}

    def filter_data(self, query_string):
        """
        Filter/sort the dataframe and return a dataframe
        """
        query = self.parse_query(query_string)
        result = self.query(query)
        if self.sort:
            asc = True if self.order == "asc" else False
            result = result.sort_values(by=self.sort, ascending=asc)

        return result

    def aggregate_data(self, query_string):
        """
        Aggregate the dataframe and return a dataframe
        """
        data = self.data.groupby(
            query_string.get("by", "project_name"), as_index=False
        )["amount"].sum()
        return data
