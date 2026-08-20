import streamlit as st

# 1. DATABASE COMPONENT SETS
DRUG_DATABASE = {
    "Emzor Paracetamol": "Analgesics",
    "Panadol": "Analgesics",
    "Boska": "Analgesics",
    "Calpol": "Analgesics",
    "Efferalgan": "Analgesics",
    "M&B Paracetamol": "Analgesics",
    "Amatem": "Antimalarials",
    "Coartem": "Antimalarials",
    "Lonart": "Antimalarials",
    "P-Alaxin": "Antimalarials",
    "Maldox": "Antimalarials",
    "Brufen (Ibuprofen)": "NSAIDs",
    "Nurofen": "NSAIDs",
    "Diclofenac": "NSAIDs",
    "Voltaren": "NSAIDs",
    "Aspirin": "NSAIDs",
    "Ampiclox": "Antibiotics",
    "Amoxicillin": "Antibiotics",
    "Augmentin": "Antibiotics",
    "Ciprofloxacin": "Antibiotics",
    "Doxycycline": "Antibiotics",
    "Tetracycline": "Antibiotics",
    "Septrin": "Antibiotics",
    "Flagyl": "Antiprotozoals",
    "Metrogyl": "Antiprotozoals",
    "Actifed": "Cold & Antihistamines",
    "Mixagrip": "Cold & Antihistamines",
    "Procold": "Cold & Antihistamines",
    "Piriton": "Cold & Antihistamines"
}

HERB_DATABASE = {
    "Dogonyaro (Neem Tree)": {
        "scientific": "Azadirachta indica",
        "conflicting_classes": ["Analgesics", "Antimalarials"],
        "risk": "🚨 CRITICAL LIVER STRESS: Dogonyaro crude properties drastically multiply organ processing workloads when combined with Paracetamol or Antimalarials. Risk of acute hepatotoxicity."
    },
    "Ewuro (Bitter Leaf)": {
        "scientific": "Vernonia amygdalina",
        "conflicting_classes": ["Antibiotics"],
        "risk": "⚠️ ABSORPTION INTERFERENCE: Bitter Leaf properties alter stomach acidity parameters, dropping blood assimilation rates and blocking the effectiveness of synthetic antibiotics."
    },
    "Efinrin (Scent Leaf)": {
        "scientific": "Ocimum gratissimum",
        "conflicting_classes": ["Antiprotozoals"],
        "risk": "CRITICAL TOXICITY: Mixing concentrated Scent Leaf infusions with Metronidazole (Flagyl) triggers extreme gastrointestinal contractions and acute vomiting."
    }
}

# 2. DESIGN & INTERFACE WRAPPERS
st.set_page_config(page_title="SmartRx Plus Engine", page_icon="🇳🇬", layout="centered")

# Reusable Function to render boxes with indigo title text color and light blue background color
def render_styled_box(title, content):
    st.markdown(
        f"""
        <div style="background-color: #EBF3F9; padding: 18px; border-radius: 8px; margin-bottom: 20px; border-left: 5px solid #4B0082;">
            <h4 style="color: #4B0082; margin-top: 0px; font-weight: bold; font-family: sans-serif;">{title}</h4>
            <div style="color: #2F4F4F; font-family: sans-serif; font-size: 15px; line-height: 1.5;">{content}</div>
        </div>
        """, 
        unsafe_html=True
    )

st.title("SmartRx Plus — Polypharmacy & Herb Safety Engine 🇳🇬")
st.caption("Engineered by Chizix Orbit Digital Innovations LTD (CODIL)")
st.write("---")

# 3. INTERACTIVE LAYOUT STRATEGY (Sidebar Tabs)
menu_selection = st.sidebar.radio("Navigation Menu", ["Safety Screening Dashboard", "How to Use Guide", "About SmartRx Plus"])

# TAB PANEL 1: HOW TO USE GUIDE
if menu_selection == "How to Use Guide":
    guide_content = """
    Follow these straightforward steps to run a multi-layered medicine safety check:
    <br><br>
    <b>Step 1: Select Your Full Pill List</b><br>
    Click the selector field under the orthodox drugs section. Scroll or search to tap on your medications. You can select multiple separate brands at the same time to screen for active group duplication.
    <br><br>
    <b>Step 2: Choose Your Traditional Herbal Extracts</b><br>
    Click the dropdown panel under the traditional section. Select all local remedies or organic mixtures you are currently drinking or consuming alongside your pills.
    <br><br>
    <b>Step 3: Run Interactive Diagnostic Screening</b><br>
    Click the full-width screening control button at the base of the portal. The matrix will cross-check synthetic ingredient duplications and traditional bio-chemical contradictions instantly.
    """
    render_styled_box("Step-by-Step User Instructions", guide_content)

