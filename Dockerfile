FROM jupyter/tensorflow-notebook:6d42503c684f

USER root

ENV GCSFUSE_REPO gcsfuse-stretch
RUN apt-get update && apt-get install --yes --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
  && echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" \
    | tee /etc/apt/sources.list.d/gcsfuse.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
  && apt-get update \
  && apt-get install --yes gcsfuse 

USER jovyan

COPY course_1.0 /tmp/course_1.0
