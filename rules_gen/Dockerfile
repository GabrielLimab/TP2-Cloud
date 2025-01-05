# The ML container will:

#     Run the playlist_rules_gen.py script.
#     Generate and save the recommendation model as a .pickle file.

# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY playlist_rules.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python", "playlist_rules.py"]