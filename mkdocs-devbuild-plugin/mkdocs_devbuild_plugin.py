import re
from contextlib import suppress
from pathlib import Path

from mkdocs.config import base, config_options
from mkdocs.plugins import BasePlugin


class DevBuildPluginConfig(base.Config):
    enabled = config_options.Type(bool, default=False)


class DevBuildPlugin(BasePlugin[DevBuildPluginConfig]):
    """Override nav tree in dev mode."""

    def on_config(self, config):
        if self.config.enabled:
            return self._override_config(config)

        return config

    def _override_config(self, config):
        self._ensure_symlinks()
        config["site_name"] = f"{config['site_name']} (dev)"
        config["nav"] = self._override_nav_item(config["nav"])
        return self._override_mkdocstrings_handlers(config)

    def _override_mkdocstrings_handlers(self, config):
        config_paths = config["plugins"]["mkdocstrings"].config.handlers["python"]["paths"]
        for idx, path in enumerate(config_paths):
            config_paths[idx] = re.sub(r"^questionpy-(.+)$", r"questionpy-\1-dev", path)
        return config

    def _override_nav_item(self, item):
        if isinstance(item, str) and item.startswith("!include"):
            return self._rewrite_nav_value(item)
        if isinstance(item, list):
            return [self._override_nav_item(_item) for _item in item]
        if isinstance(item, dict):
            for k, v in item.items():
                item[k] = self._override_nav_item(v)
        return item

    @staticmethod
    def _rewrite_nav_value(key):
        return re.sub(r"^\!include\s+\./questionpy-(.+)/mkdocs\.yml$", r"!include ./questionpy-\1-dev/mkdocs.yml", key)

    @staticmethod
    def _ensure_symlinks():
        docs_path = Path(__file__).parent / ".." / ".."
        for repo in ("common", "sdk", "server"):
            dst = docs_path / f"questionpy-{repo}-dev"
            target = Path("..") / repo
            with suppress(FileExistsError):
                dst.symlink_to(target)
