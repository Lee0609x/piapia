FROM python:3.11
ADD . ./training
WORKDIR /training
RUN pip install -r requirements.txt
CMD ["python3", "deploy.py"]