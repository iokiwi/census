FROM python:alpine

COPY scripts/entrypoint.sh /opt/
COPY census  /opt/census
COPY etc/conf.py /etc/census/

WORKDIR /opt/
RUN apk add --no-cache \
      bash \
      git \
      gcc \
      curl \
      g++ \
      sqlite \
      sqlite-dev \
      libstdc++ \
      openssl-dev \
      linux-headers \
      libffi-dev \
      musl-dev \
      libmagic && \
    pip install --upgrade pip && \
    pip install -r /opt/census/requirements.txt && \
    pip install gunicorn && \
    apk del \ 
          git;

HEALTHCHECK --interval=2s --timeout=5s --retries=5 \
   CMD curl -f http://localhost:8000/ || exit 1

EXPOSE 8000

WORKDIR /opt

ENTRYPOINT ["/opt/entrypoint.sh"]

CMD ["--start-service"]
