from pathlib import Path
import nbformat


def test_readme_exists():
    assert Path("README.md").is_file()


def test_ipynb_files_exist():
    assert Path("18_Sep_Python Basics Variable.ipynb").is_file()
    assert Path("9_Sep_Python Basics Variable.ipynb").is_file()


def test_notebooks_parseable():
    for p in ["18_Sep_Python Basics Variable.ipynb","9_Sep_Python Basics Variable.ipynb"]:
        nb = nbformat.read(p, as_version=4)
        assert nb is not None
        assert 'cells' in nb
