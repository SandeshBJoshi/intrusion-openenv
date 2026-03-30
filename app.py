from fastapi import FastAPI
from pydantic import BaseModel
from env import IntrusionEnv
import random

app = FastAPI()

env = IntrusionEnv()

# store last action for grading
last_action = {"action": None}


# request model
class ActionRequest(BaseModel):
    action: str


@app.get("/")
def home():
    return {"message": "Intrusion Detection Environment is running"}


# ---------------- RESET ----------------
@app.get("/reset")
def reset(level: str = None):
    state = env.reset(level)
    last_action["action"] = None  # reset last action
    return {
        "observation": state
    }


# ---------------- STEP ----------------
@app.post("/step")
def step(request: ActionRequest):
    last_action["action"] = request.action  # store action

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


# ---------------- GRADER (DYNAMIC) ----------------
@app.get("/grader")
def grader():
    state = env.get_state()

    if not state:
        return {"error": "No active task"}

    if not last_action["action"]:
        return {"error": "No action taken yet"}

    correct = state["label"]
    action = last_action["action"]

    # dynamic scoring logic
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
            "correct": info["correct_label"]
        })

    return {
        "baseline_results": results
    }