# marmotX_SC_plots

Runs grafana, prometheus and IOTpy in a docker compose.

# Install Docker compose

After installing docker do the following (instructions from [here](https://docs.docker.com/compose/install/))

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version
```

# Configuring
You need to do this only the first time.

### Init Swarm
First you need to have your system run as docker "swarm".
```bash
sudo docker swarm init
```
### Create Grafana persisten volume
```bash
sudo docker volume create grafana-storage
```

### Setup grafana Secrets
Grafana uses external email service to provide alarm notifications, the credential for this service are secret and must stay so.
The Demo-SC administrator knows those credentials. **YOU MUST NOT ADD THEM TO THIS GIT REPOSITORY**.

```bash
git clone git@github.com:Physik-Institut-UZH/marmotX_SC_plots.git
cd marmotX_SC_plots
export GF_EMAIL_USER="<user-name>"
export GF_EMAIL_PASSWORD="<password>"
sudo source scripts/set_grafana_env.sh
# delete history
history -c 
```

# Deploy

```bash
cd marmotX_SC_plots
sudo docker stack deploy -c docker-compose.yml marmot

# check the services are running
sudo docker stack services marmot

# Stop it
sudo docker stack rm marmot
```

# Setup Grafana

### Setup prometheus data source

You need to setup Grafana with prometheus data source as described [here](https://grafana.com/docs/grafana/latest/datasources/prometheus/).
The only thing you need to modify is **URL** set it to **http://prometheus:9090**.

### Setup Alarms via Email

![alt text](https://raw.githubusercontent.com/Physik-Institut-UZH/marmotX_SC_plots/main/images/grafana_alarms.png)

