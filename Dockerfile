FROM python:3.11
ADD . ./piapia
WORKDIR /piapia
RUN pip install -r requirements.txt
CMD ["python3", "deploy.py"]