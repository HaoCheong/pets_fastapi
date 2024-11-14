#!/bin/bash

# Runs all the unit tests available

echo "========== RUNNING UNIT TESTS =========="
python3 -m pytest -v tests/unit/*_tests.py