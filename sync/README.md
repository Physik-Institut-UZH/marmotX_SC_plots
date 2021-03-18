# Watchdog based on Monit package #
# Yanina 18.03.2021 #
Monit handles the checking of a stalled process and the relaunching in case it crashes

You can add to /etc/monit/monitrc the configuration file 

In case you want to use pid based instead of regex rule, you can use the script create_pid.sh, since not always a pid file is created for a process.

after configuring it, you can do

monit reaload

You can check the syntax of the configuration with

monit -t

You can start running all monitores programs with

monit start all

And you can check the status with

monit status 
