# Package structure

A QuestionPy project resides in a single project directory. It requires a few essential files to function:

```
📂 PROJECT
┣ 📂 python
┃ ┗ 📂 NAMESPACE
┃   ┗ 📂 SHORTNAME
┃     ┗ 📄 __init__.py
┗ 📄 qpy_config.yml
```

!!! tip

    Use the [`questionpy-sdk create`][questionpy-sdk-create] command to generate an empty QuestionPy project scaffold.

  [questionpy-sdk-create]: ../getting_started/create_qtype.md#creating-a-project

A more complete folder structure is depicted below. It shows files and folders that may be part of a QuestionPy source
directory.

```
📂 PROJECT
┣ 📂 python
┣ 📂 static
┣ 📂 static-private
┣ 📂 resources
┣ 📂 js
┣ 📂 css
┣ 📂 lang
┣ 📄 qpy_config.yml
┗ 📄 ...
```

The following sections will delve deeper into the individual files and directories that may be included in a QuestionPy
package.

## Project configuration

**File:** `qpy_config.yml`

The project configuration file is described thoroughly on the [Configuration page].

  [Configuration page]: configuration.md

## Python code

**Directory:** `python`

```
┣ 📂 python
┃ ┣ 📂 NAMESPACE
┃ ┃ ┗ 📂 SHORTNAME
┃ ┃   ┣ 📄 __init__.py
┃ ┃   ┣ 📄 foo.py
┃ ┃   ┗ 📄 ...
┃ ┗ 📂 tests
┃   ┣ 📄 test_foo.py
┃   ┗ 📄 ...
```

The Python code for the project resides in the directory `python/NAMESPACE/SHORTNAME`, where `NAMESPACE` and
`SHORTNAME` should be replaced with the project's namespace and short name, respectively.

By default, the project's entry point is the function `NAMESPACE.SHORTNAME.init`. The module can be customized using the
[`entrypoint` option][entrypoint_option].

Feel free to create modules and sub-modules as needed. When utilizing external Python packages, ensure to include them
in your project using the [`requirements` option][requirements_option].

Under the directory `python/tests`, automated software tests can be stored.

  [entrypoint_option]: configuration.md#entrypoint
  [requirements_option]: configuration.md#requirements

## Static files

**Directory:** `static`

```
┣ 📂 static
┃ ┣ 📂 public
┃ ┃ ┣ 🖼️ image.jpg
┃ ┃ ┗ 🖼️ ...
┃ ┣ 📂 docs
┃ ┃ ┣ 📄 index.html
┃ ┃ ┗ 📄 ...
┃ ┣ 📂 screenshots
┃ ┃ ┣ 🖼️ screen1.png
┃ ┃ ┗ 🖼️ ...
┃ ┗ 🖼️ icon.svg
```

Commonly QuestionPy packages may contain raster images, vector graphics or any other static files. The place to store
those files is the directory `static/public`. Other static files include project documentation (`static/docs`),
screenshots (`static/screenshots`), and a [project icon] (`static/icon.svg`).

  [project icon]: configuration.md#icon

## Private static files

```
┣ 📂 static-private
┃ ┣ 🖼️ private-image.jpg
┃ ┗ 🖼️ ...
```

**Directory:** `static-private`

Sometimes it's desirable for static files to only be accessible after a specific progress in the task has been achieved,
for example, to illustrate a solution path. For this purpose, files can be stored in the `static-private` folder.

## Resources

**Directory:** `resources`

```
┣ 📂 resources
```

TODO

## JavaScript

**Directory:** `js`

```
┣ 📂 js
┃ ┣ 📄 module.js
┃ ┗ 📄 ...
```

This directory contains JavaScript files used for displaying questions. These can be statically defined or [dynamically
generated] during the build process, for example, using a bundler or transpiler.

  [dynamically generated]: building.md#build-hooks

## CSS

**Directory:** `css`

```
┣ 📂 css
┃ ┣ 📄 styles.css
┃ ┗ 📄 ...
```

CSS files for styling questions can be placed here. Like in the `js` folder, these files can also be dynamically
generated, for example, to use preprocessors like [Sass] or [Less.js].

  [Sass]: https://sass-lang.com/
  [Less.js]: https://lesscss.org/

## Translation files

**Directory:** `lang`

```
┣ 📂 lang
┃ ┣ 📂 en
┃ ┃ ┗ 📂 LC_MESSAGES
┃ ┃   ┣ 📄 domain.po
┃ ┃   ┗ 📄 ...
┃ ┣ 📂 de
┃ ┃ ┗ 📂 LC_MESSAGES
┃ ┃   ┣ 📄 domain.po
┃ ┃   ┗ 📄 ...
┃ ┗ 📂 ...
```

To translate content into different languages, [gettext] is used. Translations are maintained in so-called PO files.

  [gettext]: https://www.gnu.org/software/gettext/

## Additional files

```
┣ 📄 README.md
┣ 📄 package.json
┣ 📄 .gitignore
┣ 📄 .editorconfig
┗ 📄 ...
```

The project may include any additional files, such as `README.md`, `.gitignore`, `package.json`, or similar.
