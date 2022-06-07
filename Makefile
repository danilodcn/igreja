.PHONE: help
help:
	@echo "This is the help"


.PHONE: install
install:
	poetry install

.PHONE: clear
clear:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -path "*.egg-info*" -delete
	find . -type d -path "*.egg-info" -delete
	find . -type f -path "*.egg-info*" -delete
	find . -type d -path "*.egg-info" -delete
	rm -f ./.coverage

.PHONE: run
run:
	# ./manage.py collectstatic --no-input --clear
	./manage.py runserver

lint:
	@echo "Linting"
	isort .
	black .

tests:
	# - python -m unittest discover -s tests -v