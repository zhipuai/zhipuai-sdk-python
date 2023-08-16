all:

format: install
	autoflake -r -i zhipuai tests
	isort -rc zhipuai tests
	black zhipuai tests

dist: clean ## builds source and wheel package
	python3 setup.py sdist bdist_wheel
	ls -l dist

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

install:
	pip3 install autoflake isort black