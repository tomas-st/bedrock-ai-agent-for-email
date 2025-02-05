FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Set environment variables for AWS credentials (optional, recommended to use mounted volumes or secrets)
# ENV AWS_ACCESS_KEY_ID=your_access_key
# ENV AWS_SECRET_ACCESS_KEY=your_secret_key
# ENV AWS_DEFAULT_REGION=eu-central-1

# Define the command to run the chatbot
CMD ["python", "app.py"]