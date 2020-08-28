#!/bin/bash

gcloud container clusters create \
    --machine-type n1-standard-2 \
    --num-nodes 2 \
    --zone europe-west2-a \
    --node-locations europe-west2-a \
    --cluster-version latest \
    sciml-workshop
