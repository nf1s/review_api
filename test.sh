#!/bin/bash
echo "Activating virtual environment .."
source ../venv/bin/activate

echo "run tests"
python manage.py test
~                 
