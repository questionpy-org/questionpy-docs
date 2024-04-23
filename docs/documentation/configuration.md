# Configuration

The project is configured via a `qpy_config.yml` file located at the project's root, utilizing the [YAML format].

  [YAML format]: https://yaml.org/

!!! example "Example `qpy_config.yml`"

    ```yaml
    short_name: my_project
    namespace: my_namespace
    version: 0.1.0
    api_version: "0.1"
    author: Jane Smith <jane.smith@example.com>
    name:
      de: Mein QuestionPy-Projekt
      en: My QuestionPy Project
    languages: [de, en]
    ```

The table below outlines the available configuration options:

| Name           | Description                           | Type                                              | Required?  |
| -------------- | ------------------------------------- | ------------------------------------------------- | :--------: |
| `short_name`   | [Short name](#short_name)             | String                                            | ✅         |
| `namespace`    | [Namespace](#namespace)               | String                                            | ✅         |
| `version`      | [Version](#version)                   | String                                            | ✅         |
| `api_version`  | [Required API version](#api_version)  | String                                            | ✅         |
| `name`         | [Project name](#name)                 | Dictionary of strings                             | ✅         |
| `author`       | [Author](#author)                     | String                                            | ✅         |
| `description`  | [Project description](#description)   | Dictionary of strings                             |            |
| `languages`    | [Supported languages](#languages)     | List of strings                                   |            |
| `url`          | [Project URL](#url)                   | String                                            |            |
| `icon`         | [Project icon](#icon)                 | String                                            |            |
| `license`      | [Project license](#license)           | String                                            |            |
| `tags`         | [Project tags](#tags)                 | List of strings                                   |            |
| `entrypoint`   | [Package entry point](#entrypoint)    | String                                            |            |
| `type`         | [Package type](#type)                 | `QUESTIONTYPE` (default), `QUESTION` or `LIBRARY` |            |
| `permissions`  | [Package permissions](#permissions)   | List of strings                                   |            |
| `requirements` | [Package requirements](#requirements) | String or list of strings                         |            |
| `build_hooks`  | [Build hooks](#build_hooks)           | String dictionary or list of strings dictionary   |            |

## `short_name`

The short name is a unique identifier within the [namespace](#namespace). Ensure that:

- it contains only lowercase alphanumeric characters and underscores,
- it is 1 to 127 characters long,
- it does not start with a number,
- it is a valid Python identifier, and
- it is **not** a [reserved Python keyword].

  [reserved Python keyword]: https://docs.python.org/3.12/reference/lexical_analysis.html#keywords

## `namespace`

The package namespace helps you organize your QuestionPy packages to prevent name conflicts. It must follow the same
naming conventions as the [short name](#short_name). Consider using your organization's name for clarity.

## `version`

Ensure that the package version adheres to the [Semantic Versioning convention].

  [Semantic Versioning convention]: https://semver.org/

## `api_version`

The minimum compatible version of the QuestionPy API your package supports.

## `name`

The long package name, localized for all supported languages.

## `author`

The project author. Recommended format: `NAME <EMAIL>`.

## `description`

The package description, localized for all supported languages.

## `languages`

A list of supported languages ([ISO 639 two-letter code]).

  [ISO 639 two-letter code]: https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes

## `url`

A URL pointing to the project homepage.

## `icon`

The project icon can be specified either as a relative path (e.g., `static/icon.svg`) or as a URL (e.g.,
`https://example.com/icon.svg`).

## `license`

The license your project is released under, preferably using a [SPDX License identifier].

  [SPDX License identifier]: https://spdx.org/licenses/

## `tags`

A list of tags, categorizing your project.

## `entrypoint`

The project entry point is a Python module name which is relative to `NAMESPACE.SHORTNAME`. If not specified it defaults
to `NAMESPACE.SHORTNAME` itself (`python/NAMESPACE/SHORTNAME/__init__.py`). The entry point is expected to have a
function named `init`.

!!! example

    Set the entry point to `custom_entrypoint` for the entry point to be `my_namespace.my_question.custom_entrypoint`,
    given a namespace `my_namespace` and a short name `my_question`.

## `type`

QuestionPy packages can be of type `QUESTIONTYPE` (default), `LIBRARY` or `QUESTION`.

## `permissions`

TODO

## `requirements`

The field lists all Python requirements your package has. It can be either a relative path to a [requirements file]
(e.g., `requirements.txt`) or a list of [requirement specifiers].

  [requirements file]: https://pip.pypa.io/en/stable/reference/requirements-file-format/
  [requirement specifiers]: https://pip.pypa.io/en/stable/reference/requirement-specifiers/

## `build_hooks`

QuestionPy can run arbitrary commands before and after the build process.

See [Build hooks](building.md#build-hooks) for more information.
