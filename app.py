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

.stApp {
    background-color: #F3F9FF;
}

h1, h2, h3 {
    color: #4338CA;
}

.section {
    background-color: #EAF4FF;
    padding: 20px;
    border-radius: 14px;
    border-left: 6px solid #4338CA;
    margin-bottom: 20px;
}

.section-title {
    color: #4338CA;
    font-weight: 700;
    font-size: 1.15rem;
}

div.stButton > button {
    background-color: #4338CA;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 18px;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #3730A3;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# ORTHODOX MEDICINE DATABASE
# ==========================================================
DRUG_DATABASE = {

    # Analgesics
    "Boska": "Analgesics",
    "Calpol": "Analgesics",
    "Efferalgan": "Analgesics",
    "Emzor Paracetamol": "Analgesics",
    "M&B Paracetamol": "Analgesics",
    "Panadol": "Analgesics",

    # Antimalarials
    "Amatem": "Antimalarials",
    "Coartem": "Antimalarials",
    "Lonart": "Antimalarials",
    "P-Alaxin": "Antimalarials",
    "Maldox": "Antimalarials",

    # NSAIDs
    "Aspirin": "NSAIDs",
    "Brufen": "NSAIDs",
    "Diclofenac": "NSAIDs",
    "Ibuprofen": "NSAIDs",
    "Naproxen": "NSAIDs",
    "Nurofen": "NSAIDs",
    "Ponstan": "NSAIDs",
    "Voltaren": "NSAIDs",

    # Antibiotics
    "Amoxicillin": "Antibiotics",
    "Ampiclox": "Antibiotics",
    "Augmentin": "Antibiotics",
    "Azithromycin": "Antibiotics",
    "Ciprofloxacin": "Antibiotics",
    "Doxycycline": "Antibiotics",
    "Septrin": "Antibiotics",
    "Tetracycline": "Antibiotics",

    # Antiprotozoals
    "Flagyl": "Antiprotozoals",
    "Metrogyl": "Antiprotozoals",

    # Cold & Flu
    "Actifed": "Cold & Flu",
    "Cetirizine": "Cold & Flu",
    "Loratadine": "Cold & Flu",
    "Mixagrip": "Cold & Flu",
    "Piriton": "Cold & Flu",
    "Procold": "Cold & Flu",

    # Gut Health
    "Andrews Liver Salt": "Gut Health",
    "Esomeprazole": "Gut Health",
    "Gaviscon": "Gut Health",
    "Omeprazole": "Gut Health"
}

# ==========================================================
# NIGERIAN HERBAL DATABASE
# ==========================================================
HERB_DATABASE = {

    "Dogonyaro": {
        "english": "Neem",
        "scientific": "Azadirachta indica",
        "yoruba": "Dogonyaro",
        "hausa": "Dogonyaro",
        "igbo": "Akoko",
        "classes": ["Analgesics", "Antimalarials"],
        "risk": "High-priority screening flag: potential hepatic and pharmacological concerns require professional review."
    },

    "Ewe-Awo": {
        "english": "Sweet Wormwood",
        "scientific": "Artemisia annua",
        "yoruba": "Ewe-Awo",
        "hausa": "Tazargade",
        "igbo": "Agbara",
        "classes": ["Antimalarials"],
        "risk": "Screening flag: contains artemisinin-related compounds. Concurrent use with antimalarial medicines requires professional review."
    },

    "Ileke": {
        "english": "Madagascar Periwinkle",
        "scientific": "Catharanthus roseus",
        "yoruba": "Ileke",
        "hausa": "Periwinkle",
        "igbo": "Agbara",
        "classes": ["Antimalarials"],
        "risk": "Screening flag: medicinally active alkaloids are present. Unsupervised medicinal use may present safety concerns."
    },

    "Atale": {
        "english": "Ginger",
        "scientific": "Zingiber officinale",
        "yoruba": "Atale",
        "hausa": "Citta",
        "igbo": "Jinja",
        "classes": ["NSAIDs"],
        "risk": "Screening flag: concentrated ginger preparations may have effects relevant to bleeding risk and gastrointestinal safety."
    },

    "Ata-Iru": {
        "english": "African Pepper",
        "scientific": "Xylopia aethiopica",
        "yoruba": "Ata-Iru",
        "hausa": "Kimba",
        "igbo": "Uda",
        "classes": ["NSAIDs"],
        "risk": "Screening flag: concentrated preparations may have pharmacological effects requiring professional assessment."
    },

    "Ewuro": {
        "english": "Bitter Leaf",
        "scientific": "Vernonia amygdalina",
        "yoruba": "Ewuro",
        "hausa": "Shuwaka",
        "igbo": "Olugbu",
        "classes": ["Antibiotics"],
        "risk": "Screening flag: medicinal preparations may contain bioactive compounds that could affect medicine response."
    },

    "Aayu": {
        "english": "Garlic",
        "scientific": "Allium sativum",
        "yoruba": "Aayu",
        "hausa": "Tafarnuwa",
        "igbo": "Ayuu",
        "classes": ["Antibiotics"],
        "risk": "Screening flag: concentrated garlic preparations can have pharmacological effects and should be reviewed when medicines are involved."
    },

    "Efinrin": {
        "english": "Scent Leaf",
        "scientific": "Ocimum gratissimum",
        "yoruba": "Efinrin",
        "hausa": "Daddoya",
        "igbo": "Nchanwu",
        "classes": ["Antiprotozoals"],
        "risk": "Screening flag: concentrated preparations contain bioactive compounds that may require interaction assessment."
    },

    "Atare": {
        "english": "Alligator Pepper",
        "scientific": "Aframomum melegueta",
        "yoruba": "Atare",
        "hausa": "Citta Gida",
        "igbo": "Ose Oji",
        "classes": ["Cold & Flu"],
        "risk": "Screening flag: stimulant and cardiovascular effects should be considered when combined with medicines."
    },

    "Ahon Erin": {
        "english": "Aloe Vera",
        "scientific": "Aloe vera",
        "yoruba": "Ahon Erin",
        "hausa": "Suku",
        "igbo": "Efe Inyanya",
        "classes": ["Gut Health"],
        "risk": "Screening flag: oral aloe preparations may affect gastrointestinal function and electrolyte balance."
    },

    "Zogale": {
        "english": "Moringa",
        "scientific": "Moringa oleifera",
        "yoruba": "Ewe Igbale",
        "hausa": "Zogale",
        "igbo": "Okwe Oyibo",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database. Professional review is recommended."
    },

    "Atale Pupa": {
        "english": "Turmeric",
        "scientific": "Curcuma longa",
        "yoruba": "Atale Pupa",
        "hausa": "Kurkum",
        "igbo": "Turmeric",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database. Concentrated supplements should still be reviewed."
    },

    "Ewe Gova": {
        "english": "Guava Leaf",
        "scientific": "Psidium guajava",
        "yoruba": "Ewe Gova",
        "hausa": "Goba",
        "igbo": "Akwukwo Gova",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database. Professional review is recommended."
    },

    "Kooko Oba": {
        "english": "Lemongrass",
        "scientific": "Cymbopogon citratus",
        "yoruba": "Kooko Oba",
        "hausa": "Tsamiya",
        "igbo": "Achara Lemon",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Zobo": {
        "english": "Hibiscus",
        "scientific": "Hibiscus sabdariffa",
        "yoruba": "Zobo",
        "hausa": "Yakwua",
        "igbo": "Zobo",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database. Effects on blood pressure and medicines may warrant professional review."
    },

    "Uziza": {
        "english": "West African Pepper",
        "scientific": "Piper guineense",
        "yoruba": "Iyere",
        "hausa": "Masoro",
        "igbo": "Uziza",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Utazi": {
        "english": "Utazi",
        "scientific": "Gongronema latifolium",
        "yoruba": "Arokeke",
        "hausa": "Utazi",
        "igbo": "Utazi",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Orogbo": {
        "english": "Bitter Kola",
        "scientific": "Garcinia kola",
        "yoruba": "Orogbo",
        "hausa": "Namijin Goro",
        "igbo": "Aki Ilu",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Kanafuru": {
        "english": "Clove",
        "scientific": "Syzygium aromaticum",
        "yoruba": "Kanafuru",
        "hausa": "Kanumfari",
        "igbo": "Kanafuru",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Na'ana": {
        "english": "Mint",
        "scientific": "Mentha spicata",
        "yoruba": "Mint",
        "hausa": "Na'ana",
        "igbo": "Mint",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Efirin": {
        "english": "African Basil",
        "scientific": "Ocimum basilicum",
        "yoruba": "Efirin",
        "hausa": "Basil",
        "igbo": "Nchanwu",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Ewe Ibepe": {
        "english": "Pawpaw Leaf",
        "scientific": "Carica papaya",
        "yoruba": "Ewe Ibepe",
        "hausa": "Ganyen Gwanda",
        "igbo": "Akwukwo Okwuru",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Thyme": {
        "english": "Thyme",
        "scientific": "Thymus vulgaris",
        "yoruba": "Thyme",
        "hausa": "Thyme",
        "igbo": "Thyme",
        "classes": [],
        "risk": "No specific interaction is asserted by this screening database."
    },

    "Agbo Jedi": {
        "english": "Traditional Polyherbal Decoction",
        "scientific": "Polyherbal formulation",
        "yoruba": "Agbo Jedi",
        "hausa": "Maganin Gargajiya",
        "igbo": "Agbo",
        "classes": [],
        "risk": "Composition varies between preparations. Because the ingredients and concentrations may be unknown, professional review is recommended."
    }
}

# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📖 How to Use", "ℹ️ About"]
)

