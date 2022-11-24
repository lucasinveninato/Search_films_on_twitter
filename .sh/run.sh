#!/bin/bash
python -m src.main
aws s3 sync "./src/output" "s3://top_10_actors_tweets"

