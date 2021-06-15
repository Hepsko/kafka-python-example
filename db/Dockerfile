FROM mysql


WORKDIR /mysql
VOLUME /mysql

COPY database.sql /docker-entrypoint-initdb.d/
