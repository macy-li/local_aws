FROM lambci/lambda:build-python3.7
COPY pip.conf pip.conf
ENV PIP_CONFIG_FILE pip.conf
ENV REQPATH /root/requirements.txt
COPY ./requirements.txt /root/requirements.txt
RUN pip install -r ${REQPATH} --target=/opt/python/lib/python3.7/site-packages/
RUN cd /opt/python/lib/python3.7/site-packages/ && zip -r /root/lambda-layer.zip *
