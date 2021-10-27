# Wait code
Wait for a queue of keys to be pressed (like the cheat codes)

[Documentation](https://github.com/themixray/waitcode/wiki)
# Quick Start
Like the cheat codes
```python
from waitcode import waitcode
from rich.console import Console
from rich.table import Table
console = Console()
def stats():
  table = Table()
  table.add_column("Money")
  table.add_column("Health")
  table.add_row(f"{money}$", f"{health}/100")
  console.clear()
  console.print(table)
money = 0
health = 1
stats()

waiting = waitkey('hesoyam')
while 1:
  waiting.wait()
  health = 100
  money += 1000
  stats()
```
