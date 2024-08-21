# Define base image
FROM python:3.10

# Copy contents into image
COPY . /app

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Port
EXPOSE 8000

# Run
CMD ["uvicorn", "app:app", "--host", "localhost", "--port", "8000"]
