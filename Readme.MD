# To use this boiler plate, follow the script.
 - python3 -m venv venv | Create venv
 - soure venv/bin/activate | Activate venv
 - pip install -r requirements.txt | Install dependencies
 - pre-commit install | Install pre-commit into .git file

<p><b> If everything was configured.</b></p>


### Mypy
 - pip install mypy
 - Typechecker
 - mypy <file.py>

### Pylint
 - pip install pylint
 - pylint --generate-rcfile 
 - take the output and create .pylintrc

### Pre commit
 - pip install pre-commit
 - pre-commit install
 - use the sample file .pre-commit-config.yaml
 - pre-commit hook with pylint and mypy
