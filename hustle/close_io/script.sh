sort log.txt | grep '^/closeio.html' | grep -v '::1$' | grep -v '127.0.0.1$' | uniq -c | sort
