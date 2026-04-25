# Lipstick

A lightweight matplotlib visualization utility library. Keeps things simple — convenience over abstraction.

## Setup

```bash
uv sync --group dev   # installs lipstick + dev tools (jupyter, seaborn, etc.)
```

## Project Structure

```
src/lipstick/
├── animations.py     # GifMaker (context manager), update_fig
├── bar_plots.py      # cumulative_bar
├── scatter_plots.py  # scatter_diag, scatter_hist
└── grid.py           # place_axes_on_grid, add_axis
```

Public API is exported from `__init__.py`. All functions return `(fig, ax)` tuples for matplotlib interoperability.

## Release Workflow

Releases are automated via GitHub Actions. To ship a new version:

1. Bump `version` in `pyproject.toml`
2. Commit, tag, and push:
```bash
git commit -am "bump version to x.x.x"
git tag vx.x.x
git push origin main --tags
```

The CI workflow (`.github/workflows/publish.yml`) builds and publishes to PyPI automatically on tag push using OIDC trusted publishing — no tokens needed.

## Conventions

- All public functions return `(fig, ax)` or `(fig, axes)` for matplotlib interoperability
- Dependencies must be on PyPI — no git URL dependencies (PyPI rejects them)
- Keep the public API small; don't add functions without clear use cases

## Open Backlog (see GitHub issues)

- #10 Tests + CI for PRs
- #11 Type hints
- #12 Bump `requires-python` to `>=3.8`
- #13 Style/theme system
- #14 Richer `scatter_hist` (KDE, correlation annotation)
- #15 Heatmap function
- #16 Better README
- #8 Clean up `scatter_hist` return value
- #1 MP4 export for animations
