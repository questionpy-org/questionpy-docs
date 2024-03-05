# Installation

## Requirements

QuestionPy is a framework developed in Python.
Therefore, you need a compatible Python version installed.
A list of compatible versions can be found [here](faq.md#what-python-version-can-i-use-with-questionpy)

---

## Install QuestionPy SDK

To create your own question type, QuestionPy provides a Software Development Kit (SDK).


#### 1. Python and pip
Make sure that the Python interpreter can load QuestionPy’s code.
The most convenient way to do this is to use a virtual environment and [pip](https://pip.pypa.io/en/stable/).

If you need additional information about creating virtual environments see: 
[Creation of virtual environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

To confirm the virtual environment is activated, check the location of your Python interpreter:

##### Unix/macOS
```shell
which python
```

##### Windows
```shell
where python
```

While the virtual environment is active, the above command will output a filepath that includes the `.venv` directory

#### 2. Install SDK from GitHub

After creating and activating your virtual environment, you can install the _questionpy-sdk_ code with:
```shell
pip install git+https://github.com/questionpy-org/questionpy-sdk.git
```

#### 3. Verify Installation

You can verify that _questionpy-sdk_ was successfully installed by running:
```shell
questionpy-sdk -h
```

This should display the help section.

You are now ready to continue with the next step: [Create a QuestionType](create_qtype.md).
