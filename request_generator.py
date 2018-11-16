import pandas as pd
from sklearn.datasets import make_classification
import grequests
from uuid import uuid4


class RequestsGenerator:
    def __init__(self, n_requests=100):

        self.endpoint = "http://localhost:8080/predict"
        self.N_SAMPLES = n_requests
        self.N_FEATURES = 5

    def generate_requests(self):
        _data, _ = make_classification(n_samples=self.N_SAMPLES, n_features=self.N_FEATURES, random_state=42)
        _data = pd.DataFrame(_data, columns=["X%i" % i for i in range(self.N_FEATURES)])

        # prepare requests data
        request_stack = [_data.ix[i, :].to_dict() for i in range(self.N_SAMPLES)]

        # add user id
        for d in request_stack:
            d.update({"user_id": str(uuid4())})

        # generate request objects

        hooks = []

        for rs in request_stack:
            _hook = grequests.post(self.endpoint, json=rs)
            hooks.append(_hook)
        return hooks

    def run(self):
        hooks = self.generate_requests()
        print("Starting requests load ")
        start = pd.datetime.now()
        grequests.map(hooks)
        end = pd.datetime.now()
        delta = end-start
        print("Time delta: %s" % delta)
        print("Total %i requests in %0.4f seconds, %0.5f RPS" % (self.N_SAMPLES,
                                                                 delta.total_seconds(),
                                                                 self.N_SAMPLES/delta.total_seconds()))


if __name__ == '__main__':
    load_types = [20, 100, 1000, 2000, 4000]
    for load_type in load_types:
        print("Testing %i requests" % load_type)
        generator = RequestsGenerator(n_requests=load_type)
        generator.run()
