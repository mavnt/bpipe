# What's this

Pipe-like built-in functions.

# Usage

```python
from bpipe import *
data = [1, 2, 3, 4]
sum_ = data | sum()
prod = data | reduce(lambda x, y: x*y)
print(sum_, prod, data | len())

# these still work
print(sum(data), len(data))
```
# Note

- This version overrides builtins and it's not safe. For a safer version see [bpipe2](https://github.com/mavnt/bpipe2/).
- You can use both `>>` and `|`

# Credits

Inspired by [Pipe](https://github.com/JulienPalard/Pipe).