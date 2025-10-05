PYTHON=python
MANAGE=manage.py

run:
	$(PYTHON) $(MANAGE) runserver

setup-db:
	$(PYTHON) $(MANAGE) makemigrations
	$(PYTHON) $(MANAGE) migrate

run-pre-commit:
	pre-commit run --all-files

run-ruff:
	ruff check . && \
	ruff format .

run-server-tailwind:
	$(PYTHON) $(MANAGE) tailwind runserver

run-tailwind-setup
	$(PYTHON) $(MANAGE) tailwind setup

run-tailwind-build:
	$(PYTHON) $(MANAGE) tailwind build

run-tailwind-watch:
	$(PYTHON) $(MANAGE) tailwind watch

run-tailwind-config:
	$(PYTHON) $(MANAGE) tailwind config

run-tailwind-troubleshoot:
	$(PYTHON) $(MANAGE) tailwind troubleshoot

    