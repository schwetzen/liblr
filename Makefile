SRC_DIR        = src
VENV           = venv
DRIVER_DIR    := $(PWD)/.drivers
PYTHON         = $(VENV)/bin/python
GECKODRIVER    = $(DRIVER_DIR)/geckodriver
MANAGE         = $(SRC_DIR)/manage.py
ENV_PATH       = ./$(SRC_DIR)/liblr/env.py
LAUNCHER_PATH  = /etc/systemd/system
NGINX_PATH     = /etc/nginx
DOMAIN         = schwetzen.com
WHOAMI        := $(shell whoami)
UNAME         := $(shell uname)
PATH          := $(shell echo $$PATH)


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


.PHONY: static
.SILENT: static
static: $(PYTHON) $(MANAGE)
	$(call colorize,1,"Collecting static files")
	$(PYTHON) $(MANAGE) collectstatic --no-input


.PHONY: clean
.SILENT: clean
clean:
	$(call colorize,1,"Deleting compiled files...")
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

	$(call colorize,1,"Deleting symlink to geckodriver...")
	rm -f $(GECKODRIVER)


.SILENT: $(GECKODRIVER)
$(GECKODRIVER):
	$(call colorize,3,"Setting up test driver...")
ifeq ($(UNAME),Darwin)
	ln -s $(GECKODRIVER)-macos $(GECKODRIVER)
	$(call colorize,2,"Set up symlink to driver for macOS")
else
ifeq ($(UNAME),Linux)
	ln -s $(GECKODRIVER)-linux64 $(GECKODRIVER)
	$(call colorize,2,"Set up symlink to driver for Linux")
else
	$(error "Unknown platform: $(UNAME)")
endif
endif


.PHONY: test
.SILENT: test
test: $(GECKODRIVER) $(PYTHON) $(MANAGE)
ifneq ($(WHOAMI),schwetzen)
	$(call colorize,3,"Running tests...")
	PATH="$(DRIVER_DIR):$(PATH)" $(PYTHON) $(MANAGE) test app
else
	$(call colorize,1,"Not running tests here.")
endif


.PHONY: run
.SILENT: run
run: static $(PYTHON) $(MANAGE)
ifneq ($(WHOAMI),schwetzen)
	$(PYTHON) $(MANAGE) runserver
else
	$(call colorize,3,"Restarting gunicorn...")
	sudo systemctl restart gunicorn
endif


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
	$(call colorize,3,"Creating default local env at: $(ENV_PATH)")
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


# Production declarations

.PHONY: setup status logs
.SILENT: setup status logs
setup:
ifneq ($(WHOAMI),schwetzen)
	$(call colorize,1,"Current environment incorrect.")
else
	$(call colorize,3,"Copying launcher files...")
	sudo cp .gunicorn.socket $(LAUNCHER_PATH)/gunicorn.socket
	sudo cp .gunicorn.service $(LAUNCHER_PATH)/gunicorn.service

	$(call colorize,3,"Setting up socket...")
	sudo systemctl start gunicorn.socket
	sudo systemctl enable gunicorn.socket

	$(call colorize,3,"Copying nginx configuration...")
	sudo cp .nginx $(NGINX_PATH)/sites-available/liblr
	sudo ln -s $(NGINX_PATH)/sites-available/liblr $(NGINX_PATH)/sites-enabled
	sudo systemctl reload nginx

	$(call colorize,3,"Setting up certbot...")
	sudo certbot --nginx -d $(DOMAIN) -d www.$(DOMAIN)

	$(call colorize,3,"Setting up monthly auto-renew...")
	sudo touch /etc/cron.monthly/cert.sh
	sudo chmod +x /etc/cron.monthly/cert.sh
	echo "sudo certbot renew" | sudo tee /etc/cron.monthly/cert.sh
endif


status:
ifneq ($(WHOAMI),schwetzen)
	$(call colorize,1,"Current environment incorrect.")
else
	$(call colorize,3,"Checking gunicorn socket...")
	sudo systemctl status gunicorn.socket
	file /run/gunicorn.sock

	$(call colorize,3,"Checking gunicorn status...")
	sudo systemctl status gunicorn

	$(call colorize,3,"Checking nginx status...")
	sudo systemctl status nginx

	$(call colorize,3,"Checking PostgreSQL status...")
	sudo systemctl status postgresql
endif


logs:
ifneq ($(WHOAMI),schwetzen)
	$(call colorize,1,"Current environment incorrect.")
else
	$(call colorize,3,"Printing gunicorn logs...")
	sudo journalctl -u gunicorn.socket
endif


define colorize
	@tput setaf $1
	@echo $2
	@tput sgr0
endef
