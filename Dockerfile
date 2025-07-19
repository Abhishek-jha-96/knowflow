FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG ENVIRONMENT

# Copy project code
COPY . /code/

# Set work directory
WORKDIR /code

# Install project dependencies
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -r ./requirements/${ENVIRONMENT}.txt

ENTRYPOINT ["sh", "server.sh"]
