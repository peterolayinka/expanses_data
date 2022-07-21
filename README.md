# Coding challenge Backend Exercise - Python

```
TIMEBOX:    2hours +
LANGUAGES:  Python
FRAMEWORKS: Flask
TESTS:      I would have loved to write some unit test with `pytest` but the instruction efforces (We mean it!) a 3 hour hard limit and I wouldn't want to submit an incomplete test case.
DOCS:       Please find the DOCS below.
```

## Installation

- RUN `python3 -m venv venv` to create a virtual environment
- RUN `source ./venv/bin/activate` to enable the virtual env
- RUN `pip install -r requirements.txt` to install required libraries.
- export environment variable with the statements below.
  - `export FLASK_ENV=development`
  - `export FLASK_APP=app`
  - `export FLASK_RUN_HOST=0.0.0.0` (optional)

## Launch APP

- RUN `flask run` to start the app

## Sample Endpoint URL

- The sample URL below is used to list expanses data via API GET request
  - http://127.0.0.1:5000/expanses_data?amount[lt]=1400&member_name="Sam"

  - http://127.0.0.1:5000/expanses_data?amount[lt]=1400&member_name="Sam"&sort=date&order=asc

- The sample URL below is used to fetch a single record via GET request

  - http://127.0.0.1:5000/expanses_data?fields=amount=1298.0,departments="Marketing",member_name="Sam"


- The sample URL below is used to get total sum of expanses by departments, project_name, date and by member_name etc...

  - http://127.0.0.1:5000/agregate?by=departments

