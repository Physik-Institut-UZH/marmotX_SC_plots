# Watchdog based on Monit package #
### Yanina 18.03.2021 ###
---

Monit handles the checking of a stalled process and the relaunching in case it crashes

You can add monit.conf to /etc/monit/monitrc the configuration file, it usually looks like:

    check process sync_files_from_marmotx.sh with matching sync_files_from*
        start = "/home/marmotxsc/marmotX_SC_plots/sync/sync_files_from_marmotx.sh start"
        set alert ybiondi@physik.uzh.ch

In case you want to use pid based instead of regex rule, you can use the script create_pid.sh, since not always a pid file is created for a process.

After configuring it, you can do

    monit reload

You can check the syntax of the configuration with

    monit -t

You can start running all monitored programs with

    monit start all

And you can check the status with

    monit status 
    
More details can be found at https://mmonit.com/monit/documentation/monit.html
