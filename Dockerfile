# 任意のイメージを取得
FROM python

RUN apt update && apt -y update
RUN apt install -y less

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN pip install obs-websocket-py python-dotenv

WORKDIR /opt/app

COPY app /opt/app

RUN chmod 755 /opt/app/start.sh

RUN python --version

CMD [ "/opt/app/start.sh" ]
