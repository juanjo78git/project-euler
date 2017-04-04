init:
	pip install -r requirements.txt

test:
	python -m unittest 'tests/test_projecteuler.py' -v

testpypy:
	pypy -m unittest 'tests/test_projecteuler.py' -v

coverage:
	coverage erase
	coverage run -a -m unittest 'tests/test_projecteuler.py'
	coverage html

flake8:
	flake8 projecteuler
