#!/bin/bash
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm repo update

RELEASE=jhub
NAMESPACE=jhub

helm upgrade --install $RELEASE jupyterhub/jupyterhub \
      --namespace $NAMESPACE  \
      --version=0.9.0 \
      --values config.yaml
