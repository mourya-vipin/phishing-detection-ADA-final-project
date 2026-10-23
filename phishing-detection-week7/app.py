import streamlit as st
import pandas as pd
import joblib
from lime.lime_text import LimeTextExplainer
import streamlit.components.v1 as components

# load saved models
@st.cache_resource
def load_models():
    model = joblib.load('baseline_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    return model, vectorizer

model, vectorizer = load_models()
explainer = LimeTextExplainer(class_names=['Legitimate', 'Phishing'])

# prediction function for LIME
def predict_proba(texts):
    X_vec = vectorizer.transform(texts)
    return model.predict_proba(X_vec)

st.title("Phishing Detection & Explainability UI")
st.markdown("Paste an email below to see the classification and why it was flagged.")

email_input = st.text_area("Email Body:", height=200, placeholder="Paste email text here...")

if st.button("Analyze Email"):
    if email_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            # predict
            X_vec = vectorizer.transform([email_input])
            pred = model.predict(X_vec)[0]
            prob = model.predict_proba(X_vec)[0]

            # display result
            if pred == 1:
                st.error(f"ALARM: Phishing Detected! (Confidence: {prob[1]*100:.1f}%)")
            else:
                st.success(f"Safe: Legitimate Email. (Confidence: {prob[0]*100:.1f}%)")

            st.markdown("### LIME Explainability Analysis")
            st.markdown("*Highlighted words show what triggered the model's decision.*")

            # generate LIME explanation
            exp = explainer.explain_instance(email_input, predict_proba, num_features=10)

            # render LIME HTML in Streamlit
            html_content = exp.as_html()

            # force white background container for LIME so it ignores Streamlit's dark theme
            clean_css = """
            <style>
            .lime-wrapper {
                background-color: white !important;
                color: black !important;
                padding: 1rem;
                border-radius: 0.5rem;
            }
            /* Override Streamlit's iframe injection */
            body { background-color: white !important; }
            </style>
            <div class="lime-wrapper">
            """

            final_html = clean_css + html_content + "</div>"
            components.html(final_html, height=400, scrolling=True)
