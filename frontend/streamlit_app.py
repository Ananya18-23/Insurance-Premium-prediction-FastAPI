import streamlit as st
import requests

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🚗",
    layout="wide"
)

# ---------------- API URL ---------------- #

API_URL = "https://insurance-premium-api-kxta.onrender.com/predict"

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🚗 Insurance Premium Predictor")

st.sidebar.info("""
### Tech Stack

- FastAPI
- Machine Learning
- Streamlit
- Docker
- Render
""")

st.sidebar.success("Backend Status : Live ✅")

# ---------------- TITLE ---------------- #

st.title("🚗 Insurance Premium Category Predictor")

st.write(
    "Fill in the details below to predict your Insurance Premium Category using Machine Learning."
)

st.divider()

# ---------------- INPUT FORM ---------------- #

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=200.0,
        value=65.0
    )

    height = st.number_input(
        "Height (m)",
        min_value=0.5,
        max_value=2.5,
        value=1.70
    )

    income_lpa = st.number_input(
        "Annual Income (LPA)",
        min_value=0.1,
        value=8.0
    )

with col2:

    smoker = st.selectbox(
        "Smoker",
        [True, False]
    )

    city = st.text_input(
        "City",
        "Mumbai"
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job"
        ]
    )

st.divider()

# ---------------- BUTTON ---------------- #

if st.button("🚀 Predict Premium Category", use_container_width=True):

    payload = {

        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation

    }

    with st.spinner("Predicting... Please wait..."):

        try:

            response = requests.post(API_URL, json=payload, timeout=60)

            if response.status_code == 200:

                result = response.json()

                prediction = result.get(
                    "predicted_category",
                    "Unknown"
                )

                st.success("Prediction Completed Successfully ✅")

                st.metric(
                    label="Predicted Insurance Category",
                    value=prediction
                )

                st.balloons()

            else:

                st.error(f"API Error : {response.status_code}")

                try:
                    st.json(response.json())
                except:
                    st.write(response.text)

        except requests.exceptions.ConnectionError:

            st.error("Unable to connect to FastAPI server.")

        except requests.exceptions.Timeout:

            st.error("Request Timed Out.")

        except Exception as e:

            st.error(str(e))

st.divider()

st.markdown(
"""
### 👨‍💻 Developed By

**Ananya Ginnare**

B.Tech AIML Student

FastAPI • Machine Learning • Docker • Streamlit
"""
)