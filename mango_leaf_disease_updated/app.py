import os
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model("mango_leaf_disease_model.h5")

# Define class labels
class_labels = {
    0: "Anthracnose",
    1: "Bacterial Canker",
    3: "Die Back",
    4: "Healthy",
    5: "Powdery Mildew",
    6: "Sooty Mould"
}

# Define recommendations
disease_recommendations = {
    "Anthracnose": "Apply fungicides containing copper hydroxide or mancozeb. Prune affected areas and remove infected leaves and fruits.",
    "Bacterial Canker": "Prune affected areas using sterilized equipment. Apply copper-based fungicides. Avoid overhead irrigation.",
    "Cutting Weevil": "Prune and remove infested twigs. Apply insecticides containing imidacloprid or thiamethoxam.",
    "Die Back": "Prune affected areas. Ensure proper drainage and avoid over-watering. Apply fungicides if necessary.",
    "Gall Midge": "Remove and destroy infested leaves and shoots. Apply neem oil or insecticidal soap. Avoid overhead irrigation.",
    "Healthy": "No action needed. Continue regular monitoring of the orchard.",
    "Powdery Mildew": "Apply fungicides containing sulfur or potassium bicarbonate. Prune affected areas and improve air circulation.",
    "Sooty Mould": "Remove and destroy affected leaves. Control the insect pests responsible for honeydew secretion."
}

# Function to preprocess and classify an image
def classify_image(img):
    try:
        img = img.resize((224, 224))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        predictions = model.predict(img)
        predicted_class_idx = np.argmax(predictions)
        predicted_class = class_labels[predicted_class_idx]

        return predicted_class, predictions[0]
    except Exception as e:
        return None, None

def main():
    st.title('🍃 Mango Leaf Disease Classifier')

    st.write("Upload an image OR use your camera:")

    # Upload file option
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # --- Camera Icon Button ---
    if "camera_on" not in st.session_state:
        st.session_state.camera_on = False

    if st.button("📷 Open Camera"):
        st.session_state.camera_on = True

    image = None

    # Show camera only when button is clicked
    if st.session_state.camera_on:
        camera_file = st.camera_input("Take a photo")
        if camera_file:
            image = Image.open(camera_file)

    elif uploaded_file is not None:
        image = Image.open(uploaded_file)

    # Process image if available
    if image:
        st.image(image, caption="Selected Image", use_column_width=True)
        predicted_class, prediction_probabilities = classify_image(image)

        if predicted_class is not None:
            st.success(f"Prediction: **{predicted_class}**")
            if predicted_class != "Healthy":
                st.subheader("Recommendations:")
                recommendations_list = disease_recommendations[predicted_class].split(". ")
                for i, recommendation in enumerate(recommendations_list):
                    if recommendation.strip():
                        st.write(f"{i+1}. {recommendation}")
        else:
            st.error("❌ Could not classify the image. Try again.")

if __name__ == "__main__":
    main()
