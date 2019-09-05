#!/bin/bash
echo "Activating virtual environment .."
source ../venv/bin/activate

echo "dump database fixtures to reviews/fixtures/initial_data.json"
python manage.py dumpdata --format=json reviews > reviews/fixtures/initial_data.json

echo "Done."