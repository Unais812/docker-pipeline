FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY count.py .
RUN pip install flask redis 

# Copy code
COPY . .

# Expose Flask port
EXPOSE 5002

# Run Flask app
CMD ["python", "count.py"]