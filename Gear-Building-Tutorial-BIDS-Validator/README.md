# Gear Building Tutorial (Part 2): BIDS Validator

In this gear, we will build on the basic flywheel gear building tutorial. In this tutorial we will learn to automatically call a subjects's input data using BIDS format, and will look at some additions required for singularity compatibility.

**Objectives:**
1. Use BIDS formatted subject level data for gear input
2. Run some computation / pipeline
3. Store results
4. Special case: Run on HPC

## Getting Started
We will start from the sucessful hello world gear. To do this, copy the project into a new directory and name it "Gear-Building-Tutorial-BIDS-Validator"

`cp -R Gear-Building-Tutorial/ Gear-Building-Tutorial-BIDS-Validator`

(TO DO)...Update the manifest file (flywheel gear name, docker image name, remove file input, remove file output)

## BIDS Data in Flywheel Gear
Using a bids dataset in the flywheel gear can be genereated directly from the flywheel SDK, and does not require naming each of your inputs in the manifest file. 

### Step 1.1: Add necessary packages to Dockerfile
(TO DO)... explaination of pip install flywheel gear toolkit

### Step 1.2. Add Api-Key as a required input in Manifest.json
(TO DO)... explaination of api-key requirement in manifest...link to flywheel documentation on the subject

### Step 1.3. Add Python Function Set (utils/BIDS)
(TO DO)... explanation of required python functions to identify group / project / subject / session ids for bids download function

### Step 1.4. Update run.py, Download BIDS within Container
(To DO)... add description and example code

All set! You now have a function that downloads your subject-level BIDS dataset into the flywheel container. This dataset can be used at the input to any number of BIDS compliant apps / pipelines. Lets test that this step worked correctly. We will add some checkpoints in our run.py script to confirm the BIDS dataset was downloaded in the location we expect, and with the correct naming convention.

## Running In Singularity 
The next objective we will tackle, is ensuring the gear is compatible with singularity. Here we need to make sure that the bids files (and outputs) are written into a directory with write permissions. 

### Step 2.1 Add Python Function Set (utils/BIDS)
(TO DO)... add description and example code

### Step 2.2. Point FLYWHEEL BASE to a temporary directory
(TO DO)... add description and example code

### Step 2.3. Update Dockerfile to run as non-root user
(TO DO)... add description and example code

Lets test it!! You need to run the flywheel gear on your high perforamce compute (using flywheel tag: `hpc`). 

## Adding Run Command
Now we have all the building blocks set, we will add the main computation for the pipeline. In this case we will run the BIDS Validator to check the bids dataset downloaded in the flywheel container can be used for any BIDS compatible pipeline.

### Step 3.1 Add Run Command
(TO DO)... add description and example code

### Step 3.2 Store Outputs
(TO DO)... add description and example code
