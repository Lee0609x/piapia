FROM python:3.11
ADD . ./piapia
WORKDIR /piapia
CMD ["source", "venv/bin/activate"]
CMD ["python3", "deploy.py"]