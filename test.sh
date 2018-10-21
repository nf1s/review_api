#!/bin/bash
echo "Activating virtual environment .."
source ../venv/bin/activate

echo "run tests"
cd product
python manage.py test
~                 
