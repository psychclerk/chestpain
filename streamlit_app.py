import streamlit as st
import random

# -------------------------------
# App Configuration
# -------------------------------
st.set_page_config(
    page_title="Chest Pain Case Simulator",
    layout="centered"
)

st.title("🫀 Chest Pain Case Simulator")
st.caption("Clinical reasoning simulator for MBBS graduates")

# -------------------------------
# Case Generator
# -------------------------------
def generate_case():
    cases = [
        {
            "diagnosis": "Acute Myocardial Infarction (STEMI)",
            "age": 58,
            "sex": "Male",
            "pain": "Central crushing chest pain radiating to left arm and jaw",
            "duration": "45 minutes",
            "associated": "Diaphoresis, nausea, shortness of breath",
            "risk_factors": ["Hypertension", "Diabetes", "Smoking"],
            "vitals": "BP 90/60 mmHg, HR 110/min, SpO₂ 94%",
            "ecg": "ST elevation in leads II, III, aVF",
            "troponin": "Markedly elevated",
            "management": "Immediate MONA, reperfusion therapy (Primary PCI)"
        },
        {
            "diagnosis": "Pulmonary Embolism",
            "age": 42,
            "sex": "Female",
            "pain": "Sharp pleuritic chest pain",
            "duration": "Sudden onset",
            "associated": "Dyspnea, hemoptysis",
            "risk_factors": ["Recent surgery", "Oral contraceptive use"],
            "vitals": "BP 110/70 mmHg, HR 120/min, SpO₂ 88%",
            "ecg": "Sinus tachycardia, S1Q3T3 pattern",
            "troponin": "Mildly elevated",
            "management": "CTPA, anticoagulation"
        },
        {
            "diagnosis": "Aortic Dissection",
            "age": 65,
            "sex": "Male",
            "pain": "Severe tearing chest pain radiating to back",
            "duration": "Sudden onset",
            "associated": "Syncope",
            "risk_factors": ["Hypertension"],
            "vitals": "BP difference between arms",
            "ecg": "Normal",
            "troponin": "Normal",
            "management": "CT aortogram, urgent surgical consult"
        }
    ]
    return random.choice(cases)

# -------------------------------
# Session State
# -------------------------------
if "case" not in st.session_state:
    st.session_state.case = generate_case()
    st.session_state.revealed = {
        "history": False,
        "exam": False,
        "investigations": False
    }

case = st.session_state.case

# -------------------------------
# History Section
# -------------------------------
st.header("📜 Patient History")

if st.button("Reveal History"):
    st.session_state.revealed["history"] = True

if st.session_state.revealed["history"]:
    st.write(f"**Age / Sex:** {case['age']} / {case['sex']}")
    st.write(f"**Chief Complaint:** {case['pain']}")
    st.write(f"**Duration:** {case['duration']}")
    st.write(f"**Associated Symptoms:** {case['associated']}")
    st.write(f"**Risk Factors:** {', '.join(case['risk_factors'])}")

# -------------------------------
# Examination Section
# -------------------------------
st.header("🩺 Physical Examination")

if st.button("Reveal Examination"):
    st.session_state.revealed["exam"] = True

if st.session_state.revealed["exam"]:
    st.write(f"**Vital Signs:** {case['vitals']}")

# -------------------------------
# Investigations Section
# -------------------------------
st.header("🧪 Investigations")

if st.button("Order Investigations"):
    st.session_state.revealed["investigations"] = True

if st.session_state.revealed["investigations"]:
    st.write(f"**ECG:** {case['ecg']}")
    st.write(f"**Troponin:** {case['troponin']}")

# -------------------------------
# Differential Diagnosis
# -------------------------------
st.header("🧠 Your Diagnosis")

user_dx = st.selectbox(
    "What is the most likely diagnosis?",
    [
        "Acute Myocardial Infarction (STEMI)",
        "Unstable Angina",
        "Pulmonary Embolism",
        "Aortic Dissection",
        "Pericarditis",
        "GERD"
    ]
)

if st.button("Submit Diagnosis"):
    if user_dx == case["diagnosis"]:
        st.success("✅ Correct diagnosis!")
    else:
        st.error(f"❌ Incorrect. Correct diagnosis: **{case['diagnosis']}**")

# -------------------------------
# Management
# -------------------------------
st.header("💊 Management")

if st.checkbox("Show Recommended Management"):
    st.info(case["management"])

# -------------------------------
# Reset Case
# -------------------------------
st.divider()
if st.button("🔄 Start New Case"):
    st.session_state.clear()
    st.rerun()

