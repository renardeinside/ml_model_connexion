FROM continuumio/miniconda3

# import & setup packages
RUN /opt/conda/bin/pip install --upgrade pip
ADD ./requirements.txt requirements.txt
RUN /opt/conda/bin/conda install --yes --file requirements.txt
RUN /opt/conda/bin/pip install connexion[swagger-ui]==2.0.2

# import all files
RUN mkdir /opt/model_server
WORKDIR /opt/model_server
ADD ./app.py app.py
ADD ./model.pkl model.pkl
ADD ./swagger.yaml swagger.yaml


CMD /opt/conda/bin/python app.py