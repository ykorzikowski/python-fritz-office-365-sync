FROM python:3.6-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN git clone https://github.com/ykorzikowski/fritzbox-smarthome.git
RUN cd fritzbox-smarthome && python3 setup.py sdist bdist_wheel

RUN pip install fritzbox-smarthome/dist/fritzhome-1.0.6.tar.gz
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-mradiator_fritz_o365_sync.runner" ]
