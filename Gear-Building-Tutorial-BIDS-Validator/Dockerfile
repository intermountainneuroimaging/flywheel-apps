FROM bids/validator:v1.8.9

RUN apk add --no-cache bash \
        python3 \
        py-pip

RUN pip install flywheel-sdk~=15.1.0 \
                flywheel-gear-toolkit~=0.1.3   \
                flywheel-bids~=0.9.1    \
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
