#!/bin/bash
echo "Activating virtual environment .."
source ../venv/bin/activate

echo "dump database fixtures to reviews/fixtures/initial_data.json"
python product/manage.py dumpdata --format=json reviews > product/reviews/fixtures/initial_data.json

echo "Done."