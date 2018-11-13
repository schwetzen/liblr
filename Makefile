SRC_DIR  = src
ENV_PATH = ./$(SRC_DIR)/liblr/env.py


env: $(ENV_PATH)


.PHONY: $(ENV_PATH)
.SILENT: $(ENV_PATH)
$(ENV_PATH):
ifneq (,$(wildcard $(ENV_PATH)))
	$(call colorize,1,"Local env already exists at: $(ENV_PATH)")
else
	$(call colorize,1,"Creating default local env at: $(ENV_PATH)")
	touch $(ENV_PATH)
	echo "SECRET_KEY = 'super_secret'" >> $(ENV_PATH)
	echo "DATABASE = {" >> $(ENV_PATH)
	echo "    'ENGINE': 'django.db.backends.sqlite3'," >> $(ENV_PATH)
	echo "    'NAME': os.path.join(BASE_DIR, 'db.sqlite3')," >> $(ENV_PATH)
	echo "}" >> $(ENV_PATH)
	$(call colorize,2,"Done")
endif


define colorize
	@tput setaf $1
	@echo $2
	@tput sgr0
endef
