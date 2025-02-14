from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function for EDA
def perform_eda(df):
    eda_results = {}
    eda_results['head'] = df.head().to_html()
    eda_results['describe'] = df.describe().to_html()
    eda_results['info'] = df.info(buf=None)
    
    # Correlation matrix plot
    plt.figure(figsize=(10, 8))
    corr = df.corr()
    plt.matshow(corr, fignum=1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.colorbar()
    plt.title('Correlation Matrix', pad=20)
    corr_plot_path = os.path.join(UPLOAD_FOLDER, 'corr_matrix.png')
    plt.savefig(corr_plot_path)
    plt.close()
    eda_results['corr_matrix'] = corr_plot_path
    
    return eda_results

# Helper function for prediction
def make_prediction(df):
    if 'Close' not in df.columns:
        return 'Column "Close" not found in data.'
    
    # Example: Simple Linear Regression on Close price
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].map(pd.Timestamp.toordinal)
    
    X = df[['Date']]
    y = df['Close']
    
    model = LinearRegression()
    model.fit(X, y)
    df['Prediction'] = model.predict(X)
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Close'], label='Actual Close Price')
    plt.plot(df['Date'], df['Prediction'], label='Predicted Close Price', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    prediction_plot_path = os.path.join(UPLOAD_FOLDER, 'prediction.png')
    plt.savefig(prediction_plot_path)
    plt.close()
    
    return prediction_plot_path

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('home'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home'))
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    df = pd.read_csv(file_path)
    eda_results = perform_eda(df)
    prediction_plot = make_prediction(df)
    
    return render_template('results.html', eda_results=eda_results, prediction_plot=prediction_plot)

if __name__ == '__main__':
    app.run(debug=True)
