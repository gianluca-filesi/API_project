#!/bin/bash
# Start Supervisor to manage both processes
pip install supervisor
supervisord -c supervisord.conf