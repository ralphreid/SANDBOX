# References

1. <https://grafana.com/docs/grafana/latest/installation/docker/>
2. <http://oz123.github.io/writings/2019-06-16-Visualize-almost-anything-with-Grafana-and-Python/index.html>
3. <https://bottlepy.org/docs/dev/>


# Key Commands

1. Run Grafana

```bash
docker run -d \
-p 3000:3000 \
--name=grafana \
-e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource" \
-e "GF_AUTH_ANONYMOUS_ENABLED=true" \
grafana/grafana
```

2. Grafana credentials are `admin` and `admin`

3. adf
