SRC_DIR     = src
VENV        = venv
PYTHON      = $(VENV)/bin/python
MANAGE      = $(SRC_DIR)/manage.py
ENV_PATH    = ./$(SRC_DIR)/liblr/env.py


all: check


.PHONY: check
.SILENT: check
check: $(PYTHON) $(MANAGE)
	$(call colorize,6,"Running default check")
	$(PYTHON) $(MANAGE) check
	$(call colorize,6,"Running migration dry-run")
	$(PYTHON) $(MANAGE) makemigrations --dry-run


.PHONY: makemigrations
.SILENT: makemigrations
makemigrations: $(PYTHON) $(MANAGE)
	$(call colorize,1,"Creating migrations")
	$(PYTHON) $(MANAGE) makemigrations


.PHONY: migrate
.SILENT: migrate
migrate: $(PYTHON) $(MANAGE)
	$(call colorize,1,"Running migrations")
	$(PYTHON) $(MANAGE) migrate


.PHONY: run
.SILENT: run
run: $(PYTHON) $(MANAGE)
	$(PYTHON) $(MANAGE) runserver


.PHONY: shell
.SILENT: shell
shell: $(PYTHON) $(MANAGE)
	$(PYTHON) $(MANAGE) shell


env: $(ENV_PATH)


.PHONY: $(ENV_PATH)
.SILENT: $(ENV_PATH)
$(ENV_PATH):
ifneq (,$(wildcard $(ENV_PATH)))
	$(call colorize,1,"Local env already exists at: $(ENV_PATH)")
else
	$(call colorize,1,"Creating default local env at: $(ENV_PATH)")
	touch $(ENV_PATH)
	echo "import os" >> $(ENV_PATH)
	echo "_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))" >> $(ENV_PATH)
	echo "SECRET_KEY = 'super_secret'" >> $(ENV_PATH)
	echo "DATABASE = {" >> $(ENV_PATH)
	echo "    'ENGINE': 'django.db.backends.sqlite3'," >> $(ENV_PATH)
	echo "    'NAME': os.path.join(_BASE_DIR, 'db.sqlite3')," >> $(ENV_PATH)
	echo "}" >> $(ENV_PATH)
	$(call colorize,2,"Done")
endif


define colorize
	@tput setaf $1
	@echo $2
	@tput sgr0
endef
