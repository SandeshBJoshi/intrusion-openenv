from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import Body
import random

# try importing env safely
try:
    from env import IntrusionEnv
    env = IntrusionEnv()
except Exception as e:
    print("ENV INIT ERROR:", e)
    env = None

app = FastAPI()

# store last action for grading
last_action = {"action": None}


# request model
class ActionRequest(BaseModel):
    action: str


@app.get("/")
def home():
    return {
        "message": "Intrusion Detection Environment is running",
        "docs": "/docs"
    }


# ---------------- RESET ----------------

@app.get("/reset")
@app.post("/reset")
def reset(level: Optional[str] = Body(default=None)):
    if env is None:
        return {"error": "Environment not initialized"}

    state = env.reset(level)
    last_action["action"] = None

    return {
        "observation": state
    }


# ---------------- STEP ----------------
@app.post("/step")
def step(request: ActionRequest):
    if env is None:
        return {"error": "Environment not initialized"}

    last_action["action"] = request.action

    state, reward, done, info = env.step(request.action)

    return {
        "observation": state,
        "reward": reward,
        "done": done,
        "info": info
    }


# ---------------- STATE ----------------
@app.get("/state")
def get_state():
    if env is None:
        return {"error": "Environment not initialized"}

    return {
        "state": env.get_state()
    }


# ---------------- TASKS ----------------
@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {
                "level": "easy",
                "description": "Detect simple attack patterns",
                "actions": ["Normal", "BruteForce"]
            },
            {
                "level": "medium",
                "description": "Detect moderate attacks",
                "actions": ["DDoS", "PortScan", "BruteForce"]
            },
            {
                "level": "hard",
                "description": "Detect complex multi-stage attacks",
                "actions": ["DDoS", "DataExfiltration", "MultiAttack"]
            }
        ]
    }


# ---------------- GRADER ----------------
@app.get("/grader")
def grader():
    if env is None:
        return {"error": "Environment not initialized"}

    state = env.get_state()

    if not state:
        return {"error": "No active task"}

    if not last_action["action"]:
        return {"error": "No action taken yet"}

    correct = state.get("label", "")
    action = last_action["action"]

    # dynamic scoring
    if action == correct:
        score = 1.0
    elif action.lower() in correct.lower():
        score = 0.5
    else:
        score = 0.0

    return {
        "score": score,
        "your_action": action,
        "correct_answer": correct
    }


# ---------------- BASELINE AGENT ----------------
@app.get("/baseline")
def baseline():
    if env is None:
        return {"error": "Environment not initialized"}

    results = []

    for level in ["easy", "medium", "hard"]:
        state = env.reset(level)

        possible_actions = [
            "Normal", "BruteForce", "DDoS",
            "PortScan", "DataExfiltration", "MultiAttack"
        ]

        action = random.choice(possible_actions)

        _, reward, _, info = env.step(action)

        results.append({
            "level": level,
            "chosen_action": action,
            "reward": reward,
            "correct": info.get("correct_label", "Unknown")
        })

    return {
        "baseline_results": results
    }