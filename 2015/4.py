import hashlib
import sys

key = "yzbqklnj"

for i in range(sys.maxsize):
  data = (key + str(i)).encode('utf-8')
  m = hashlib.md5()
  m.update(data)
  hash_val = m.hexdigest()
  if hash_val[:6] == '000000':
    print(i)
    sys.exit(0)
