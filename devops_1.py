#!/usr/bin/python3
# Author: Marty Rath
# Description: Python 3 program to automate the process of creating, 
#              launching and monitoring public-facing web servers in the Amazon cloud.

from create_instance import create_instance
from create_bucket import create_bucket
from monitoring_commands import monitoring_commands
from cloud_watch import run_cloud_watch
import subprocess

# Creates bucket and returns bucket name
bucket_name = create_bucket()

# Ensure this is up-to-date
ami_id = 'ami-0f403e3180720dd7e'
# Creates instance, inputting name as parameter to display bucket image
instance = create_instance(ami_id, bucket_name)

# Runs monitoring script, saving to monitoring.txt and displaying results
subprocess.run(monitoring_commands(instance.public_ip_address), shell=True)

# Runs cloud watch monitoring
run_cloud_watch(instance)

