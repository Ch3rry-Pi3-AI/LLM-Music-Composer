# ------------------------------------------------------------
# Base Image
# ------------------------------------------------------------
# Use the lightweight Python 3.12 slim image.
# This keeps the container small while providing everything
# needed to run the Streamlit music composer application.
FROM python:3.12-slim


# ------------------------------------------------------------
# Working Directory
# ------------------------------------------------------------
# Set the working directory inside the container.
# All subsequent commands (COPY, RUN, CMD, etc.) will operate here.
WORKDIR /app


# ------------------------------------------------------------
# Copy Project Files
# ------------------------------------------------------------
# Copy the entire project directory from the host to the container.
# This includes the application code, setup.py, requirements, etc.
COPY . .


# ------------------------------------------------------------
# Install Dependencies
# ------------------------------------------------------------
# Install all Python dependencies using the editable install (-e .).
# --no-cache-dir prevents pip from storing cached wheels,
# keeping the final image as small as possible.
RUN pip install --no-cache-dir -e .


# ------------------------------------------------------------
# Environment Variables
# ------------------------------------------------------------
# Ensure Python imports recognise the root directory.
# This allows "app.*" modules to be imported without issues.
ENV PYTHONPATH=.


# ------------------------------------------------------------
# Expose Streamlit Port
# ------------------------------------------------------------
# Streamlit runs on port 8501 by default.
# Expose it so external systems (Docker host, Kubernetes) can access the UI.
EXPOSE 8501


# ------------------------------------------------------------
# Start the Application
# ------------------------------------------------------------
# Run the Streamlit app.
# --server.address=0.0.0.0  ensures it listens on all network interfaces.
# --server.headless=true    ensures it runs without a browser (container-friendly).
CMD ["streamlit", "run", "application.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
