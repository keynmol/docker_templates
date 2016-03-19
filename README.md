# Simple templating for Dockerfiles

Piss easy.

Check out Dockerfile in `sbt/` for example. 

Template parameters should be uppercase and can only include `A-Z_`. Whatever you specified in command line will be replaced in all files, not the other way around.

How to generate definitions:

```bash
python generate.py --base-folder sbt # where the template lives
                   --output-folder /tmp # where the folders will be created
                   --name keynmol/sbt # base docker name
                   --files sbt.sh # additional files to include
                   --label-template=SBT_VERSION-SCALA_VERSION # what label should look like
                   --SBT_VERSION 0.13.7 0.13.8 # specify values for your template variables
                   --SCALA_VERSION 2.11.7 2.11.8
``` 