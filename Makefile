PYTHON ?= python3

.PHONY: check test reproduce
check:
	$(PYTHON) scripts/check_repository.py

test:
	$(PYTHON) -m unittest discover -s tests -v

reproduce:
	$(PYTHON) scripts/reproduce.py
