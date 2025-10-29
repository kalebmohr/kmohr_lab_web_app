# Author: Kaleb Mohr
# Date: 29 Oct 2025
# Purpose: This is a Dockerfile used to build a Docker image for our web application.

# Use the official Python image. FROM specifically tells us a needed dependency.
FROM python:3.11-slim-bookworm

# Documenting developer metadata. The LABEL command allows us to specify metadata inside of our Dockerfile.
LABEL maintainer="Kaleb Mohr"

# RUN command allows us to execute BASH commands inside of our Docker container.
# We are telling it to install flask for us.
RUN pip install flask

# WORKDIR command switches working directories inside the Docker container.
# Here, we are setting it to /src since that is where our app files are.
WORKDIR /src

# EXPOSE command informs the image and container of the ports that will be used.
# This does NOT publicly expose the ports. That has to be done separate.
EXPOSE 5000/tcp

# ENTRYPOINT is used for calling the software command (i.e. python).
# CMD is used to declare the actual command from that software command (i.e. run.py).
# Here, we're telling Docker to run python app.py.
ENTRYPOINT ["python"]
CMD ["app.py"] 
