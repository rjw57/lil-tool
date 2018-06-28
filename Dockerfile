FROM python:3.6-alpine
ADD . /usr/src/app
WORKDIR /usr/src/
RUN pip install ./app && rm -rf app/
ENTRYPOINT ["/usr/local/bin/lil"]
