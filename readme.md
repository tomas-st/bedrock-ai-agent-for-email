# AWS Bedrock E-Mail Response Service

A e-mail response service that uses AWS Bedrock to automatically respond to customer inquiries. This open-source project demonstrates how to integrate generative AI into a simple application.

## Features
- Automatic response to e-mails using AWS Bedrock
- Utilizes Claude (Anthropic) as the AI model
- Example code in Python

## Prerequisites
- An AWS account with access to AWS Bedrock
- Python 3.x installed
- Enable the corresponding model for your AWS region on https://console.aws.amazon.com/bedrock/ (anthropic.claude-v2:1)
- We are using task instead of make (brew install go-task/tap/go-task)

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/tomas-st/bedrock-ai-agent-for-email.git
   cd bedrock-ai-agent-for-email
   ```
2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Make sure to have your AWS credentials setup:**
   ```sh
   aws configure
   ```

## Alternative local Installation with docker compose
   ```sh
   docker compose up -d
   ```

## Usage
### **Run the script**
Replace the AWS region if necessary and then execute the script:

```sh
python chatbot.py
```

## Possible Further Enhancements
- Integrate with a database for personalized responses
- Deploy as an AWS Lambda function
- Connect with Amazon Lex for voice recognition

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

## Contributing
Pull requests are welcome! Please open an issue before making significant changes.