# TAB PANEL 2: ABOUT THE SOLUTION
elif menu_selection == "About SmartRx Plus":
    about_content = """
    <b>SmartRx Plus</b> is an AI-powered medication safety middleware engine developed directly by <b>Chizix Orbit Digital Innovations LTD (CODIL)</b>. 
    <br><br>
    In developing markets like Nigeria, a massive public health blindspot exists due to concurrent dual-medication—where citizens mix modern synthetic prescriptions with traditional African medicinal herbs without standard dosage calculations or compound labeling. 
    <br><br>
    Our platform acts as a digital companion that standardizes colloquial dialect variants into universal chemical identifiers. By leveraging advanced logical architectures and Meta's open-source artificial intelligence systems, we bridge traditional practices with clinical safety datasets to protect millions of consumers from preventable organ toxicities.
    """
    render_styled_box("Corporate Solution Overview", about_content)

# TAB PANEL 3: THE MAIN SCREENING WORKSPACE
else:
    # Segment 1 UI Container
    drugs_instruction = "💡 <b>Pro Tip:</b> Click this selector multiple times to select every separate brand pill you are scheduled to take concurrently."
    render_styled_box("1. Select All Current Orthodox Medications", drugs_instruction)
    selected_drugs = st.multiselect(
        "Choose synthetic prescriptions or over-the-counter brands:",
        options=sorted(list(DRUG_DATABASE.keys())),
        label_visibility="collapsed"
    )
    
    st.write("") # Layout spacer
    
    # Segment 2 UI Container
    herbs_instruction = "🌿 <b>Dropdown Unlocked:</b> You can now choose multiple traditional local herb infusions from this menu to run comparative cross-domain analysis."
    render_styled_box("2. Select All Current Indigenous Herb Infusions", herbs_instruction)
    selected_herbs = st.multiselect(
        "Choose traditional local remedies or native extracts:",
        options=sorted(list(HERB_DATABASE.keys())),
        label_visibility="collapsed"
    )

    st.write("---")

    # 4. DATA LOGIC PROCESSOR
    if st.button("RUN ADVANCED CROSS-DOMAIN SAFETY SCREENING", use_container_width=True):
        if not selected_drugs and not selected_herbs:
            st.info("Please fill out your medication panels above to execute the diagnostic screening check.")
        else:
            st.write("### 🔍 Advanced Screening Diagnostics")
            conflicts_found = False
            
            # CHECK LEVEL 1: Synthetic Overdoses (Multi-Drug Duplication)
            if selected_drugs:
                selected_classes = [DRUG_DATABASE[drug] for drug in selected_drugs]
                duplicate_classes = set([cls for cls in selected_classes if selected_classes.count(cls) > 1])
                
                if duplicate_classes:
                    conflicts_found = True
                    for cls in duplicate_classes:
                        st.error(f"❌ **Orthodox Duplication Detected**: You have chosen multiple brands belonging to the **{cls}** class simultaneously. This introduces an accidental synthetic drug overdose risk.")

            # CHECK LEVEL 2: Multi-Herb to Multi-Drug Interactions
            if selected_herbs and selected_drugs:
                for herb_name in selected_herbs:
                    herb_info = HERB_DATABASE[herb_name]
                    
                    for drug_name in selected_drugs:
                        drug_class = DRUG_DATABASE[drug_name]
                        
                        if drug_class in herb_info["conflicting_classes"]:
                            conflicts_found = True
                            st.error(f"❌ **Cross-Domain Interaction Warning**: The extract **{herb_name}** conflicts directly with your medication: **{drug_name}** ({drug_class}).")
                            st.warning(herb_info["risk"])
            
            # CLEAN VERDICT PASS
            if not conflicts_found:
                st.success("✅ **Clear Safety Profile**: No active ingredient duplications or direct drug-herb class contradictions flagged for this intake profile.")
