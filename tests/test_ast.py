from ctypes import *  # noqa: F406
from pathlib import Path

from rich.console import Console

from ctypespec import decl_to_cobj, decl_to_ctypes, expand_cobj, headers_to_ast, parse_ast

console = Console()

base = Path().resolve()
sub_dir = ".preprocess"

inputs = ["tests/src/sample.h"]
inputs = [Path(f).resolve() for f in inputs]


def header_to_cobj(
    files: list[str], includes: list[str] = None, defines: dict[str] = None, output_dir: str = None, clean: bool = True
) -> None:
    output_dir = Path(output_dir)

    ast = headers_to_ast(
        files=files,
        includes=includes,
        defines=defines,
        output_dir=output_dir,
        clean=clean,
    )
    # console.print(ast)

    decl = parse_ast(ast)
    # console.print(decl)

    cobj = decl_to_cobj(decl, output_file=output_dir / "cobj.json")
    expand_cobj(cobj, output_file=output_dir / "cobj_ex.json")
    decl_to_ctypes(decl, output_file=output_dir / "ctype.py")


header_to_cobj(
    files=sorted({str(p) for p in inputs}),
    includes=sorted({str(p.parent) for p in inputs}),
    defines=None,
    output_dir="build",
    # clean=False,
)
