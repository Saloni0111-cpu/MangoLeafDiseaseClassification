import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import plotly.graph_objects as go
import base64
# -----------------------------
# Load the trained model
# -----------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("mango_leaf_disease_model.h5")
    return model

model = load_model()

# -----------------------------
# Class labels
# -----------------------------
class_labels = {
    0: "Anthracnose",
    1: "Bacterial Canker",
    2: "Die Back",
    3: "Healthy",
    4: "Powdery Mildew",
    5: "Sooty Mould"
}

# -----------------------------
# Disease recommendations
# -----------------------------
disease_recommendations = {
    "Anthracnose": "Apply fungicides containing copper hydroxide or mancozeb. Prune affected areas and remove infected leaves and fruits.",
    "Bacterial Canker": "Prune affected areas using sterilized equipment. Apply copper-based fungicides. Avoid overhead irrigation.",
    "Die Back": "Prune affected areas. Ensure proper drainage and avoid over-watering. Apply fungicides if necessary.",
    "Healthy": "No action needed. Continue regular monitoring of the orchard.",
    "Powdery Mildew": "Apply fungicides containing sulfur or potassium bicarbonate. Prune affected areas and improve air circulation.",
    "Sooty Mould": "Remove and destroy affected leaves. Control the insect pests responsible for honeydew secretion."
}

# -----------------------------
# Preprocess & classify function
# -----------------------------
def classify_image(img):
    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array_exp = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array_exp)
    predicted_class_idx = np.argmax(predictions)
    predicted_class = class_labels.get(predicted_class_idx, "Unknown")
    return predicted_class, predictions[0]

