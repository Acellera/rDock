# rDock

rDock is a fast, versatile and open-source program for docking ligands to proteins and nucleic acids.
This is Acellera's fork of [CBDD/rDock](https://github.com/CBDD/rDock), with improvements to tethered docking and several crash fixes.
The user guide and getting started guide are in `docs/`.

## Installation

```
pip install acellera-rdock
```

Wheels are available for Linux x86_64.
This puts the rDock programs (`rbdock`, `rbcavity`, `rblist`, ...) and the `sd*` tools on your PATH and sets `RBT_ROOT` for them, so no environment setup is needed.
The Perl tools (`sdsort`, `sdfilter`, `sdreport`, ...) need a system `perl`.

## Building from source

You need a C++ compiler and the popt headers (`popt-devel` or `libpopt-dev`).

```
pip install .
pytest tests/
```

## Releasing

Bump `version` in `pyproject.toml` and push to `main`.
CI builds and tests the wheel with cibuildwheel and uploads it to PyPI.
