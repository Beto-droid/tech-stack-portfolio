# Start from a base image
FROM 3.13.0-slim-bullseye

# Set up working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Set the entry point for Celery (for example)
CMD ["celery", "-A", "TechStackPortfolio", "worker", "--loglevel=info"]