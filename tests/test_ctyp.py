from ctypespec import __version__, ctyp

print(f"version: {__version__}")

print(ctyp.get("bool"))
print(ctyp.get("int8_t"))
print(ctyp.get("int32_t"))
print(ctyp.get("float"))
print(ctyp.get("uintptr_t"))
print(ctyp.get("unsigned int"))
# print(ctyp.map)
# print(ctyp.map.get("uint32_t"))
# print(ctyp.to_ctypes_name("uintptr_t"))
