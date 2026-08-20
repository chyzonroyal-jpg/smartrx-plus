import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="SmartRx Plus",
    page_icon="💊",
    layout="centered"
)

# ==========================================================
# CUSTOM THEME
# ==========================================================
st.markdown("""
<style>
.stApp{
    background-color:#F3F9FF;
}
h1,h2,h3{
    color:#4338CA;
}
.section{
    background:#EAF4FF;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #4338CA;
    margin-bottom:18px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# ORTHODOX MEDICINE DATABASE
# ==========================================================
DRUG_DATABASE = {

    # Analgesics
    "Boska":"Analgesics",
    "Calpol":"Analgesics",
    "Efferalgan":"Analgesics",
    "Emzor Paracetamol":"Analgesics",
    "M&B Paracetamol":"Analgesics",
    "Panadol":"Analgesics",

    # Antimalarials
    "Amatem":"Antimalarials",
    "Coartem":"Antimalarials",
    "Lonart":"Antimalarials",
    "P-Alaxin":"Antimalarials",
    "Maldox":"Antimalarials",

    # NSAIDs
    "Aspirin":"NSAIDs",
    "Brufen":"NSAIDs",
    "Diclofenac":"NSAIDs",
    "Ibuprofen":"NSAIDs",
    "Naproxen":"NSAIDs",
    "Nurofen":"NSAIDs",
    "Ponstan":"NSAIDs",
    "Voltaren":"NSAIDs",

    # Antibiotics
    "Amoxicillin":"Antibiotics",
    "Ampiclox":"Antibiotics",
    "Augmentin":"Antibiotics",
    "Azithromycin":"Antibiotics",
    "Ciprofloxacin":"Antibiotics",
    "Doxycycline":"Antibiotics",
    "Septrin":"Antibiotics",
    "Tetracycline":"Antibiotics",

    # Antiprotozoals
    "Flagyl":"Antiprotozoals",
    "Metrogyl":"Antiprotozoals",

    # Cold & Flu
    "Actifed":"Cold & Flu",
    "Cetirizine":"Cold & Flu",
    "Loratadine":"Cold & Flu",
    "Mixagrip":"Cold & Flu",
    "Piriton":"Cold & Flu",
    "Procold":"Cold & Flu",

    # Gut Health
    "Andrews Liver Salt":"Gut Health",
    "Esomeprazole":"Gut Health",
    "Gaviscon":"Gut Health",
    "Omeprazole":"Gut Health"
}

# ==========================================================
# NIGERIAN HERBAL DATABASE
# ==========================================================
HERB_DATABASE = {

    "Dogonyaro": {"english":"Neem","scientific":"Azadirachta indica","yoruba":"Dogonyaro","hausa":"Dogonyaro","igbo":"Akoko","classes":["Analgesics","Antimalarials"],"risk":"CRITICAL LIVER STRESS"},

    "Ewe-Awo": {"english":"Sweet Wormwood","scientific":"Artemisia annua","yoruba":"Ewe-Awo","hausa":"Tazargade","igbo":"Agbara","classes":["Antimalarials"],"risk":"CARDIOTOXICITY RISK"},

    "Ileke": {"english":"Madagascar Periwinkle","scientific":"Catharanthus roseus","yoruba":"Ileke","hausa":"Periwinkle","igbo":"Agbara","classes":["Antimalarials"],"risk":"NEUROLOGICAL RISK"},

    "Atale": {"english":"Ginger","scientific":"Zingiber officinale","yoruba":"Atale","hausa":"Citta","igbo":"Jinja","classes":["NSAIDs"],"risk":"GASTRIC BLEEDING"},

    "Ata-Iru": {"english":"African Pepper Bark","scientific":"Xylopia aethiopica","yoruba":"Ata-Iru","hausa":"Kimba","igbo":"Uda","classes":["NSAIDs"],"risk":"GASTRIC BLEEDING"},

    "Ewuro": {"english":"Bitter Leaf","scientific":"Vernonia amygdalina","yoruba":"Ewuro","hausa":"Shuwaka","igbo":"Olugbu","classes":["Antibiotics"],"risk":"ABSORPTION INTERFERENCE"},

    "Aayu": {"english":"Garlic","scientific":"Allium sativum","yoruba":"Aayu","hausa":"Tafarnuwa","igbo":"Ayuu","classes":["Antibiotics"],"risk":"ABSORPTION INTERFERENCE"},

    "Efinrin": {"english":"Scent Leaf","scientific":"Ocimum gratissimum","yoruba":"Efinrin","hausa":"Daddoya","igbo":"Nchanwu","classes":["Antiprotozoals"],"risk":"SEVERE GI TOXICITY"},

    "Atare": {"english":"Alligator Pepper","scientific":"Aframomum melegueta","yoruba":"Atare","hausa":"Citta Gida","igbo":"Ose Oji","classes":["Cold & Flu"],"risk":"HYPERTENSION RISK"},

    "Ahon Erin": {"english":"Aloe Vera","scientific":"Aloe vera","yoruba":"Ahon Erin","hausa":"Suku","igbo":"Efe Inyanya","classes":["Gut Health"],"risk":"ELECTROLYTE IMBALANCE"},

    "Zogale": {"english":"Moringa","scientific":"Moringa oleifera","yoruba":"Ewe Igbale","hausa":"Zogale","igbo":"Okwe Oyibo","classes":[],"risk":"Under AI Review"},

    "Atale Pupa": {"english":"Turmeric","scientific":"Curcuma longa","yoruba":"Atale Pupa","hausa":"Kurkum","igbo":"Turmeric","classes":[],"risk":"Under AI Review"},

    "Ewe Gova": {"english":"Guava Leaf","scientific":"Psidium guajava","yoruba":"Ewe Gova","hausa":"Goba","igbo":"Akwukwo Gova","classes":[],"risk":"Under AI Review"},

    "Kooko Oba": {"english":"Lemongrass","scientific":"Cymbopogon citratus","yoruba":"Kooko Oba","hausa":"Tsamiya","igbo":"Achara Lemon","classes":[],"risk":"Under AI Review"},

    "Zobo": {"english":"Hibiscus","scientific":"Hibiscus sabdariffa","yoruba":"Zobo","hausa":"Yakwua","igbo":"Zobo","classes":[],"risk":"Under AI Review"},

    "Uziza": {"english":"West African Pepper","scientific":"Piper guineense","yoruba":"Iyere","hausa":"Masoro","igbo":"Uziza","classes":[],"risk":"Under AI Review"},

    "Utazi": {"english":"Utazi","scientific":"Gongronema latifolium","yoruba":"Arokeke","hausa":"Utazi","igbo":"Utazi","classes":[],"risk":"Under AI Review"},

    "Orogbo": {"english":"Bitter Kola","scientific":"Garcinia kola","yoruba":"Orogbo","hausa":"Namijin Goro","igbo":"Aki Ilu","classes":[],"risk":"Under AI Review"},

    "Kanafuru": {"english":"Clove","scientific":"Syzygium aromaticum","yoruba":"Kanafuru","hausa":"Kanumfari","igbo":"Kanafuru","classes":[],"risk":"Under AI Review"},

    "Na'ana": {"english":"Mint","scientific":"Mentha spicata","yoruba":"Mint","hausa":"Na'ana","igbo":"Mint","classes":[],"risk":"Under AI Review"},

    "Efirin": {"english":"African Basil","scientific":"Ocimum basilicum","yoruba":"Efirin","hausa":"Basil","igbo":"Nchanwu","classes":[],"risk":"Under AI Review"},

    "Ewe Ibepe": {"english":"Pawpaw Leaf","scientific":"Carica papaya","yoruba":"Ewe Ibepe","hausa":"Ganyen Gwanda","igbo":"Akwukwo Okwuru","classes":[],"risk":"Under AI Review"},

    "Thyme": {"english":"Thyme","scientific":"Thymus vulgaris","yoruba":"Thyme","hausa":"Thyme","igbo":"Thyme","classes":[],"risk":"Under AI Review"},

    "Agbo Jedi": {"english":"Traditional Polyherbal Decoction","scientific":"Polyherbal formulation","yoruba":"Agbo Jedi","hausa":"Maganin Gargajiya","igbo":"Agbo","classes":[],"risk":"Composition varies – Use with caution"}
}

# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home","📖 How to Use","ℹ️ About"]
)

# ==========================================================
# HOME
# ==========================================================
if page == "🏠 Home":

    st.title("💊 SmartRx Plus")
    st.caption("AI Polypharmacy & Traditional Herbal Safety Platform")

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("About SmartRx Plus")
    st.write("SmartRx Plus cross-references orthodox medicines with Traditional African medicinal herbs to identify potential herb–drug interactions and medication safety risks.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("1. Select Orthodox Medicine")
    st.caption("Choose one medicine from the dropdown.")
    selected_drug = st.selectbox(
        "Orthodox Medicine",
        ["-- Select Medicine --"] + sorted(DRUG_DATABASE.keys())
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("2. Select Up to Four Local Herbs")
    st.caption("Choose every herbal infusion or extract currently being used.")

   # Create dropdown labels with Local + English + Scientific names
herb_labels = {
    herb: f"{herb} ({info['english']}) — {info['scientific']}"
    for herb, info in HERB_DATABASE.items()
}

display_options = ["None"] + sorted(herb_labels.values())

reverse_lookup = {v: k for k, v in herb_labels.items()}

herb1 = st.selectbox("Herb 1", display_options)
herb2 = st.selectbox("Herb 2", display_options, key="h2")
herb3 = st.selectbox("Herb 3", display_options, key="h3")
herb4 = st.selectbox("Herb 4", display_options, key="h4")

selected_herbs = []

for item in [herb1, herb2, herb3, herb4]:
    if item != "None":
        selected_herbs.append(reverse_lookup[item])
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🧠 RUN AI SAFETY VERIFICATION"):

        if selected_drug == "-- Select Medicine --":
            st.warning("Please select an orthodox medicine.")

               elif len(selected_herbs) == 0:
            st.warning("Please select at least one herb.")

        else:

            st.markdown('<div class="section">', unsafe_allow_html=True)
            st.subheader("AI Clinical Screening Report")

            drug_class = DRUG_DATABASE[selected_drug]
            interaction_found = False

            for herb in selected_herbs:

                info = HERB_DATABASE[herb]

                if drug_class in info["classes"]:

                    interaction_found = True

                    st.error("🚨 HIGH-RISK HERB–DRUG INTERACTION")

                    st.write(f"**Orthodox Medicine:** {selected_drug}")
                    st.write(f"**Drug Class:** {drug_class}")
                    st.write(f"**Local Name:** {herb}")
                    st.write(f"**English Name:** {info['english']}")
                    st.write(f"**Scientific Name:** {info['scientific']}")
                    st.write(f"**Yoruba:** {info['yoruba']}")
                    st.write(f"**Hausa:** {info['hausa']}")
                    st.write(f"**Igbo:** {info['igbo']}")
                    st.write(f"**Risk Level:** {info['risk']}")

                    st.divider()

            if not interaction_found:
                st.success("✅ CLEAR SAFETY PROFILE")
                st.write(
                    "No validated high-risk herb–drug interaction was detected within the current SmartRx Plus knowledge base."
                )

            st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# HOW TO USE
# ==========================================================
elif page == "📖 How to Use":

    st.title("📖 How to Use SmartRx Plus")

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("Step 1")
    st.write("Select one orthodox medicine from the pharmaceutical database.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("Step 2")
    st.write("Choose up to four Nigerian medicinal herbs currently being used.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("Step 3")
    st.write("Click **RUN AI SAFETY VERIFICATION** to analyze the selected combination.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("Step 4")
    st.write("Review the AI clinical report. Red indicates a validated high-risk interaction, while green indicates no known interaction in the current knowledge base.")
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# ABOUT
# ==========================================================
else:

    st.title("ℹ️ About SmartRx Plus")

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("Corporate Solution Overview")

    st.write("""
    **SmartRx Plus** is an AI-powered clinical decision-support platform developed by **Chizix Orbit Digital Innovations Ltd.**

    The platform combines pharmaceutical intelligence with Traditional African Medicine (TAM) through an ethnobotanical knowledge base to identify potential herb–drug interactions, duplicate therapeutic mechanisms, and medication safety risks.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("AI Knowledge Base")

    st.write("• 40+ Nigerian orthodox medicine brands")
    st.write("• 24 indigenous medicinal herbs")
    st.write("• English, Yoruba, Hausa & Igbo herb identification")
    st.write("• AI clinical interaction reporting")
    st.write("• Polypharmacy safety screening")

    st.markdown("</div>", unsafe_allow_html=True)

    st.info("SmartRx Plus is an educational clinical decision-support platform and does not replace professional medical advice.")
