FROM python:3.11
ADD . ./piapia
WORKDIR /piapia
VOLUME ["/piapia/logs", "/piapia/sqlite/db"]
RUN pip install -r requirements.txt
CMD ["python3", "deploy.py", "DEPLOY_ENV=prod"]