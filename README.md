# AppDaemon Helpers

Some helper functions I use in multiple AppDaemon apps.

## Installation
Clone the repository into your AppDaemon `apps` directory:
```bash
git clone https://github.com/LupinIII/appdaemon-helpers.git helpers
```

### Directory Structure
Placed as a sibling directory to my apps:
```text
> apps
  > app1    (one of the apps)
  > helpers (This repository)
```

## Available functions

### `class EntityFilter`:
Implements an entity filter following Home Assistant recorder's syntax. Home Assistant `entity_id`s can then be checked against this filter.

#### Usage example:
```python
from helpers import EntityFilter

my_filter = EntityFilter(my_app_config.get('entity_filter'))
if my_filter.is_included('sensor.meter_l1_voltage'):
  # do stuff
  pass
```

Where `entity_filter` is something like this in apps.yaml:
```yaml
my_app:
  entity_filter:
    include:
      entities:
        - sensor.node1_uptime
      domains:
        - sensor
    exclude:
      entities:
        - sensor.commode
        - sensor.error_codes
      entity_globs:
        - sensor.*uptime
```


<br>

### `class BreakNested`:
A custom exception to raise to break out of nested loops

<br>

### `try_float(value) -> float | None`:
Just a wrapper for Python's `float()` function to avoid `try...except` block clutter in code. Returns `None` on failure, the parsed float otherwise.

#### Usage example:

```python
from helpers import try_float

float1 = try_float('3.14')
print(float1) # output: 3.14

float2 = try_float('non_numeric_string')
print(float2) # output: None
```

<br>

### `__LINE__() -> int | None`:
Mimics the C preprocessor `__LINE__` macro. Inspects the execution stack to return the line number where the function is called.


#### Usage example:

```python
from helpers import __LINE__
# .
# .
# .
# line 40
# line 41
print(f'{__LINE__()}') # output: 42
```

## License

This project is licensed under the **GNU General Public License v3 (GPL-3.0)**.

For the full legal text, please refer to the [LICENSE](LICENSE) file in the root of this repository.