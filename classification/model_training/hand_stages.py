import wandb
from ultralytics import YOLO

# === Step 1: Initialize Weights & Biases (W&B) ===
wandb.login(key="869e9dd4d25f2c41a3d15fd114688969331cfcbf")

# === Step 2: Load YOLO Model for Classification ===
model = YOLO("yolo11x-cls.pt")  # Ensure you have the classification model


# === Step 3: Train the Model and Log to W&B ===
# Train the model with recommended improvements
model.train(
    data="train_test_val",
    epochs=50,
    project="Kawasaki Diseases",
    name="Yolo v11-hand-stages-augmented",
    device="cuda",
    verbose=True
)

# === Step 4: Finish W&B Logging ===
wandb.finish()