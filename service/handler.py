import json
from service.main import app
from serverless_wsgi import handle_request

def lambda_handler(event, context):
    response = handle_request(app, event, context)
    return response