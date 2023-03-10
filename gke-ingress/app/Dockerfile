FROM python:3.9

# Set up working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY app.py .

EXPOSE 80

# Set the entrypoint for the container
ENTRYPOINT ["python", "app.py"]
