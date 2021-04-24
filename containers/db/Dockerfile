FROM postgres:12

ENV POSTGRES_USER="postgres"
ENV POSTGRES_PASSWORD="postgres"
ENV POSTGRES_DB="postgres"

# put some utils and vim in the container
RUN apt-get update && apt-get install -y procps && apt install -y iputils-ping && apt-get install -y vim

