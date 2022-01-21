################################################
#                This Dockerfil                #
################################################
FROM python:3.6

WORKDIR /projects
COPY ./ Marvel_KBQA/
WORKDIR /projects/Marvel_KBQA
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  py2neo
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  flask
RUN pip install pyltp-0.2.1-cp36-cp36m-win_amd64.whl
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  gunicorn==20.1.0
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  gevent


EXPOSE 5000

ENTRYPOINT [ "gunicorn", "-c", "gunicorn.conf.py", "run:app" ]