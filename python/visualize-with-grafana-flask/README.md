# References

1. <https://blog.jonathanmccall.com/2018/10/09/creating-a-grafana-datasource-using-flask-and-the-simplejson-plugin/>
2. <https://github.com/Jonnymcc/grafana-simplejson-datasource-example>

# Key Commands

1. Start data server `python3 index.py`
2. Run Grafana

```bash
docker stop  grafana; docker rm grafana;
docker run -d \
-p 3000:3000 \
--name=grafana \
-e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource" \
-e "GF_AUTH_ANONYMOUS_ENABLED=true" \
-e "GF_SECURITY_ADMIN_PASSWORD=admin" \
--add-host=host.docker.internal:host-gateway \
-v /Users/jah/dev/me/SANDBOX/python/visualize-with-grafana-flask/grafana/datasources:/etc/grafana/provisioning/datasources \
grafana/grafana
```
