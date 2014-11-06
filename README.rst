PyWatson |Travis CI| |Code Health| |Documentation Status|
=========================================================

A Python adapter for IBM Watson's question and answer API

Installation
------------

Install the package from PyPI:

.. code:: shell

    pip install pywatson

Usage
-----

.. code:: python

    from pywatson.watson import Watson

    # Create a Watson instance with your URL and credentials
    # pywatson will use the endpoint `url + '/question'`
    watson = Watson(url='https://watson-wdc01.ihost.com/instance/507/deepqa/v1', username='someuser', password='zyXHLz3sCoPt6G')

See also
--------

-  `IBM Watson Developer Cloud API Reference <http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/apis/#!/Question_Answer>`__

.. |Travis CI| image:: http://img.shields.io/travis/sherlocke/pywatson.svg?style=flat
   :target: https://travis-ci.org/sherlocke/pywatson
.. |Code Health| image:: https://landscape.io/github/sherlocke/pywatson/master/landscape.png?style=flat
   :target: https://landscape.io/github/sherlocke/pywatson/master
.. |Documentation Status| image:: https://readthedocs.org/projects/pywatson/badge/?version=latest
   :target: https://readthedocs.org/projects/pywatson/?badge=latest
