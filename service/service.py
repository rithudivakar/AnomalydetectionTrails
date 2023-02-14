from sklearn.ensemble import IsolationForest

class AnomalyDetectionService:
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(contamination=contamination)

    def fit(self, data):
        self.model.fit(data)

    def predict(self, data):
        return self.model.predict(data)
        