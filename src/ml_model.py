from sklearn.svm import SVC
import joblib


class MLModel:
    def __init__(self):
        self.model = SVC(kernel='linear')

    def load_model(self, path):
        self.model = joblib.load(path)

    def predict(self, image):
        return self.model.predict(image)