# ==========================================================
# HOME
# ==========================================================
if page == "🏠 Home":

    st.title("💊 SmartRx Plus")
    st.caption("AI Polypharmacy & Traditional Herbal Safety Platform")

    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.subheader("About SmartRx Plus")

    st.write(
        "SmartRx Plus cross-references selected orthodox medicines with "
        "Traditional African Medicine (TAM) entries in its knowledge base "
        "to screen for potential herb–drug safety concerns."
    )

    st.info(
        "This is a safety-screening and educational tool. It does not "
        "diagnose illness or replace a doctor or pharmacist."
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # ORTHODOX MEDICINE
    # ------------------------------------------------------
    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.subheader("1. Select Orthodox Medicine")

    st.caption(
        "Select one orthodox medicine. SmartRx Plus currently screens "
        "one selected medicine against up to four selected herbs."
    )

    selected_drug = st.selectbox(
        "Orthodox Medicine",
        ["-- Select Medicine --"] + sorted(DRUG_DATABASE.keys())
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # HERBS
    # ------------------------------------------------------
    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.subheader("2. Select Up to Four Local Herbs")

    st.caption(
        "Choose up to four herbs. Each option includes the Nigerian "
        "local name, English name and scientific botanical name."
    )

    herb_labels = {
        herb: (
            f"{herb} ({info['english']}) — "
            f"{info['scientific']}"
        )
        for herb, info in HERB_DATABASE.items()
    }

    display_options = ["None"] + sorted(herb_labels.values())

    reverse_lookup = {
        value: key
        for key, value in herb_labels.items()
    }

    herb1 = st.selectbox(
        "🌿 Herb 1",
        display_options,
        key="herb1"
    )

    herb2 = st.selectbox(
        "🌿 Herb 2",
        display_options,
        key="herb2"
    )

    herb3 = st.selectbox(
        "🌿 Herb 3",
        display_options,
        key="herb3"
    )

    herb4 = st.selectbox(
        "🌿 Herb 4",
        display_options,
        key="herb4"
    )

    selected_herbs = []

    for item in [herb1, herb2, herb3, herb4]:

        if item != "None":

            actual_herb = reverse_lookup[item]

            if actual_herb not in selected_herbs:
                selected_herbs.append(actual_herb)

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # VERIFICATION BUTTON
    # ------------------------------------------------------
    if st.button(
        "🧠 RUN AI SAFETY VERIFICATION",
        use_container_width=True
    ):

        if selected_drug == "-- Select Medicine --":

            st.warning(
                "Please select an orthodox medicine before running the screening."
            )

        elif len(selected_herbs) == 0:

            st.warning(
                "Please select at least one local herb before running the screening."
            )

        else:

            st.markdown(
                '<div class="section">',
                unsafe_allow_html=True
            )

            st.subheader("🔍 Safety Screening Report")

            drug_class = DRUG_DATABASE[selected_drug]

            interaction_found = False

            st.write(
                f"**Orthodox Medicine:** {selected_drug}"
            )

            st.write(
                f"**Medicine Category:** {drug_class}"
            )

            st.write(
                f"**Herbs Screened:** {len(selected_herbs)}"
            )

            st.divider()

            # --------------------------------------------------
            # CHECK EACH SELECTED HERB
            # --------------------------------------------------
            for herb in selected_herbs:

                info = HERB_DATABASE[herb]

                if drug_class in info["classes"]:

                    interaction_found = True

                    st.error(
                        "🚨 SCREENING FLAG — POTENTIAL HERB–DRUG CONCERN"
                    )

                    st.write(
                        f"**Local Nigerian Name:** {herb}"
                    )

                    st.write(
                        f"**English Name:** {info['english']}"
                    )

                    st.write(
                        f"**Scientific Name:** "
                        f"*{info['scientific']}*"
                    )

                    st.write(
                        f"**Yoruba:** {info['yoruba']}"
                    )

                    st.write(
                        f"**Hausa:** {info['hausa']}"
                    )

                    st.write(
                        f"**Igbo:** {info['igbo']}"
                    )

                    st.warning(
                        f"**Safety Note:** {info['risk']}"
                    )

                    st.divider()

                else:

                    st.info(
                        f"🌿 **{herb} ({info['english']})** — "
                        f"*{info['scientific']}*"
                    )

                    st.write(
                        "No specific interaction flag was triggered "
                        "for this medicine–herb pair within the current "
                        "SmartRx Plus knowledge base."
                    )

                    st.divider()

            # --------------------------------------------------
            # FINAL RESULT
            # --------------------------------------------------
            if interaction_found:

                st.error(
                    "⚠️ One or more potential safety concerns were "
                    "identified. Do not combine medicines and herbal "
                    "preparations based solely on this screening result. "
                    "Consult a qualified healthcare professional."
                )

            else:

                st.success(
                    "✅ NO SPECIFIC INTERACTION FLAG TRIGGERED"
                )

                st.write(
                    "No specific high-risk interaction flag was triggered "
                    "for the selected combination within the current "
                    "SmartRx Plus knowledge base."
                )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

# ==========================================================
# HOW TO USE
# ==========================================================
elif page == "📖 How to Use":

    st.title("📖 How to Use SmartRx Plus")

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("Step 1 — Select Your Orthodox Medicine")

    st.write(
        "Choose **one orthodox medicine** from the pharmaceutical "
        "dropdown. The current version screens one selected medicine "
        "against up to four local herbs."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("Step 2 — Select Your Local Herbs")

    st.write(
        "Choose up to **four Nigerian medicinal herbs** using the "
        "four herb selection boxes."
    )

    st.write(
        "Each herb is displayed using its **local Nigerian name, "
        "English common name and scientific botanical name** so that "
        "both Nigerian and international users can identify the plant."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("Step 3 — Run the Safety Verification")

    st.write(
        "After selecting your medicine and herbs, click "
        "**RUN AI SAFETY VERIFICATION**."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("Step 4 — Understand Your Results")

    st.write(
        "A red warning indicates that the current knowledge base "
        "has triggered a potential safety screening flag."
    )

    st.write(
        "A green result means that no specific interaction flag "
        "was triggered for the selected combination in the current "
        "knowledge base."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("⚠️ Important Safety Notice")

    st.write(
        "SmartRx Plus is an educational medication-safety and "
        "decision-support screening tool. A 'clear' result does "
        "not prove that a combination is completely safe. Herbal "
        "products can vary in species, preparation, concentration "
        "and composition. Always consult a qualified doctor or "
        "pharmacist before combining medicines with herbal products."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ==========================================================
# ABOUT
# ==========================================================
else:

    st.title("ℹ️ About SmartRx Plus")

    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("🚀 The SmartRx Plus Vision")

    st.write(
        """
        **SmartRx Plus** is an emerging Nigerian digital health
        intelligence platform developed by **Chizix Orbit Digital
        Innovations Ltd.**

        The platform is designed to address an important medication-
        safety challenge: the concurrent use of orthodox medicines
        and traditional herbal preparations without adequate
        information about possible interactions.

        SmartRx Plus creates a digital bridge between pharmaceutical
        medicine information and Traditional African Medicine (TAM),
        providing users with an accessible way to screen selected
        medicine–herb combinations and understand potential safety
        concerns.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # THE PROBLEM
    # ------------------------------------------------------
    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("🎯 The Problem We Are Solving")

    st.write(
        """
        In Nigeria, people may use prescription or over-the-counter
        medicines alongside herbal preparations. However, information
        about these combinations can be difficult to find, fragmented
        across different sources, or complicated by the fact that
        medicinal plants are known by different local and regional
        names.

        This creates an information gap at the point where people
        make medication decisions.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # THE SOLUTION
    # ------------------------------------------------------
    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("💡 Our Solution")

    st.write(
        """
        SmartRx Plus provides a user-friendly safety-screening
        interface that allows a user to select an orthodox medicine
        and up to four local herbal preparations.

        The platform cross-references the selected combination against
        its structured pharmaceutical and ethnobotanical knowledge base
        and presents the result in an understandable format.

        Each plant can be identified through its:

        • Nigerian/local name

        • English common name

        • Scientific botanical name

        • Yoruba name

        • Hausa name

        • Igbo name
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # AI INNOVATION
    # ------------------------------------------------------
    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("🤖 AI & Digital Health Innovation")

    st.write(
        """
        SmartRx Plus is being developed as an AI-enabled digital
        health intelligence solution.

        Its architecture is designed to combine structured
        pharmaceutical and ethnobotanical knowledge with
        AI-powered natural-language understanding and retrieval.

        This will enable users to ask medication-safety questions
        in a more natural and accessible way while the structured
        SmartRx Plus knowledge base provides the underlying safety
        information.

        The platform is being developed with the goal of making
        advanced AI technology useful for a distinctly Nigerian
        healthcare information challenge while creating an
        architecture that can scale to other African markets.
        """
    )

    st.info(
        "AI-assisted screening is intended to support information "
        "access and decision-making. It does not replace a qualified "
        "doctor, pharmacist or other healthcare professional."
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # WHY NIGERIA
    # ------------------------------------------------------
    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("🇳🇬 Built for Nigeria, Designed for Global Relevance")

    st.write(
        """
        A major feature of SmartRx Plus is its use of local
        ethnobotanical identification.

        A plant may have completely different common names across
        communities and countries. By connecting Nigerian local
        names with English names and scientific botanical names,
        SmartRx Plus creates a common identification layer that can
        make traditional medicine information more understandable
        to both Nigerian and international users.

        The same approach can support future expansion into other
        African countries and multilingual health-information
        environments.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # CURRENT PROTOTYPE
    # ------------------------------------------------------
    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("📊 Current SmartRx Plus Prototype")

    st.write(
        f"• {len(DRUG_DATABASE)} orthodox medicine entries"
    )

    st.write(
        f"• {len(HERB_DATABASE)} traditional/local herb entries"
    )

    st.write(
        "• Four-herb selection and comparison capability"
    )

    st.write(
        "• Nigerian local-name, English and scientific plant identification"
    )

    st.write(
        "• Yoruba, Hausa and Igbo reference names"
    )

    st.write(
        "• Structured herb–drug safety screening"
    )

    st.write(
        "• Educational medication-safety guidance"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # STARTUP VISION
    # ------------------------------------------------------
    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("🌍 Startup Vision")

    st.write(
        """
        The vision for SmartRx Plus is to grow beyond a basic
        medication checker into an intelligent African medication-
        safety information platform.

        Future development can include natural-language AI
        assistance, expanded medicine and ethnobotanical databases,
        multilingual interaction, evidence-linked safety information,
        pharmacist and healthcare-provider tools, and expansion into
        additional African healthcare markets.

        The goal is simple:

        **Use AI to make medication-safety information more accessible,
        understandable and relevant to African users.**
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # DEVELOPER / COMPANY
    # ------------------------------------------------------
    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("🏢 Developer")

    st.write(
        """
        **SmartRx Plus** is developed by **Chizix Orbit Digital
        Innovations Ltd.**, a Nigerian technology and digital
        innovation company working across digital solutions,
        data analytics, artificial intelligence, web development
        and technology-driven business solutions.
        """
    )

    st.write(
        """
        SmartRx Plus is being developed as an early-stage innovation
        with the ambition of demonstrating how AI can be applied to
        solve practical, locally relevant problems in Nigeria.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # INTELLECTUAL PROPERTY
    # ------------------------------------------------------
    st.markdown(
        '<div class="section">',
        unsafe_allow_html=True
    )

    st.subheader("© Intellectual Property")

    st.write(
        """
        **SmartRx Plus™** is a proprietary digital health technology
        solution developed by **Chizix Orbit Digital Innovations Ltd.**

        © 2026 Chizix Orbit Digital Innovations Ltd.
        **All Rights Reserved.**

        The SmartRx Plus name, concept, software, interface,
        knowledge-base structure and associated digital materials
        are proprietary to Chizix Orbit Digital Innovations Ltd.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # SAFETY DISCLAIMER
    # ------------------------------------------------------
    st.warning(
        "⚠️ SmartRx Plus is a digital health information and "
        "clinical decision-support screening prototype. It does "
        "not diagnose disease, prescribe medication or replace "
        "professional medical advice. Users should consult a "
        "qualified healthcare professional before combining "
        "medicines with herbal preparations."
    )
