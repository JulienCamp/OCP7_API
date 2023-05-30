from flask import Flask, jsonify, request
import joblib
import pandas as pd
import os
#import shap

app = Flask(__name__)

# Charger le modèle et les données
# MODELS_PATH = "./models/"
# DATA_PATH = "./data/"

path = os.path.join('models', 'best_model.joblib')
with open(path, 'rb') as file:
    model = joblib.load(file)

path = os.path.join('models', 'cal_best_model.joblib')
with open(path, 'rb') as file:
    cal_model = joblib.load(file)

path = os.path.join('data', 'test_data.joblib')
with open(path, 'rb') as file:
    data = joblib.load(file)

# model = joblib.load(MODELS_PATH + "best_model.joblib")
# cal_model = joblib.load(MODELS_PATH + "cal_best_model.joblib")
# data = joblib.load (DATA_PATH + "test_data.joblib")

# def get_shap(client_data) :

#     #explainer = shap.TreeExplainer(model['classifier'])
#     # Get the feature names (lost during scaling)
#     column_transformer = model.named_steps['transformers']
#     feature_names = column_transformer.get_feature_names_out()
    
#     # create preprocessed array from the line of dataframe which corresponds to the client
#     X_t = model['transformers'].transform(client_data)
#     # create preprocessed dataframe from preprocessed array
#     X_t_df = pd.DataFrame(X_t, columns=feature_names)
#     chosen_instance = X_t_df
#     shap_values = explainer.shap_values(chosen_instance)
#     shap_values_list = [arr.tolist() for arr in shap_values]

    
#     return shap_values_list

@app.route("/")
def index():
    return "API loaded"

@app.route('/api/prediction', methods=['POST'])
def prediction():
    # Get the POST request data
    client_id = request.json['client_id']
    model_type = request.json['model_type']
    credit_amount = request.json['credit_amount']
    
    client_data = data[data["SK_ID_CURR"] == client_id]
    client_data['AMT_CREDIT'] = credit_amount

    # Make the prediction
    if model_type == "default" :
        prediction = model.predict(client_data)
        confidence = model.predict_proba(client_data)
#        shap_values = get_shap(client_data)
    else :
        prediction = cal_model.predict(client_data)
        confidence = cal_model.predict_proba(client_data)
#       shap_values = get_shap(client_data)
    print("dbg3")
    print("prediction=" , prediction[0])

    # Return the prediction as JSON
    return jsonify({'prediction': str(prediction[0]),
                    'confidence' : str(confidence[0][1])
                    #'shap_values' : shap_values
                    })
    
if __name__ == '__main__':
    app.run(debug=True)