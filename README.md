# url_tools

A Python utility module for URL parsing and manipulation.

## Functions

### `parse_url(url: str) -> dict`
Parses a URL string and returns its components (scheme, netloc, path, params, query, fragment).

### `validate_url(url: str) -> bool`
Validates whether a string is a well-formed URL.

### `extract_domain(url: str) -> str`
Extracts the domain name from a URL.

### `get_query_params(url: str) -> dict`
Parses and returns query parameters from a URL as a dictionary.

### `build_url(scheme: str, domain: str, path: str, params: dict = None) -> str`
Constructs a URL from individual components.


## Usage

```python
from url_tools import parse_url, validate_url, extract_domain

url = "https://example.com/path?key=value"
print(parse_url(url))
print(validate_url(url))
print(extract_domain(url))
```

## License

MIT