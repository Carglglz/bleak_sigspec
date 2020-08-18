===========
Limitations
===========

``get_char_value may fail``, or return unexpected results due to the following reasons:

- The characteristic does not exist in ``bleak`` or the xml file in ``bleak_sigspec`` is missing
- There is a bug in the xml file.
- The format of the characteristic is not supported (see: `struct <https://docs.python.org/3/library/struct.html>`_.)
- There is a bug in ``get_char_value``
- The data is not formatted following the xml file description.
