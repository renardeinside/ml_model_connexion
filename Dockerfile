FROM python:3.6-slim

# import & setup packages
ADD requirements.in requirements.txt
RUN pip install -r requirements.txt

# import all files
RUN mkdir /opt/model_server
WORKDIR /opt/model_server
ADD ./app.py app.py
ADD ./model.pkl model.pkl
ADD ./swagger.yaml swagger.yaml


CMD python app.py