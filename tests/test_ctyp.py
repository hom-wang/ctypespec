from ctypespec import __version__, ctyp


def verify_ctyp(typ: str, sign: str, category: str, bits: int, short: str):
    ct = ctyp.get(typ)
    print(f"{ct}, {ct.flag}")
    if ct.sign != sign:
        raise ValueError(f"wrong sign: {ct.sign}")
    elif ct.category != category:
        raise ValueError(f"wrong category: {ct.category}")
    elif ct.bits != bits:
        raise ValueError(f"wrong bits: {ct.bits}")
    elif ct.short != short:
        raise ValueError(f"wrong short: {ct.short}")
    elif ct.fmt is None:
        raise ValueError(f"wrong fmt: {ct.fmt}")


def verify_range(typ: str, min_value, max_value):
    ct = ctyp.get(typ)
    print(f"{typ}: [{ct.min}, {ct.max}]")
    if ct.min != min_value or ct.max != max_value:
        raise ValueError(f"wrong range: [{ct.min}, {ct.max}], expected [{min_value}, {max_value}]")


def verify_clip(typ: str, value, expected):
    ct = ctyp.get(typ)
    clipped = ct.clip(value)
    print(f"{typ}: clip({value}) = {clipped}")
    if clipped != expected:
        raise ValueError(f"wrong clip({value}): {clipped}, expected {expected}")


def verify_to_value(typ: str, value, expected, clip: bool = False):
    ct = ctyp.get(typ)
    converted = ct.to_value(value, clip=clip)
    print(f"{typ}: to_value({value!r}, clip={clip}) = {converted}")
    if converted != expected or not isinstance(converted, type(expected)):
        raise ValueError(f"wrong to_value({value!r}): {converted}, expected {expected}")


print(f"version: {__version__}")
print("----------------")

verify_ctyp("bool", "unsigned", "int", 8, "u8")
verify_ctyp("char", "signed", "int", 8, "i8")
verify_ctyp("int8_t", "signed", "int", 8, "i8")
verify_ctyp("u16", "unsigned", "int", 16, "u16")
verify_ctyp("int32_t", "signed", "int", 32, "i32")
verify_ctyp("float", "signed", "float", 32, "f32")
verify_ctyp("uintptr_t", "unsigned", "pointer", 32, "ptr")
verify_ctyp("unsigned int", "unsigned", "int", 32, "u32")

print("----------------")

verify_range("bool", 0, 1)
verify_range("int8_t", -128, 127)
verify_range("uint8_t", 0, 255)
verify_range("int32_t", -2147483648, 2147483647)
verify_range("uint64_t", 0, 18446744073709551615)
verify_range("float", -3.4e38, 3.4e38)
verify_range("f32", -3.4e38, 3.4e38)
verify_range("double", -1.7e308, 1.7e308)
verify_range("f64", -1.7e308, 1.7e308)
verify_range("long double", float("-inf"), float("inf"))
verify_range("uintptr_t", None, None)

print("----------------")

verify_clip("int8_t", 200, 127)
verify_clip("int8_t", -200, -128)
verify_clip("int8_t", "42", 42)
verify_clip("float", 1e40, 3.4e38)
verify_clip("float", -1e40, -3.4e38)
verify_clip("float", "-2.5", -2.5)
verify_clip("double", 1e40, 1e40)
verify_clip("uintptr_t", 1, None)

print("----------------")

verify_to_value("int32_t", "42", 42)
verify_to_value("int32_t", 3.9, 3)
verify_to_value("float", 2.5, 2.5)
verify_to_value("float", "2.5", 2.5)
verify_to_value("float", 1e40, 3.4e38, clip=True)
verify_to_value("int8_t", 200, 127, clip=True)
