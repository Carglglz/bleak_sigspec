============
How it works
============

``get_char_value`` function uses the characteristic's name, parsing the respective xml file
to get all the value fields. From there it reads the Flags field (if exists)
and unpack the bytes accordingly.
After that it performs any post-proccesing operation required
(e.g. DecimalExponent, Multiplier etc). Finally it packs the result in a dictionary.

To see more about bytes packing/unpacking in python see: `struct <https://docs.python.org/3/library/struct.html>`_.
