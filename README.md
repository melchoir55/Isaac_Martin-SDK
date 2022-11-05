# Isaac_Martin-SDK

## Install

`pip install isaac-martin-sdk`

## Usage

The sdk is designed to abstract retrieving data from the one API. It makes working with the api easier by providing
the following primary benefits:

* Data structures are instantiated in objects, which can be extended
* These objects are intuitively named
* The objects have their relevant fields enumerated. No need to experiment with the API to learn the structures.
* The objects have all relevant http actions implemented.
* Query parameters are also abstracted

### Valid object classes

The following classes are provided to the user which are compatible with the standard `list` and `index` method interfaces:

```python
Book
Movie
Chapter
Character
Quote
```

### Using object methods

`list` and `index` are found on most objects. These methods accept
Certain objects have additional methods. `Character` and `Movie` have `.quotes` and `Book` has `.chapters`. These all 
accept the standard query modification parameters as described below.

### Modifying the method's results

All methods comply with a standard interface. For example, here are the valid parameters accepted by `list`:

```
             limit: int = None,
             page: int = None,
             offset: int = None,
             sort: str = None,
             filters: List[Filter] = []

        :param limit: Limit the number of responses to your specified int.
        :param page: Select which page of responses you wish to return. Usually used in
        conjunction with `limit`
        :param offset: Move the start index of your response window up from it's normal starting point (`0`)
        :param sort: Sort by a specified field either descending or ascending. For example: `name:asc` or `name:dsc`
        :param filters: Filters modify the response according to the configuration of the filter.
```

In order to create a filter, simply import and implement the `filter.Filter` class. Examples below.

### Usage Examples

#### No auth for books, just grab them!
```python
from isaac_martin_sdk.resources.book import Book
from isaac_martin_sdk.sdk import TheOneSDK

TheOneSDK()  # Books don't need auth tokens.
books = Book.list()
```

#### Movies need to be authenticated. The information is very <i>precious</i>.
```python
from isaac_martin_sdk.sdk import TheOneSDK
import os

token = os.environ['TOKEN']  # An authentication token obtained here: https://the-one-api.dev/
TheOneSDK(authentication_token=token)  # Things that aren't books do need auth tokens!

from isaac_martin_sdk.resources.movie import Movie
movies = Movie.list()
```

#### You only need to instantiate the SDK once. After that, you're good to go
```python
from isaac_martin_sdk.sdk import TheOneSDK
import os

token = os.environ['TOKEN']  # An authentication token obtained here: https://the-one-api.dev/
TheOneSDK(authentication_token=token)
```

#### Apply filters and other response modifiers as desired
```python
from isaac_martin_sdk.resources.character import Character
from isaac_martin_sdk.resources.quote import Quote
from isaac_martin_sdk.filter import Filter, Operator

gandalf_filter = Filter(field='name', # valid field names can be found enumerate on the respective objects. For example `Quote` in this case.
                        operator=Operator.REGEX_MATCH,
                        value='Gandalf')

characters = Character.list(sort='name:dsc', filters=[gandalf_filter], limit=1)

gandalf = characters[0]

gandalf_quotes_filter = Filter(field='character',
                               # valid field names can be found enumerate on the respective objects. For example `Quote` in this case.
                               operator=Operator.REGEX_MATCH,
                               value='Gandalf')
quotes = Quote.list(limit=10, filters=[gandalf_quotes_filter])
print(quotes[0].dialog)
```

## Testing for development

A unit test suite can be found in `/tests`.
This suite implements unittest, the test runner from the standard library. 
Make sure to set the environment variable `API_TOKEN` as some of these tests contact the remote api.
You can get a token here: https://the-one-api.dev/

1. Use virtualenv, or poetry, to install requirements.
For example
```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements
```

2. In the context of your venv, execute the tests

```shell
API_TOKEN=<your one api token> poetry run pytest
```