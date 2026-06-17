import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from train import main as train_main

if __name__ == "__main__":
    print("=== Student Performance Prediction ===")
    train_main()
    print("=== Done. Model saved to model.pkl ===")