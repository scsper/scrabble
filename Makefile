clean:
	rm -rf *.pyc
	rm -rf unit_tests/*.pyc

install:
	sudo apt-get install python-pip
	sudo apt-get install vim
	sudo pip install coverage
	sudo pip install mock

set_python_path:
	PYTHONPATH="${PYTHONPATH}:/vagrant"
	export PYTHONPATH

test:
	python unit_tests/RunTest.py
	make clean

run:
	python run.py
	make clean

coverage:
	coverage run --source='.' unit_tests/RunTest.py
	coverage html