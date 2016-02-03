FROM ubuntu:15.04

RUN apt-get update && apt-get install -y iputils-ping apache2


# for example docker run hw2 Hellowwwww there! would pass
# arguments to the entry point so docker run hw2 Hellowwwww there!
# ENTRYPOINT ["echo"]

ENTRYPOINT ["apache2ctl"]

