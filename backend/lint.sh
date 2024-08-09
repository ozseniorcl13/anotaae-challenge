#!/bin/bash

echo "Running Flake8..."
flake8 .

echo "Running Black..."
black .

echo "Running Isort..."
isort .
