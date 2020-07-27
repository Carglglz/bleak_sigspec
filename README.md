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

