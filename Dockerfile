FROM python:3.6-alpine

LABEL Author="Christa <christa0584@gmail.com>"
# Set your admin account here

ENV LDFLAGS=-L/usr/lib/x86_64-linux-gnu/
ENV SECRET_KEY=SECRET_KEYS USERNAME=postgres PASSWORD=postgres
ENV SUPUSER=admin EMAIL="admin@admin.com" SUPPASSWD=admin

RUN echo "http://mirrors.aliyun.com/alpine/v3.9/main/" > /etc/apk/repositories && \
    echo "http://mirrors.aliyun.com/alpine/v3.9/community/" >> /etc/apk/repositories && \
    \
    apk add --no-cache --virtual   make  vim postgresql-dev  musl-dev && \
    apk add --no-cache postgresql-libs gcc  && \
    apk add --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
    
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh

ARG PIP_MIRROR="https://pypi.tuna.tsinghua.edu.cn/simple"
COPY ./requirements.txt /requirements.txt

RUN set -ex \
    && pip install -i $PIP_MIRROR -r /requirements.txt

COPY . /usr/src/c1blog
RUN chmod +x /usr/src/c1blog/run.sh && \
    chmod +x /usr/local/bin/wait-for-it.sh && \
    chmod 755 /usr/src/c1blog

WORKDIR /usr/src/c1blog

EXPOSE 80
CMD ["sh", "run.sh"]

