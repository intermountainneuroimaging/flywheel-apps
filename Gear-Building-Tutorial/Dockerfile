FROM conda/miniconda3:latest

# RUN apt-get update -qq \
#     && apt-get install -y -q --no-install-recommends \
#            apt-utils \
#            bzip2 \
#            ca-certificates \
#            curl \
#            locales \
#            unzip \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/* \

 
RUN conda update -n base -y -c defaults conda   \
    && conda install -y -c conda-forge pytest-shutil   \
    && conda install -y -c conda-forge glob2    

RUN pip install flywheel-sdk

## new code...
# easy_install -U setuptools
# pip install "flywheel-gear-toolkit[all]~=0.3.2"
  
ENV FLYWHEEL=/flywheel/v0

RUN mkdir -p ${FLYWHEEL} 

# Create Flywheel User
RUN adduser --disabled-password --gecos "Flywheel User" flywheel

# Copy executable/manifest to Gear
COPY manifest.json ${FLYWHEEL}/manifest.json
COPY utils ${FLYWHEEL}/utils
COPY run.py ${FLYWHEEL}/run.py

# ENTRYPOINT ["python3 run.py"]