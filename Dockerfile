FROM registry.cn-hangzhou.aliyuncs.com/sourcegarden/python:centos7-3.6

ADD . /var/www/codo-cron/

RUN pip3 install -r /var/www/codo-cron/requirements.txt

COPY docker/nginx_default.conf /etc/nginx/nginx.conf
COPY docker/nginx_ops.conf /etc/nginx/conf.d/codo-cron.conf
COPY docker/supervisor_ops.conf  /etc/supervisord.conf

EXPOSE 80
CMD ["/usr/bin/supervisord"]