# -----------------------------
# Streamlit App
# -----------------------------
def main():
    st.set_page_config(page_title="Mango Leaf Disease Classifier", layout="wide")


    #===========Background-----
    st.markdown(
"""
<style>
.video-background {
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -1;
    object-fit: cover;
    opacity: 0.5;  /* adjust transparency */
}
</style>

<video autoplay muted loop class="video-background">
    <source src="https://www.pexels.com/video/mangoes-on-a-tree-2239153/" type="video/mp4">
</video>
""",
unsafe_allow_html=True
)


    # -----------------------------
    # Smooth animated heading + subtitle
    # -----------------------------
    st.markdown(
    """
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 class="animated-heading">Mango Leaf Disease Classification</h1>
        <p class="animated-subtitle">Detect, Diagnose, and Protect Your Mango Orchard 🌿</p>
    </div>

    <style>
    .animated-heading {
        color: #10b981 !important;

        font-weight: bold;
        letter-spacing: 1px;
        font-size: 48px;
        opacity: 0;
        transform: scale(0.9);
        animation: headingFadeZoom 2s forwards;
    }

    .animated-subtitle {
        color: #d1fae5;
        font-style: italic;
        font-size: 20px;
        margin-top: 10px;
        opacity: 0;
        transform: translateY(10px);
        animation: subtitleFadeUp 2s forwards;
        animation-delay: 0.5s;
    }

    @keyframes headingFadeZoom {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }

    @keyframes subtitleFadeUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    # --- CSS for Buttons (green border, transparent bg, hover with black text) ---
    st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        flex-direction: column;  
        justify-content: center;
        align-items: center;
        gap: 12px;              
        margin-bottom: 20px;
        margin-top: 20px;
    }
    .button {
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 9px 12px;
      height: 40px;
      width: 180px;             
      border: 2px solid #10b981;  
      background: transparent;     
      border-radius: 20px;
      cursor: pointer;
      font-family: sans-serif;
      font-size: 16px;
      color: #10b981; 
      letter-spacing: 1px;
      text-align: center;
    }
    .button:hover {
      background: #10b981 !important; 
      border: 2px solid #10b981;
      color: black;  
    }
    .stButton {
        display: flex;
        justify-content: center;
    }
    .stButton>button {
      padding: 9px 12px;
      height: 40px;
      width: 180px;
      border: 2px solid #10b981;  
      background: transparent;     
      border-radius: 20px;
      cursor: pointer;
      font-family: sans-serif;
      font-size: 16px;
      color: #10b981; 
      letter-spacing: 1px;
    }
    .stButton>button:hover {
      background: #10b981 !important; 
      border: 2px solid #10b981;
      color: black;  
    }
    </style>
    """,
    unsafe_allow_html=True,
    )




    # --- Place the two buttons in one column (stacked) ---
    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    # Use session_state to remember chosen mode across reruns
    if "mode" not in st.session_state:
        st.session_state.mode = None

    upload_clicked = st.button("📂 Upload Image", key="upload_btn")
    camera_clicked = st.button("📷 Open Camera", key="camera_btn")

    if upload_clicked:
        st.session_state.mode = "upload"
    if camera_clicked:
        st.session_state.mode = "camera"

    st.markdown("</div>", unsafe_allow_html=True)

    # --- Show file uploader or camera input based on selected mode ---
    image = None
    if st.session_state.mode == "upload":
        st.markdown('<div style="width: 100px; margin: auto;">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose an image", type=["jpg","jpeg","png"], key="file_uploader")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)

    elif st.session_state.mode == "camera":
        st.markdown(
        """
        <div style="width:200px; height:70px; margin:auto; overflow:hidden;">
        <style>
        input[type='file'] {
            width: 200px !important;
            height: 500px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        camera_file = st.camera_input("Take a photo", key="camera_input")
        if camera_file is not None:
            image = Image.open(camera_file)

    # --- If image is available ---
    if image is not None:
        st.image(image, caption="Selected Leaf Image", width=400)
        with st.spinner("🔎 Analyzing the leaf..."):
            predicted_class, prediction_probabilities = classify_image(image)

        tab1, tab2, tab3 = st.tabs(["🔍 Prediction", "💡 Recommendations", "📊 Confidence Chart"])

        # Tab 1: Prediction
        with tab1:
            st.markdown(
                f'<div style="padding: 16px; border-radius: 11px; text-align: center; background: #1f2937; margin-bottom: 0.5rem; '
                f'border: 2.5px solid {"#10b981" if predicted_class=="Healthy" else "#f59e42"}; '
                f'color: {"#34d399" if predicted_class=="Healthy" else "#F59E42"}">'
                f'<h3>Prediction: {predicted_class}</h3>'
                f'<p style="font-size:18px;">Confidence: {np.max(prediction_probabilities)*100:.2f}%</p>'
                f'</div>',
                unsafe_allow_html=True,
            )

        # Tab 2: Recommendations
        with tab2:
            if predicted_class == "Healthy":
                st.success("✅ The leaf looks healthy. No treatment required.")
            else:
                st.markdown(
                    f'''
                    <div style="
                        padding: 16px; 
                        border-radius: 10px; 
                        background-color: #1f2937; 
                        border: 2px solid #f59e42; 
                        color: #f59e42; 
                        text-align: center;
                        font-size: 18px;
                        font-weight: bold;">
                        ⚠️ Detected: {predicted_class}
                    </div>
                    ''',
                    unsafe_allow_html=True,
                )
                st.subheader("Recommended Actions:")
                recommendations = [r.strip() for r in disease_recommendations[predicted_class].split(". ") if r.strip()]
                st.markdown(
                    "<ul style='padding-left: 18px; color:#f9fafb;'>" + "".join([f"<li>{rec}.</li>" for rec in recommendations]) + "</ul>",
                    unsafe_allow_html=True,
                )

        # Tab 3: Confidence Chart
        with tab3:
            class_names = [class_labels[i] for i in range(len(class_labels))]
            probabilities = prediction_probabilities[:len(class_labels)]
            fig = go.Figure(
                data=[
                    go.Bar(
                        x=class_names,
                        y=[float(f"{x:.4f}") * 100 for x in probabilities],
                        marker_color=['#10b981' if class_labels[i]==predicted_class else '#a7f3d0' for i in range(len(class_labels))],
                    )
                ]
            )
            fig.update_layout(
                title="Prediction Confidence per Class",
                xaxis_title="Disease Class",
                yaxis_title="Confidence (%)",
                plot_bgcolor="#1f2937",
                paper_bgcolor="#1f2937",
                font=dict(color="#f3faf7"),
                showlegend=False,
                height=400,
            )
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.markdown("<p style='text-align:center; color:#f9fafb;'>Please upload a mango leaf image or open the camera to get started.</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
