FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN apt-get update && apt-get upgrade -y

RUN python -m pip install --upgrade pip
RUN git clone https://github.com/mrdevil42023/Devil_X_Telegraph.git
RUN cd Devil_X_Telegraph
WORKDIR /Devil_X_Telegraph
RUN pip3 install -U -r requirements.txt
CMD python3 -m DevilxTelegraph
