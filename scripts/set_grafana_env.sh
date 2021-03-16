#!/bin/sh
GF_CONFIG_PART=`cat ./configs/grafana.ini`
GF_CONFIG=`echo "$GF_CONFIG_PART"; echo "user = '$GF_EMAIL_USER'"; echo "password = '$GF_EMAIL_PASSWORD'"`
printf "$GF_CONFIG" | docker secret create gf_email_config.ini -
