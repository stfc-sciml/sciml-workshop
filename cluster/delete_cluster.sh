#!/bin/bash

helm delete jhub --purge
kubectl delete namespace jhub
gcloud container clusters delete sciml-workshop --zone=europe-west2-a
