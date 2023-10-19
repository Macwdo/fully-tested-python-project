# Python project boiler plate
- In this project we are using only linters and checkers.
- Mypy, Pylint.
- We are using pre-commit too.

---

### Some warnings.
You should configure your .pylintrc to match your preferences.

Mypy was configured in the pre-commit config file using the --strict flag:

    mypy --strict
This instructs Mypy to use the strict checker, you can make change too.

### To use this boilerplate, follow the script.
 - python3 -m venv venv | Create a venv
 - soure venv/bin/activate | Activate the venv
 - pip install -r requirements.txt | Install dependencies
 - pre-commit install | Install pre-commit the into .git file

<p>
    <h4><b> If everything was configured.</b></h4>
    When you make a commit you should see something like this

    pylint...................................................................Passed

    mypy.....................................................................Passed
         
Most likely, everything was configured successfully.

</p>
 


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
