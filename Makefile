# Including commands
run-django-server:
	poetry run task runserver

install-backend:
	poetry run pip install -U setuptools
	poetry install --no-root

.PHONY: createadmin
createadmin:
	poetry run task manage createadmin

.PHONY: migrate
migrate:
	poetry run task migrate

# Primary commands
.PHONY: install
install:
	@make -j 2 install-backend
	poetry run task manage initconfig --debug
	@make migrate
	poetry run task manage createadmin

.PHONY: run
run:
	@make -j 2 run-django-server
