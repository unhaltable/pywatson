pywatson
========

A Python adapter for IBM Watson's question and answer API

## Installation

Install the package from PyPI:

    pip install pywatson

## Usage

```python
from pycanlii import Watson

# Create a Watson instance with your URL and credentials
# pywatson will use the endpoint `url + '/question'`
watson = Watson(url='https://watson-wdc01.ihost.com/instance/507/deepqa/v1', username='someuser', password='zyXHLz3sCoPt6G')


```

## See also

- [IBM Watson Developer Cloud API Reference](http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/apis/#!/Question_Answer)
