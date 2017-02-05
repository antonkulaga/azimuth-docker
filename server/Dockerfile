FROM compbioaging/azimuth:latest

LABEL maintainer "antonkulaga@gmail.com"

RUN pip install Flask

COPY src/server.py /opt/azimuth

ENV FLASK_APP=/opt/azimuth/server.py

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["/opt/azimuth/server.py"]
