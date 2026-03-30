import requests

BASE_URL = "https://sandeshbj-intrusion-openenv.hf.space"

def run():
    # reset environment
    r = requests.post(f"{BASE_URL}/reset")
    state = r.json()

    # take a random action
    action = {"action": "Normal"}
    r = requests.post(f"{BASE_URL}/step", json=action)
    result = r.json()

    # get grading
    r = requests.get(f"{BASE_URL}/grader")
    score = r.json()

    return {
        "state": state,
        "result": result,
        "score": score
    }


if __name__ == "__main__":
    print(run())