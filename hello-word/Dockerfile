# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY app.py .
COPY interface.py .
COPY model.pkl .

# Install required packages
RUN pip install -r requirements.txt

# Expose the ports for FastAPI (8000) and Gradio (7860)
EXPOSE 8000
EXPOSE 7860

# Command to start both FastAPI and Gradio using bash
CMD ["bash", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & python interface.py"]
#################################################################
# # Use official lightweight Python base image
# FROM python:3.11-slim

# # Set working directory
# WORKDIR /app

# # Copy dependencies and install them
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the script
# COPY model.py .

# # Run the script
# CMD ["python", "model.py"]
