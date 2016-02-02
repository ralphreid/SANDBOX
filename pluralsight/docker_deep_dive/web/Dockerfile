#Simple webserver for learning
FROM ubuntu:15.04
RUN apt-get update && RUN apt-get install -y \
	apache2 \
	apache2-utils \
	vim \
	#Clean up apt cache to keep containers lean and mean
	&& apt-get clean \
	#Simple command to remove tmp files and etc
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
