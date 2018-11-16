import pandas as pd
from sklearn.datasets import make_classification
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import pickle as pkl
import gzip


class ModelBuilder:
    def __init__(self):
        self.n_samples = 100000
        self.n_features = 5

    def run(self):
        print("Model creation started")

        X, y = make_classification(self.n_samples, self.n_features, random_state=42)
        model = Pipeline(steps=[
            ('scaler', StandardScaler()),
            ('clf', RandomForestClassifier())
        ])

        params = {
            "clf__n_estimators": [10, 20, 50]
        }

        X = pd.DataFrame(X, columns=['X%i' % i for i in range(5)])

        gsearch = GridSearchCV(model, param_grid=params, cv=2)
        gsearch.fit(X, y)

        _best_model = gsearch.best_estimator_

        print("Saving model to the disk")

        with gzip.GzipFile('model.pkl', 'w') as fhandler:
            pkl.dump(_best_model, fhandler)

        print("Model written")


if __name__ == '__main__':
    builder = ModelBuilder()
    builder.run()
