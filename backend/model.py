import joblib
import pandas as pd

def load_model():
    bundle = joblib.load('rfc_pipeline.pkl')
    rfc_model = bundle['model']
    scaler_loaded = bundle['scaler']
    
    return rfc_model, scaler_loaded


def load_data():
    # Load the data into a DataFrame
    df = pd.read_csv('TheWorldOverHeaven.csv')
    X = df.drop(columns=['Label'])
    
    return X

def predict(data):
    model, scaler = load_model()
    test = data.reshape(1, -1)
    # X_scaled = scaler.transform(data)

    predictions = model.predict(test)
    
    return predictions
    
if __name__ == '__main__':
    data = load_data().iloc[0].values
    print(predict(data))
    