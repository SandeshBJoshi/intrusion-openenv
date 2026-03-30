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

# 🚀 Intrusion Detection OpenEnv

🔗 **Live API:** https://sandeshbj-intrusion-openenv.hf.space
📄 **Swagger Docs:** https://sandeshbj-intrusion-openenv.hf.space/docs

---

## 🧪 Quick Demo

1. Open Swagger Docs
2. Click `GET /reset`
3. Use `POST /step` with an action
4. Check results via `GET /grader`

---

## 📌 Overview

This project implements a real-world OpenEnv environment simulating a cybersecurity intrusion detection system. The environment allows AI agents to interact via standard APIs (`reset`, `step`, `state`) and perform threat classification tasks.

---

## ⚡ Features

* Real-world cybersecurity simulation
* 3 difficulty levels: Easy, Medium, Hard
* Dynamic reward system (0.0 – 1.0)
* Agent evaluation via grader
* Baseline agent included
* Fully Dockerized

---

## ⚙️ API Endpoints

### Core APIs

* `GET /reset` → Initialize environment
* `POST /step` → Perform action
* `GET /state` → Current state

### Additional APIs

* `GET /tasks` → Task definitions
* `GET /grader` → Evaluate agent
* `GET /baseline` → Run baseline agent

---

## 🎮 Action Space

Possible actions:

* Normal
* BruteForce
* DDoS
* PortScan
* DataExfiltration
* MultiAttack

---

## 🏆 Reward Function

* Correct classification → 1.0
* Partial match → 0.5
* Incorrect → 0.0

---

## 🛠️ Setup (Local Run)

```bash
docker build -t intrusion-env .
docker run -p 7860:7860 intrusion-env
```

---

## 🌐 Access API

* Local: http://localhost:7860/docs
* Live: https://sandeshbj-intrusion-openenv.hf.space/docs

---

## 💡 Use Case

This environment simulates a Security Operations Center (SOC) workflow where an agent analyzes network logs and classifies threats.

---

## 🚀 Future Improvements

* Integration with real datasets
* Multi-step attack simulation
* Reinforcement learning agents
