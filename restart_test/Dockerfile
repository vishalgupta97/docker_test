FROM gcc

COPY test.c /

RUN gcc test.c

ENTRYPOINT ./a.out

# docker build -t restart_test .
# docker run -d --restart=on_failure:5 --name restart_test restart_test
# docker logs restart_test