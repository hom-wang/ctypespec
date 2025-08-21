
@venv:
    uv sync

@build:
    uv build --no-sources

@test:
    uv run python tests/test_ctyp.py

@publish: build test
    uv publish --token "$(pass show pypi/token)"
