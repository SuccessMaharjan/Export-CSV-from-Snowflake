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

all: venv install requirements mkdir_extract_csv extract_csv

venv:
	$(PYTHON_ENV) -m venv $(VENV)

install:
	$(ACTIVATE_CMD) $(VENV_ACTIVATE)

requirements:
	pip3 install -r requirements.txt

mkdir_extract_csv:
	mkdir extracted_csv

extract_csv:
	python3 export.py