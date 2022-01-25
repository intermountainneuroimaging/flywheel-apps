FROM conda/miniconda3:latest

RUN conda update -n base -y -c defaults conda   \
    && conda install -y -c conda-forge pytest-shutil   \
    && conda install -y -c conda-forge glob2    

RUN pip install flywheel-sdk
  
ENV FLYWHEEL=/flywheel/v0

RUN mkdir -p ${FLYWHEEL} 

# Create Flywheel User
RUN adduser --disabled-password --gecos "Flywheel User" flywheel

# Copy executable/manifest to Gear
COPY manifest.json ${FLYWHEEL}/manifest.json
COPY utils ${FLYWHEEL}/utils
COPY run.py ${FLYWHEEL}/run.py

ENTRYPOINT ["python3 run.py"]
