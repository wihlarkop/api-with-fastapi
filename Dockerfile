FROM ubuntu:latest
LABEL authors="Edo"

ENTRYPOINT ["top", "-b"]