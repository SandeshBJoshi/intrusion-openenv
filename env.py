import json
import random

class IntrusionEnv:
    def __init__(self):
        with open("data/logs.json", "r") as f:
            self.data = json.load(f)
        
        self.current_index = 0
        self.current_state = None

    def reset(self, level=None):
        # filter by difficulty if given
        if level:
            filtered = [d for d in self.data if d["level"] == level]
        else:
            filtered = self.data
        
        self.current_state = random.choice(filtered)
        return self.current_state

    def step(self, action):
        correct_label = self.current_state["label"]

        # reward logic
        if action == correct_label:
            reward = 1.0
        elif action.lower() in correct_label.lower():
            reward = 0.5
        else:
            reward = 0.0

        done = True  # one-step task

        return self.current_state, reward, done, {
            "correct_label": correct_label
        }

    def get_state(self):
        return self.current_state