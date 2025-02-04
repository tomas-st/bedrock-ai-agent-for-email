import boto3

# client
client = boto3.client(service_name='bedrock-runtime', region_name='eu-central-1')

# customer query
user_query = "Wie lange dauert der Versand meiner Bestellung?"

# ask bedrock
response = client.invoke_model(
    modelId="anthropic.claude-v2:1",  # Claude AI von Anthropic
    contentType="application/json",
    accept="application/json",
    body=f'{{"prompt": "{user_query}", "max_tokens_to_sample": 100}}'
)

# print generated response
print(response['body'].read().decode("utf-8"))
