from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


class ConfigError(ValueError):
    """Raised when Forge configuration is missing or invalid."""


@dataclass(frozen=True)
class RuntimeConfig:
    test_command: str | None = None
    lint_command: str | None = None


@dataclass(frozen=True)
class PathConfig:
    allowed_write: tuple[str, ...] = ()
    protected: tuple[str, ...] = ()


@dataclass(frozen=True)
class ForgeConfig:
    runtime: RuntimeConfig = field(default_factory=RuntimeConfig)
    paths: PathConfig = field(default_factory=PathConfig)


def load_config(root: Path) -> ForgeConfig:
    path = root / "forge.yml"
    if not path.exists():
        raise ConfigError("Missing forge.yml")

    data = _parse_simple_yaml(path.read_text(encoding="utf-8"))
    runtime = data.get("runtime", {})
    paths = data.get("paths", {})
    return ForgeConfig(
        runtime=RuntimeConfig(
            test_command=_optional_str(runtime.get("test_command")),
            lint_command=_optional_str(runtime.get("lint_command")),
        ),
        paths=PathConfig(
            allowed_write=tuple(paths.get("allowed_write", [])),
            protected=tuple(paths.get("protected", [])),
        ),
    )


def _optional_str(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ConfigError("Configured commands must be strings")
    return value.strip() or None


def _parse_simple_yaml(text: str) -> dict[str, object]:
    """Parse the tiny YAML subset used by forge.yml.

    Supported shapes are top-level sections, scalar key/value pairs, and lists
    nested one level under a section. This keeps bootstrap dependency-free.
    """
    result: dict[str, object] = {}
    current_section: str | None = None
    current_list_key: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        if indent == 0 and stripped.endswith(":"):
            current_section = stripped[:-1]
            current_list_key = None
            result[current_section] = {}
            continue

        if current_section is None:
            raise ConfigError(f"Invalid config line: {raw_line}")

        section = result[current_section]
        if not isinstance(section, dict):
            raise ConfigError(f"Invalid section: {current_section}")

        if indent == 2 and stripped.endswith(":"):
            current_list_key = stripped[:-1]
            section[current_list_key] = []
            continue

        if stripped.startswith("- "):
            if current_list_key is None:
                raise ConfigError(f"List item without key: {raw_line}")
            values = section[current_list_key]
            if not isinstance(values, list):
                raise ConfigError(f"Invalid list key: {current_list_key}")
            values.append(_strip_quotes(stripped[2:].strip()))
            continue

        if ":" in stripped:
            key, value = stripped.split(":", 1)
            current_list_key = None
            section[key.strip()] = _parse_scalar(value.strip())
            continue

        raise ConfigError(f"Invalid config line: {raw_line}")

    return result


def _parse_scalar(value: str) -> object:
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    return _strip_quotes(value)


def _strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value
