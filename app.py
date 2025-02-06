import boto3
import json

# client
client = boto3.client(service_name='bedrock-runtime', region_name='eu-central-1')

# customer query
user_query = "Warum ist die Erde rund?"

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

# print generated response
print(response['body'].read().decode("utf-8"))
