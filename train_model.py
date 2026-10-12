"""Train and validate the synthetic adaptive difficulty model.

Run: python train_model.py
No patient data is used. Replace the synthetic generator only after clinical
and privacy approvals for any real-world deployment.
"""
from models.difficulty import train_model


if __name__ == "__main__":
    metrics = train_model()
    print(f"Validation accuracy: {metrics['validation_accuracy']:.1%}")
