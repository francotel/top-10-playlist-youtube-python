# Use the official Python 3 image as the base
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the Python code and requirements into the container
COPY top-10-playlist.py /app
COPY requirements.txt /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for the API key
ENV YT_API_KEY="YOUR_YOUTUBE_API_KEY"
ENV PLAYLIST_ID="PLAYLIST_ID"

# Command to execute your Python script
CMD ["python", "top-10-playlist.py"]