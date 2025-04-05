# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir qrcode[pil] python-dotenv validators

# Set environment variable (replace with your actual repo)
ENV GITHUB_REPO_URL=https://github.com/satyavinay5566/Homework-7

# Run the app
CMD ["python", "app.py"]
