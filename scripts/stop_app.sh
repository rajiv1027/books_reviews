#!/bin/bash

# Check if the file exists and remove it
if [ -f /home/ubuntu/jktech/.dockerignore ]; then
    rm /home/ubuntu/jktech/.dockerignore
fi

# Add additional stop logic if needed
echo "Stopping application..."