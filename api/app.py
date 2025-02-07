import boto3
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# client
client = boto3.client(
    service_name='bedrock-runtime',
    region_name=os.getenv('AWS_REGION')
)

@app.route('/api/ask', methods=['POST'])
def ask_bedrock():
    user_query = request.json.get('query')
    
    # ask bedrock
    response = client.invoke_model(
        modelId="amazon.titan-text-express-v1",
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "inputText": user_query,
            "textGenerationConfig": {
                "maxTokenCount": 8192,
                "stopSequences": [],
                "temperature": 0,
                "topP": 1
            }
        })
    )
    
    # return generated response
    return jsonify(response['body'].read().decode("utf-8"))

# @app.route('/hello', methods=['GET'])
# def hello_world():
#     return "Hello, World!"

@app.route('/health', methods=['GET'])
def hello_world():
    return "Healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
