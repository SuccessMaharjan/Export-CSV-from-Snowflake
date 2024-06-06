# variables
export
VENV= .venv
PYTHON = python3


.PHONY: venv install 
# Detect the operating system
ifeq ($(OS),Windows_NT)
    VENV_ACTIVATE := $(VENV)\Scripts\activate
    PYTHON_ENV := $(PYTHON)
    ACTIVATE_CMD :=
else
    VENV_ACTIVATE := $(VENV)/bin/activate
    PYTHON_ENV := $(PYTHON)
    ACTIVATE_CMD := .
endif

all: venv install requirements mkdir_extract_csv extract_csv load_profiles seed_csv dbt_seed

venv:
	$(PYTHON_ENV) -m venv $(VENV)

install:
	$(ACTIVATE_CMD) $(VENV_ACTIVATE)

requirements:
	pip3 install -r requirements.txt

mkdir_extract_csv:
	@if [ ! -d "extracted_csv" ]; then \
		mkdir extracted_csv; \
	else \
		echo "extracted_csv folder already exists, skipping mkdir"; \
	fi

extract_csv:
	python3 export.py

## This command is required if .env is not working on MAC.
##export_cmd:
##	export $(grep -v '^#' .env | xargs)

load_profiles:
	cd loadcsv && python3 load_profiles_yml.py

seed_csv:
	python3 seed_csv.py

dbt_seed:
	cd loadcsv && dbt seed