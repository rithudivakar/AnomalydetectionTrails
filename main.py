import sys
sys.path.append('/home/rithuparnakd/projectData/phase2Training/PythonPrograms/anomalyDetectionTrail/controller')
from controller.controller import AnomalyController

controller = AnomalyController("/home/rithuparnakd/projectData/phase2Training/PythonPrograms/anomalyDetectionTrail/data/creditcard.csv")
anomalies = controller.detect_anomalies()
print("Anomalies are : ")
print(anomalies)
