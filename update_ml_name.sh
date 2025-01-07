#!/bin/bash

# Generate a unique identifier (timestamp)
UNIQUE_ID=$(date +%s)

# Replace the placeholder in the YAML file
sed -i "s/{{unique-id}}/$UNIQUE_ID/" ml_job.yaml

# Commit and push the changes
git add ml_job.yaml
git commit -m "Update Job name with unique ID: $UNIQUE_ID"
git push origin main
