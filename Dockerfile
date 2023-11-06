FROM python:3.11
ADD . ./piapia
WORKDIR /piapia
RUN source source venv/bin/activate
CMD ["python3", "deploy.py"]