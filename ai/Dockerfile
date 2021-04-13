FROM tensorflow/tensorflow

WORKDIR /server
ADD requirements.txt /server/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /server/
