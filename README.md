# ISOParser

It's a parser for ISO format.


## ISO8601 parser
```python

from isoparser import iso8601

iso8601.parse("PT1H35M27S")
# 3687

iso8601.parse("test")
# False

```