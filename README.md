## bleak_sigspec
### Characteristics Metadata xml files from SIG Bluetooth

This package enables characteristic metadata parsing and automatic formatting (bytes unpacking) into the proper characteristic values.
This is a requirement for the function `get_char_value` in `bleak.utils`

To install (not published yet)

```
pip install bleak_sigspec
```

or to get the latest version

```
pip install https://github.com/Carglglz/test_bleak_sigspec.git
```

Compatibility with +200 GATT characteristics following [GATT Specifications](https://www.bluetooth.com/specifications/gatt/characteristics/)

### Usage example

`service_explorer.py` in bleak examples:

`char --> Temperature Characteristic`

```
from bleak.utils import get_char_value
[...]
37
			bytes_value = bytes(await client.read_gatt_char(char.uuid))
			formatted_value = get_char_value(bytes_value, char)
[...]
43
			log.info(
				"Characteristic Name: {0}, Bytes Value: {1}, Formatted
				Value: {2}".format(char.description, bytes_value, formatted_value))


```

```
$ python3 service_explorer.py
[...]
Characteristic Name: Temperature, Bytes Value: b'Z\x16', Formatted Value: {'Temperature':{'Value': 57.22, 'Symbol': 'ºC'}}
```

See more at bleak [documentation](https://bleak.readthedocs.io)

### How it works

This function uses the characteristic's name, parsing the respective xml file to get all the value fields. From there it reads the Flags field (if exists) and unpack the bytes accordingly. After that it performs any post-proccesing operation required (e.g. `DecimalExponent`, `Multiplier` etc). Finally it packs the result in a dictionary.

To see more about bytes packing/unpacking in python see: [struct](https://docs.python.org/3/library/struct.html)



### Future work: Vendor specific or custom characteristics

To format a characteristic value of a Vendor specific or custom characteristic (not defined in GATT specifications) there is a *Characteristic Presentation Format* Descriptor which defines the format of the Characteristic Value. So if this Descriptor is present it is possible to read it and get the characteristic value  format, exponent, unit, name space and description.
