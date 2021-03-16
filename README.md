# marmotX_SC_plots

Runs grafana, alertmanager, prometheus and IOTpy in a docker compose.

# Install Docker compose

After installing docker do the following (instructions from [here](https://docs.docker.com/compose/install/))

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version
```

