===========
Future Work
===========

Vendor specific or custom characteristics
-----------------------------------------

To format a characteristic value of a Vendor specific or custom characteristic
(not defined in GATT specifications) there is a *Characteristic Presentation
Format* Descriptor which defines the format of the Characteristic Value.
So if this Descriptor is present it is possible to read it and get the
characteristic value  format, exponent, unit, name space and description.

To add custom characteristics it is possible to write a xml file describing
the characteristic and provide a 128 UUID. Then this could be registered
in ``bleak/bleak_sigspec``.
