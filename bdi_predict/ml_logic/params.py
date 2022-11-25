import os

BASE_PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOCAL_REGISTRY_PATH =  os.path.join(BASE_PROJECT_PATH, "training_outputs")


if __name__ == "__main__":
    print(BASE_PROJECT_PATH)
    