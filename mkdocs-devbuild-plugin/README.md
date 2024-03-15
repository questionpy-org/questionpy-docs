## mkdocs-devbuild-plugin

This mkdocs plugin allows to build the docs from *local development repositories* without manually touching the configuration. It overrides mkdocs's `nav` configuration and mkdocstrings Python handler `path` option.

### Options

- `enabled`: Enable/disable plugin (wired to `MKDOCS_DEV` env var in `mkdocs.yml`).

### Rationale

- *Why not just use [hooks](https://www.mkdocs.org/user-guide/configuration/#hooks)?*  
  Hooks run *after* other plugins. But we need the code to run *before* mkdocstrings and mkdocs-monorepo-plugin.
- *Why use symlinks? Why not point `!include` directly to `../common/mkdocs.yml`?*  
  mkdocs-monorepo-plugin doesn't allow to include files outside of the repository. Symlinks are created on-demand though, so they don't pollute the git file space.
