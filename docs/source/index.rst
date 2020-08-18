.. bleak_sigspec documentation master file, created by
   sphinx-quickstart on Tue Aug 18 17:11:14 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

bleak_sigspec
=============

.. image:: https://raw.githubusercontent.com/hbldh/bleak/master/Bleak_logo.png
    :target: https://github.com/hbldh/bleak
    :alt: Bleak Logo
    :width: 50%

**Bleak SIG Bluetooth Characteristic Specification Formatter**

This package enables characteristic metadata parsing and automatic formatting (bytes unpacking) into the proper characteristic values.

* Free software: MIT license
* Documentation: https://bleak_sigspec.readthedocs.io.

Features
--------

- xml `SIG Bluetooth GATT Characteristics <https://www.bluetooth.com/specifications/gatt/characteristics/>`_ parser
- Automatic formatting based on xml metadata (from bytes to dictionary data type)

Installation
------------

Install ``bleak_sigspec`` by running:

.. code-block:: console

    $ pip install bleak_sigspec

Or get latest development version:

.. code-block:: console

    $ pip install https://github.com/Carglglz/bleak_sigspec.git


Usage
-----
*Example:* ``service_explorer.py`` in bleak examples:

.. code-block:: python

    from bleak_sigspec.utils import get_char_value
    [...]
    37
       bytes_value = bytes(await client.read_gatt_char(char.uuid))
       formatted_value = get_char_value(bytes_value, char)
    [...]
    43
       log.info(
         "Characteristic Name: {0}, Bytes Value: {1}, Formatted
         Value: {2}".format(char.description, bytes_value, formatted_value))

**Output**

.. code-block:: console

    $ python3 service_explorer.py
    [...]
    Characteristic Name: Temperature, Bytes Value: b'Z\x16', Formatted Value: {'Temperature': {'Quantity': 'thermodynamic temperature',
    'Unit': 'degree celsius',
    'Symbol': '°C',
    'Value': 57.22}}


Contribute
----------

- `Issue Tracker <https://github.com/Carglglz/bleak_sigspec/issues>`_.
- `Source Code  <https://github.com/Carglglz/bleak_sigspec>`_.


Contents
--------

.. toctree::
   :maxdepth: 2

   howitworks
   limitations
   futurework
   api


License
--------

The project is licensed under the MIT license.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
