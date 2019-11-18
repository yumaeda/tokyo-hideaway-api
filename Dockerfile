FROM tiangolo/uwsgi-nginx:python3.7
LABEL maintainer="Yukitaka Maeda <yumaeda@gmail.com>"

# Install ansible.
RUN apt-get update
RUN apt-get -y install ansible

# Install modules.
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Set environment variables.
ENV STATIC_URL=/static
ENV STATIC_PATH=/app/static
ENV STATIC_INDEX=0
ENV PYTHONPATH=/app

# Make /app/* available to be imported by Python globally.
COPY ./app /app
WORKDIR /app

# Rename the base entrypoint to reuse it.
RUN mv /entrypoint.sh /uwsgi-nginx-entrypoint.sh

# Decrypt AWS config file.
RUN ansible-vault decrypt /app/.aws_config.json --vault-password-file /app/.vault_password

# Copy the entrypoint that will generate Nginx additional configs.
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Run the start script provided by the parent image tiangolo/uwsgi-nginx.
# It will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start nginx and uWSGI.
CMD ["/start.sh"]
