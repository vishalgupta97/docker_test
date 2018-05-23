FROM ubuntu:16.04

COPY ./a.out a.out

ENTRYPOINT ./a.out

# docker build -t restart_test .
# docker run -d --restart=on_failure:5 --name restart_test restart_test
# docker logs restart_test