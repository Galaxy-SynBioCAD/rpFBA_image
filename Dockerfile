FROM brsynth/rpbase

RUN pip install --no-cache-dir cobra
COPY rpTool.py /home/
COPY rpToolServe.py /home/
