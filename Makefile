build:
#	poetry install --with dev
	python .\ctypespec\_version.py
	poetry build

	python tests\test_ctyp.py
