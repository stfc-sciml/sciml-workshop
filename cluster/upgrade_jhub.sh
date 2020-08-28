#!/bin/bash
RELEASE=jhub
NAMESPACE=jhub

helm upgrade $RELEASE jupyterhub/jupyterhub \
      --namespace $NAMESPACE  \
      --version=0.9.0 \
      --values config.yaml
