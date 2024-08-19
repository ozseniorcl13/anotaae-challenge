#!/bin/bash
echo 'Running server...'

echo "$ENV"

if [ "$ENV" = "dev" ]; then
    echo 'Dev mod'
    python3 -m debugpy --listen 0.0.0.0:9999 main.py --reload
else
    echo 'Prod mod'
    python3 main.py
fi
