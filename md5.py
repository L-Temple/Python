import hashlib
mw = input('flag=')
m = hashlib.md5(str(mw).encode(encoding='utf-8')).hexdigest()
print(mw)
print(m)