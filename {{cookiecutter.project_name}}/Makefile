install: clean
	python setup.py sdist bdist_wheel
	pip install dist/*.whl

test:
	black --check .
	pytest --cov '{{cookiecutter.project_name}}' --cov-fail-under 95

format:
	black .

doc:
	pip install .[docs]
	sphinx-apidoc -f -o docsrc/source {{cookiecutter.project_name}}
	make -C docsrc github

clean:
	rm -rf build
	rm -rf dist
	rm -rf {{cookiecutter.project_name}}.egg-info
	find . -name *.pyc -delete
	find . -name __pycache__ -delete

coverage:
	coverage erase
	pytest --cov '{{cookiecutter.project_name}}'
	coverage html

version:
	bump2version --config-file .bumpversion.cfg $(BUMP)

all: install format coverage

