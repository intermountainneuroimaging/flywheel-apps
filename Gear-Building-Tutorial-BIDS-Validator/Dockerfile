FROM bids/validator:v1.8.9

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
RUN adduser --disabled-password --gecos "Flywheel User" flywheel

USER flywheel

# Copy executable/manifest to Gear
COPY manifest.json ${FLYWHEEL}/manifest.json
COPY utils ${FLYWHEEL}/utils
COPY run.py ${FLYWHEEL}/run.py

# ENTRYPOINT ["python3 run.py"]