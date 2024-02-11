#!/bin/sh

pip-compile --generate-hashes --output-file=requirements.txt --strip-extras --upgrade pyproject.toml
pip-compile --extra=dev,test --output-file=dev-requirements.txt --strip-extras --upgrade pyproject.toml
