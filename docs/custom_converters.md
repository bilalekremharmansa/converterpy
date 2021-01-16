# Custom Converter

Creating custom converter and integrate with command line interface is easy.

### First things first: create a module for custom converter

Create a module in the path of your choice, ie: ```/opt/converterpy/custom_converters```

```bash
$ mkdir /opt/converterpy/custom_converters
$ touch /opt/converterpy/custom_converters/__init__.py
```

### Implementing Converter interface

First, import ```Converter``` interface and ```Unit``` class

```python
from converterpy.provider import ConverterProvider
from converterpy.converter import Converter
from converterpy.unit import Unit
```

Create required units;

```python
# Unit(short_name, full_name)

UNIT_INT = Unit('int', 'integer')
UNIT_FLOAT = Unit('fl', 'float')
```

Implement a converter class:

```python
class NumberConverter(Converter):

    def __init__(self):
        super(NumberConverter, self).__init__('converter name')

    def supported_conversions(self):
        # source -> [target1, target2]
        return {
            UNIT_INT: [UNIT_FLOAT],
            UNIT_FLOAT: [UNIT_INT]
        }

    def is_convertible(self, source_unit, target_unit):
        # is given source_unit convertible to target_unit ?
        return source_unit in self.supported_conversions() and target_unit in self.supported_conversions()[source_unit]

    def convert(self, source_unit, source_value, target_unit):
        # since source_value is coming from cli, it's type is str, you may want to cast to something else
        # type(source_value) = str

        if source_unit == UNIT_INT and target_unit == UNIT_FLOAT:
            return float(source_value)
        elif source_unit == UNIT_FLOAT and target_unit == UNIT_INT:
            return float(source_value)

        raise Exception("Unknown conversion")
```

One last thing to implement...

```python
class MyConverterProvider(ConverterProvider):

    def provide(self):
        return [
            NumberConverter()
        ]
```

```MyConverterProvider``` will allow ```converterpy``` to initialize NumberConverter instance.

### Saving implementations

Save this file to the folder you've just created. ```/opt/converterpy/custom_converters/number_converter_provider.py```

### Configure converterpy to interact with custom converters

Now, you can configure converterpy config file which is located at ```/etc/converterpy.json```. Here is an example
config file;

```json
[{
    "base_path": "/opt/converterpy",
    "module_name": "custom_converters.number_converter_provider",
    "class_name": "MyConverterProvider"
}]
```

Final file structure should be like;

```bash
converterpy
└── custom_converters
    ├── __init__.py
    └── number_converter_provider.py
```

### It's ready convert!

```bash
$ convert 10 integer to float
```