# Create a Question Type

Before you can create your first question type, make sure you have _questionpy-sdk_ installed 
(see [Installation](installation.md)).

## Creating a project

For your first time using QuestionPy, we recommend running the `create` command. 
This command will create the basic layout for a question type, so you don't have to worry about the initial setup.

```shell
questionpy-sdk create my_qtype
```

This will create the **my_qtype** directory in your current directory. 

When choosing a name for your project, make sure you follow the naming rules listed 
[here](../reference/common/manifest.md#questionpy_common.manifest.ensure_is_valid_name).

To learn more about the project structure see the Information listed in the 
[Package Structure](../documentation/package_structure.md) Section.

## The Options Form

The options form provides a way for instructors to customize your question type and create actual questions. 
With the options form, you can define which aspects of your question type are customisable. 

The project you just created, has already some _elements_ defined in the `form.py` file. 
This is also the location where you can add your own _elements_. 

You can define a new _static_text_ element by adding:

```python
description = static_text(
    label="My QType Description", 
    text="""This is a description for my first question type""")
```

This will create a non-editable text in your options form.

## Run your question type locally

To test your newly created question type, you have to package your project into a `.qpy` file. 

```shell
questionpy-sdk package my_qtype
```

You should see a new `.qpy` file in your directory with your projects shortname and version in the file name.
Depending on your shortname and version you chose you have to adjust the command to run the local webserver.
If you didn't change any settings from the manifest, you should be able to run you package with the following command:

```shell
questionpy-sdk run local-my_qtype-0.1.0.qpy 
```
