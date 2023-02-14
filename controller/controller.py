import sys
sys.path.append('/home/rithuparnakd/projectData/phase2Training/PythonPrograms/anomalyDetectionTrail/entities')
from entities.entities import Data
sys.path.append('/home/rithuparnakd/projectData/phase2Training/PythonPrograms/anomalyDetectionTrail/repository')
from repository.repository import DataRepository

sys.path.append('/home/rithuparnakd/projectData/phase2Training/PythonPrograms/anomalyDetectionTrail/service')
from service.service import AnomalyDetectionService

class AnomalyController:
    def __init__(self, file_path, contamination=0.1):
        self.data_repository = DataRepository(file_path)
        self.anomaly_detection_service = AnomalyDetectionService(contamination)

    def detect_anomalies(self):
        data = self.data_repository.get_data()
        self.anomaly_detection_service.fit(data)
        y_pred = self.anomaly_detection_service.predict(data)
        data["anomaly_score"] = y_pred
        anomalies = data[data["anomaly_score"] == -1]
        return anomalies