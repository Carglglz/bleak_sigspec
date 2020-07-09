from setuptools import setup

setup(name='bleak_sigspec',
      version='0.0.1',
      description='SIG Bluetooth Low Energy Characteristic Metadata',
      url='http://github.com/cgglz/test_bleak_sigspec',
      author='Carlos Gil Gonzalez',
      author_email='carlosgilglez@gmail.com',
      license='MIT',
      packages=['bleak_sigspec'],
      zip_safe=False,
      include_package_data=True,
      install_requires=['bleak>=0.7.1'])
