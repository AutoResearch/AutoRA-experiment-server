#!/bin/bash
# Use this script to build the ui and launch the web experiment locally

cd experiment
npm run build
cd ..
cp -rf experiment/dist experiment-server
cd experiment-server
uvicorn webserver:app --host "0.0.0.0" --port 80 &
