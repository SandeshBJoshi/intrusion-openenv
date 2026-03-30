---
title: Intrusion OpenEnv
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
app_port: 7860
pinned: false
---

# Intrusion Detection OpenEnv

## Overview
This project implements a real-world OpenEnv environment simulating a cybersecurity intrusion detection system. The environment allows AI agents to interact via standard APIs (`reset`, `step`, `state`) and perform threat classification tasks.

## Features
- Real-world cybersecurity simulation
- 3 difficulty levels: Easy, Medium, Hard
- Dynamic reward system (0.0 – 1.0)
- Agent evaluation via grader
- Baseline agent included
- Fully Dockerized

## API Endpoints

### Core APIs
- `GET /reset` → Initialize environment
- `POST /step` → Perform action
- `GET /state` → Current state

### Additional APIs
- `GET /tasks` → Task definitions
- `GET /grader` → Evaluate agent
- `GET /baseline` → Run baseline agent

## Action Space
Possible actions:
- Normal
- BruteForce
- DDoS
- PortScan
- DataExfiltration
- MultiAttack

## Reward Function
- Correct classification → 1.0
- Partial match → 0.5
- Incorrect → 0.0

## Setup

```bash
docker build -t intrusion-env .
docker run -p 8000:8000 intrusion-env