# Use a lightweight Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask flask-cors

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
