#!/usr/bin/env bash
sudo pkill -9 python
cd frontend
nohup python backend/main.py &>2 &
yarn start
