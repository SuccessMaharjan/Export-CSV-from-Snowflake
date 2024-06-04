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

all: venv install requirements mkdir_extract_csv extract_csv load_profiles seed_csv create_db_schema dbt_seed

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

export_cmd:
	export $(grep -v '^#' .env | xargs)

load_profiles:
	cd loadcsv && python3 load_profiles_yml.py

seed_csv:
	python3 seed_csv.py

create_db_schema:
	cd loadcsv && dbt run -s create_sf_db_and_schema

dbt_seed:
	cd loadcsv && dbt seed