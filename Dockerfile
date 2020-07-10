FROM brsynth/rpcache

RUN pip install --no-cache-dir cobra

RUN git clone https://github.com/Galaxy-SynBioCAD/inchikeyMIRIAM.git -b master
RUN mv inchikeyMIRIAM/inchikeyMIRIAM.py /home/
RUN rm -r inchikeyMIRIAM

COPY rpTool.py /home/
COPY rpToolServe.py /home/
COPY galaxy/code/tool_rpFBA.py /home/
