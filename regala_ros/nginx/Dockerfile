FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN sudo apt-get install uwsgi
RUN sudo apt-get install usgi-plugin-python
RUN sudo apt-get install usgi-plugin-http
COPY nginx.conf /etc/nginx/conf.d/