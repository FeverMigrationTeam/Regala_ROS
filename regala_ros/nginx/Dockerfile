FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN apt-get install uwsgi
RUN apt-get install usgi-plugin-python
RUN apt-get install usgi-plugin-http
COPY nginx.conf /etc/nginx/conf.d/