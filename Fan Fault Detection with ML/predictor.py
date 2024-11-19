import pickle
class MLModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()
    def load_model(self):
        with open(self.model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    def predict(self, inp):
        return self.model.predict(inp)
    def destroy(self):
        self.model = None


def load_model(path):
    return MLModel(path)
def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

def dstAll(model):
    model.destroy()
    return 'ok'