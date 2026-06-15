import os
import subprocess
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")


def model_exists():
    return os.path.exists(MODEL_PATH)


def train_model():
    src_dir = os.path.join(BASE_DIR, "src")
    print(f"[{datetime.now()}] Training model...")
    subprocess.check_call([sys.executable, "train.py"], cwd=src_dir)
    print(f"[{datetime.now()}] Training finished.")


def run_app():
    print(f"[{datetime.now()}] Starting Flask app...")
    subprocess.check_call([sys.executable, "app.py"], cwd=BASE_DIR)


if __name__ == "__main__":
    if not model_exists():
        print("model.pkl not found, running training first.")
        train_model()
    else:
        print("model.pkl found, skipping training.")

    run_app()