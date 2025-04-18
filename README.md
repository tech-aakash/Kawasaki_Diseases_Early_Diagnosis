# Kawasaki Disease Early Screening Using Computer Vision

This project aims to develop a computer vision-based early screening tool for **Kawasaki Disease (KD)** using deep learning techniques. By analyzing visible symptoms like rash, red eyes, oral changes, and swollen extremities, the system predicts the likelihood of KD and helps guide further diagnostic decisions such as 2D echocardiography.

---

## 🩺 What is Kawasaki Disease?

Kawasaki Disease is a rare but serious illness that primarily affects children under the age of five. It causes inflammation in blood vessels and can lead to heart complications like coronary artery aneurysms if not treated early. Visible symptoms include:
- Polymorphous rash  
- Red eyes (conjunctival injection)  
- Cracked/red lips and strawberry tongue  
- Swollen hands and feet  
- Skin peeling  
- Cervical lymphadenopathy (swollen lymph nodes)

---

## 🎯 Objective

To build an AI-based system that:
- Detects visible KD symptoms from images.
- Screens for the likelihood of KD in early stages.
- Supports clinicians by recommending further diagnostic tests when needed.

---

## 📊 Dataset

- Images scraped from Google for symptoms such as:
  - Rash, red eyes, strawberry tongue, cracked lips, swollen extremities, etc.
- Working to acquire a research-grade dataset through collaboration with medical authors.
- Data is augmented and preprocessed (resizing, cropping, normalization) for better model performance.

---

## 🧠 Model

We use **YOLO v12** models:
- Variants: `yolov12-sim`, `yolov12-l`, and `yolov12-x`
- Object detection approach to localize and classify symptoms.
- Training/Validation/Test splits: `60-10-30`, `70-10-20`, and `80-10-10`.

---

## ⚙️ Training Details

- Data augmentation: Rotation, brightness adjustment, zoom, flipping.
- Hyperparameter tuning: Batch size, learning rate, number of epochs.
- Evaluation Metrics: Accuracy, Precision, Recall, F1-Score, AUC-ROC.

---

## ✅ Results

| Region        | Accuracy | Precision | Sensitivity | Specificity |
|---------------|----------|-----------|-------------|-------------|
| Body (Rash)   | 71%      | 68%       | 72%         | 73%         |
| Eye           | 80%      | 74%       | 84%         | 86%         |
| Hand          | 75%      | 73%       | 77%         | 78%         |
| Hand Stages   | 71%      | 76%       | 69%         | 66%         |
| Mouth         | 95%      | 88%       | 95%         | 95%         |
| Foot          | 80%      | 83%       | 78%         | 77%         |
| Foot Stages   | 74%      | 67%       | 78%         | 81%         |
| Avg (All)     | 78%      | 76%       | 79%         | 79%         |
| Combined (Eye, Hand, Mouth, Foot) | 83% | 79% | 83% | 84% |

---

## 📌 Conclusion

The model achieved an overall accuracy of **78%**, with the **mouth region performing best at 95%**. The combined accuracy of key body parts reached **83%**, showing strong potential for early KD detection. These results highlight the feasibility of using computer vision as a supportive tool in pediatric diagnosis workflows.
