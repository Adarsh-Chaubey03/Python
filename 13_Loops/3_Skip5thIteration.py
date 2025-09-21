#  print a table upto 10 skip fifth StopIterati
n = 3
for i in range(1, 11):
    if i == 5:      # skip the 5th multiple
        continue
    print(n, 'x', i, '=', n * i)
import traceback

try:
    # your suspect call, e.g. open(path, mode) or os.utime(...)
    ...
except Exception:
    traceback.print_exc()
    # print argument diagnostics
    print("path:", repr(path), type(path))
    print("mode:", repr(mode), type(mode))
