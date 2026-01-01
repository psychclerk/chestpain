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
        },
        {
            "diagnosis": "Unstable Angina",
            "age": 60,
            "sex": "Male",
            "pain": "Central chest tightness on minimal exertion",
            "duration": "20 minutes",
            "associated": "Dyspnea, sweating",
            "risk_factors": ["Hypertension", "Dyslipidemia", "Smoking"],
            "vitals": "BP 130/80 mmHg, HR 96/min, SpO₂ 97%",
            "ecg": "ST depression in lateral leads",
            "troponin": "Normal",
            "management": "Antiplatelets, anticoagulation, early angiography"
        },
        {
            "diagnosis": "NSTEMI",
            "age": 55,
            "sex": "Female",
            "pain": "Retrosternal pressure radiating to left shoulder",
            "duration": "30 minutes",
            "associated": "Nausea, diaphoresis",
            "risk_factors": ["Diabetes", "Hypertension"],
            "vitals": "BP 140/90 mmHg, HR 100/min, SpO₂ 96%",
            "ecg": "ST depression and T wave inversion",
            "troponin": "Elevated",
            "management": "Dual antiplatelet therapy, anticoagulation, early PCI"
        },
        {
            "diagnosis": "Acute Pericarditis",
            "age": 28,
            "sex": "Male",
            "pain": "Sharp chest pain relieved by sitting forward",
            "duration": "Several hours",
            "associated": "Low-grade fever",
            "risk_factors": ["Recent viral illness"],
            "vitals": "BP 120/70 mmHg, HR 90/min, SpO₂ 99%",
            "ecg": "Diffuse ST elevation with PR depression",
            "troponin": "Normal or mildly elevated",
            "management": "NSAIDs, colchicine"
        },
        {
            "diagnosis": "Gastroesophageal Reflux Disease (GERD)",
            "age": 45,
            "sex": "Male",
            "pain": "Burning retrosternal pain after meals",
            "duration": "Intermittent",
            "associated": "Regurgitation, sour taste",
            "risk_factors": ["Obesity", "Alcohol use"],
            "vitals": "Normal",
            "ecg": "Normal",
            "troponin": "Normal",
            "management": "Proton pump inhibitors, lifestyle modification"
        },
        {
            "diagnosis": "Pneumothorax",
            "age": 23,
            "sex": "Male",
            "pain": "Sudden unilateral pleuritic chest pain",
            "duration": "Sudden onset",
            "associated": "Dyspnea",
            "risk_factors": ["Tall thin body habitus", "Smoking"],
            "vitals": "BP 110/70 mmHg, HR 105/min, SpO₂ 92%",
            "ecg": "Normal",
            "troponin": "Normal",
            "management": "Chest X-ray, needle decompression if unstable"
        },
        {
            "diagnosis": "Costochondritis",
            "age": 34,
            "sex": "Female",
            "pain": "Localized chest wall pain worsened by movement",
            "duration": "Several days",
            "associated": "Chest wall tenderness",
            "risk_factors": ["Recent physical strain"],
            "vitals": "Normal",
            "ecg": "Normal",
            "troponin": "Normal",
            "management": "NSAIDs, reassurance"
        },
        {
            "diagnosis": "Esophageal Rupture (Boerhaave Syndrome)",
            "age": 50,
            "sex": "Male",
            "pain": "Severe chest pain after forceful vomiting",
            "duration": "Sudden onset",
            "associated": "Subcutaneous emphysema",
            "risk_factors": ["Alcohol binge"],
            "vitals": "BP 90/60 mmHg, HR 120/min, SpO₂ 90%",
            "ecg": "Normal",
            "troponin": "Normal",
            "management": "Emergency surgical repair, broad-spectrum antibiotics"
        },
        {
            "diagnosis": "Hypertrophic Obstructive Cardiomyopathy",
            "age": 19,
            "sex": "Male",
            "pain": "Exertional chest pain",
            "duration": "Minutes",
            "associated": "Syncope",
            "risk_factors": ["Family history of sudden cardiac death"],
            "vitals": "BP 110/70 mmHg, HR 85/min, SpO₂ 98%",
            "ecg": "Left ventricular hypertrophy",
            "troponin": "Normal",
            "management": "Beta blockers, activity restriction"
        },
        {
            "diagnosis": "Tension Pneumothorax",
            "age": 35,
            "sex": "Male",
            "pain": "Severe unilateral chest pain",
            "duration": "Sudden onset",
            "associated": "Severe respiratory distress",
            "risk_factors": ["Trauma"],
            "vitals": "BP 80/50 mmHg, HR 130/min, SpO₂ 85%",
            "ecg": "Sinus tachycardia",
            "troponin": "Normal",
            "management": "Immediate needle decompression"
        },
        {
            "diagnosis": "Mitral Valve Prolapse",
            "age": 26,
            "sex": "Female",
            "pain": "Atypical chest pain",
            "duration": "Intermittent",
            "associated": "Palpitations, anxiety",
            "risk_factors": ["Connective tissue disorder"],
            "vitals": "Normal",
            "ecg": "Normal",
            "troponin": "Normal",
            "management": "Reassurance, beta blockers if symptomatic"
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
        "Non–ST Elevation Myocardial Infarction (NSTEMI)",
        "Unstable Angina",
        "Aortic Dissection",
        "Pulmonary Embolism",
        "Acute Pericarditis",
        "Tension Pneumothorax",
        "Spontaneous Pneumothorax",
        "Esophageal Rupture (Boerhaave Syndrome)",
        "Gastroesophageal Reflux Disease (GERD)",
        "Costochondritis",
        "Panic / Anxiety Attack"
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
