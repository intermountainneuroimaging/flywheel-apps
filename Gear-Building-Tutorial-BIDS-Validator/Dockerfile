FROM bids/validator:v1.8.9

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

 
# RUN conda update -n base -y -c defaults conda   \
#    && conda install -y -c conda-forge pytest-shutil   \
#    && conda install -y -c conda-forge glob2    

# RUN rm -vfR /var/lib/apt/lists/* \
#     && apt-get update \
#     && apt-get install -y -q --no-install-recommends git \
#     && pip install bids    \

RUN apk add --no-cache bash \
        python3 \
        py-pip \
  && pip install flywheel-sdk \
                 flywheel-gear-toolkit    \
                 flywheel-bids    \
                 bids_validator   \
  && rm -rf /var/cache/apk/*

  
ENV FLYWHEEL=/flywheel/v0

RUN mkdir -p ${FLYWHEEL}   \
    && ln -s /usr/bin/python3 /usr/bin/python

# Create Flywheel User
# RUN groupadd -r flywheel -g 433 && \
#     useradd -u 431 -r -g flywheel -s /sbin/nologin -c "Docker image user" flywheel

#RUN adduser --disabled-password --gecos "Flywheel User" flywheel

USER flywheel

# Copy executable/manifest to Gear
COPY manifest.json ${FLYWHEEL}/manifest.json
COPY utils ${FLYWHEEL}/utils
COPY run.py ${FLYWHEEL}/run.py

# ENTRYPOINT ["python3 run.py"]