#!/usr/bin/env python3

import logging
import pickle as pkl
import numpy as np
from typing import Dict, Tuple
import connexion
from sklearn.pipeline import Pipeline
import gzip

logging.basicConfig(level=logging.INFO, format=u'%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s')


def health() -> Tuple[Dict[str, str], int]:
    return {"health_status": "running"}, 200


def load_model() -> Pipeline:
    with gzip.GzipFile('model.pkl', 'r') as fhandler:
        model_object = pkl.load(fhandler)
        return model_object


model = load_model()


def predict():
    feature_selector = ['X%i' % i for i in range(5)]
    _data = connexion.request.json
    logging.info("Request body : %s" % _data)
    _vector = np.array([_data[feature] for feature in feature_selector]).reshape(1, -1)
    _prediction = model.predict_proba(_vector)[0, 1]
    return {"user_id": _data["user_id"], "prediction": _prediction}, 200


app = connexion.App(__name__)
app.add_api("swagger.yaml")

application = app.app

if __name__ == "__main__":
    app.run(8080, server="gevent")
