# Author: Cuong Tran
#
# Build: docker build -t tranhuucuong91/app:0.1 .
# Run: docker run -d -p 8080:8080 --name app-run tranhuucuong91/app:0.1
#

FROM tranhuucuong91/java:oracle-java7
MAINTAINER Cuong Tran "tranhuucuong91@gmail.com"

# using apt-cacher-ng proxy for caching deb package
RUN echo 'Acquire::http::Proxy "http://172.17.0.1:3142/";' > /etc/apt/apt.conf.d/01proxy

ENV REFRESHED_AT 2015-10-22

RUN apt-get update -qq

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-jinja2

RUN mkdir /data/olbius-ofbiz

VOLUME /data/olbius-ofbiz
WORKDIR /data/olbius-ofbiz

COPY config /data/config

EXPOSE 8080 8443

# docker entrypoint
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["start-ofbiz"]

