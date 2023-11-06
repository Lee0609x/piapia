FROM python:3.11
ADD . ./piapia
WORKDIR /piapia
CMD ["python3", "deploy.py"]