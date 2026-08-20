import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="SmartRx Plus",
    page_icon="💊",
    layout="wide"
)

# ==========================================================
# CUSTOM STYLING
# SmartRx NG colour system retained
# Only the main title/heading area uses Indigo
# ==========================================================
st.markdown("""
<style>

.stApp {
    background: #FAFBFC;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* SmartRx Plus Hero */
.hero {
    background: linear-gradient(
        135deg,
        #4338CA,
        #6366F1
    );
    color: white;
    padding: 35px;
    border-radius: 20px;
    border-left: 10px solid #F9CC48;
    margin-bottom: 20px;
    box-shadow: 0 8px 32px rgba(31, 38, 135, 0.20);
    backdrop-filter: blur(12px);
}

.card {
    background: #FFFFFF;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(20,70,124,0.10);
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 15px;
}

.safe {
    background-color: #D1FAE5;
    padding: 20px;
    border-radius: 12px;
    border-left: 8px solid green;
    margin-bottom: 15px;
}

.warning {
    background-color: #FEF3C7;
    padding: 20px;
    border-radius: 12px;
    border-left: 8px solid orange;
    margin-bottom: 15px;
}

.danger {
    background-color: #FEE2E2;
    padding: 20px;
    border-radius: 12px;
    border-left: 8px solid red;
    margin-bottom: 15px;
}

.footer {
    text-align: center;
    padding: 20px;
    color: #444;
    margin-top: 30px;
}

h1, h2, h3, h4 {
    color: #4338CA;
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
# NIGERIAN / TRADITIONAL HERBAL DATABASE
# ==========================================================
HERB_DATABASE = {

    "Dogonyaro": {
        "english": "Neem",
        "scientific": "Azadirachta indica",
        "yoruba": "Dogonyaro",
        "hausa": "Dogonyaro",
        "igbo": "Akoko",
        "classes": ["Analgesics", "Antimalarials"],
        "risk": "Potential liver-safety concern when concentrated or excessive herbal preparations are combined with medicines that can also affect the liver."
    },

    "Ewe-Awo": {
        "english": "Sweet Wormwood",
        "scientific": "Artemisia annua",
        "yoruba": "Ewe-Awo",
        "hausa": "Tazargade",
        "igbo": "Agbara",
        "classes": ["Antimalarials"],
        "risk": "Potential concern because Artemisia annua contains artemisinin-related compounds and unstandardized herbal preparations may have unpredictable concentrations."
    },

    "Ileke": {
        "english": "Madagascar Periwinkle",
        "scientific": "Catharanthus roseus",
        "yoruba": "Ileke",
        "hausa": "Periwinkle",
        "igbo": "Agbara",
        "classes": ["Antimalarials"],
        "risk": "This plant contains potent alkaloids and should not be treated as an ordinary herbal drink. Potential toxicity and medicine interaction concerns require professional guidance."
    },

    "Atale": {
        "english": "Ginger",
        "scientific": "Zingiber officinale",
        "yoruba": "Atale",
        "hausa": "Citta",
        "igbo": "Jinja",
        "classes": ["NSAIDs"],
        "risk": "Potential additive effects on bleeding risk may require caution when concentrated preparations are combined with medicines that affect platelet function or bleeding."
    },

    "Ata-Iru": {
        "english": "African Pepper",
        "scientific": "Xylopia aethiopica",
        "yoruba": "Ata-Iru",
        "hausa": "Kimba",
        "igbo": "Uda",
        "classes": ["NSAIDs"],
        "risk": "Traditional preparations may have pharmacological effects that warrant caution when combined with medicines affecting pain, inflammation or bleeding."
    },

    "Ewuro": {
        "english": "Bitter Leaf",
        "scientific": "Vernonia amygdalina",
        "yoruba": "Ewuro",
        "hausa": "Shuwaka",
        "igbo": "Olugbu",
        "classes": ["Antibiotics"],
        "risk": "Potential herb–medicine interaction requires caution because the composition and concentration of traditional preparations can vary considerably."
    },

    "Aayu": {
        "english": "Garlic",
        "scientific": "Allium sativum",
        "yoruba": "Aayu",
        "hausa": "Tafarnuwa",
        "igbo": "Ayuu",
        "classes": ["Antibiotics"],
        "risk": "Garlic may influence drug metabolism and platelet function. Concentrated preparations may therefore warrant professional review alongside medicines."
    },

    "Efinrin": {
        "english": "Scent Leaf",
        "scientific": "Ocimum gratissimum",
        "yoruba": "Efinrin",
        "hausa": "Daddoya",
        "igbo": "Nchanwu",
        "classes": ["Antiprotozoals"],
        "risk": "Potential interaction concern with medicines such as metronidazole; concentrated herbal preparations should be reviewed by a healthcare professional."
    },

    "Atare": {
        "english": "Alligator Pepper",
        "scientific": "Aframomum melegueta",
        "yoruba": "Atare",
        "hausa": "Citta Gida",
        "igbo": "Ose Oji",
        "classes": ["Cold & Flu"],
        "risk": "May have stimulant and cardiovascular effects. Caution is appropriate when used with medicines that can influence blood pressure or heart rate."
    },

    "Ahon Erin": {
        "english": "Aloe Vera",
        "scientific": "Aloe vera",
        "yoruba": "Ahon Erin",
        "hausa": "Suku",
        "igbo": "Efe Inyanya",
        "classes": ["Gut Health"],
        "risk": "Oral aloe preparations may have laxative effects and can affect fluid and electrolyte balance."
    },

    "Zogale": {
        "english": "Moringa",
        "scientific": "Moringa oleifera",
        "yoruba": "Ewe Igbale",
        "hausa": "Zogale",
        "igbo": "Okwe Oyibo",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Atale Pupa": {
        "english": "Turmeric",
        "scientific": "Curcuma longa",
        "yoruba": "Atale Pupa",
        "hausa": "Kurkum",
        "igbo": "Turmeric",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Ewe Gova": {
        "english": "Guava Leaf",
        "scientific": "Psidium guajava",
        "yoruba": "Ewe Gova",
        "hausa": "Goba",
        "igbo": "Akwukwo Gova",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Kooko Oba": {
        "english": "Lemongrass",
        "scientific": "Cymbopogon citratus",
        "yoruba": "Kooko Oba",
        "hausa": "Tsamiya",
        "igbo": "Achara Lemon",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Zobo": {
        "english": "Hibiscus",
        "scientific": "Hibiscus sabdariffa",
        "yoruba": "Zobo",
        "hausa": "Yakwua",
        "igbo": "Zobo",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Uziza": {
        "english": "West African Pepper",
        "scientific": "Piper guineense",
        "yoruba": "Iyere",
        "hausa": "Masoro",
        "igbo": "Uziza",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Utazi": {
        "english": "Utazi",
        "scientific": "Gongronema latifolium",
        "yoruba": "Arokeke",
        "hausa": "Utazi",
        "igbo": "Utazi",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Orogbo": {
        "english": "Bitter Kola",
        "scientific": "Garcinia kola",
        "yoruba": "Orogbo",
        "hausa": "Namijin Goro",
        "igbo": "Aki Ilu",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Kanafuru": {
        "english": "Clove",
        "scientific": "Syzygium aromaticum",
        "yoruba": "Kanafuru",
        "hausa": "Kanumfari",
        "igbo": "Kanafuru",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Na'ana": {
        "english": "Mint",
        "scientific": "Mentha spicata",
        "yoruba": "Mint",
        "hausa": "Na'ana",
        "igbo": "Mint",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Efirin": {
        "english": "African Basil",
        "scientific": "Ocimum basilicum",
        "yoruba": "Efirin",
        "hausa": "Basil",
        "igbo": "Nchanwu",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Ewe Ibepe": {
        "english": "Pawpaw Leaf",
        "scientific": "Carica papaya",
        "yoruba": "Ewe Ibepe",
        "hausa": "Ganyen Gwanda",
        "igbo": "Akwukwo Okwuru",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Thyme": {
        "english": "Thyme",
        "scientific": "Thymus vulgaris",
        "yoruba": "Thyme",
        "hausa": "Thyme",
        "igbo": "Thyme",
        "classes": [],
        "risk": "No specific class match is currently configured in the SmartRx Plus knowledge base. Interaction status requires further evidence review."
    },

    "Agbo Jedi": {
        "english": "Traditional Polyherbal Decoction",
        "scientific": "Polyherbal formulation",
        "yoruba": "Agbo Jedi",
        "hausa": "Maganin Gargajiya",
        "igbo": "Agbo",
        "classes": [],
        "risk": "Composition varies between preparations. Because the ingredients and concentrations may be unknown, professional advice is recommended before combining with medicines."
    }
}


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================
def render_footer():
    st.markdown(
        """
        <div class="footer">
            <strong>SmartRx Plus</strong><br>
            © 2026 Chizix Orbit Digital Innovations Ltd.
            All Rights Reserved.<br>
            Promoting safer medication decisions through digital
            health intelligence 🇳🇬
        </div>
        """,
        unsafe_allow_html=True
    )


def herb_display_label(herb_name):
    info = HERB_DATABASE[herb_name]

    return (
        f"{herb_name} ({info['english']}) — "
        f"{info['scientific']}"
    )


# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================
st.sidebar.title("💊 SmartRx Plus")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "ℹ️ About",
        "📘 How To Use",
        "🔍 Verify Your Medicines"
    ]
)


# ==========================================================
# HOME PAGE
# ==========================================================
if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero">

        <h1 style="color:white;">💊 SmartRx Plus</h1>

        <h3 style="color:white;">
        Medication Safety & Traditional Medicine Intelligence
        </h3>

        <p>
        SmartRx Plus is an emerging Nigerian digital health
        platform designed to help users screen combinations
        of orthodox medicines and traditional herbal
        preparations for potential safety concerns.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
            <h3>💊 Orthodox Medicines</h3>
            Select multiple medicines at once and screen them
            against the SmartRx Plus pharmaceutical knowledge base.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
            <h3>🌿 Traditional Herbs</h3>
            Select up to four local herbs using Nigerian,
            English and scientific plant identification.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
            <h3>🔍 Safety Screening</h3>
            Cross-reference selected medicines and herbs
            for potential safety concerns in the current
            SmartRx Plus knowledge base.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div style="
        background:#FFF8DC;
        padding:25px;
        border-radius:20px;
        border-left:8px solid #F9CC48;
        box-shadow:0 8px 20px rgba(0,0,0,0.08);
        margin-top:20px;
        ">

        <h3 style="color:#4338CA;">
        💡 Why SmartRx Plus?
        </h3>

        <p style="color:#111111;">
        Nigerians may use orthodox medicines alongside
        traditional herbal preparations, yet information about
        potential interactions can be difficult to access.
        </p>

        <p style="color:#111111;">
        SmartRx Plus creates a digital bridge between
        pharmaceutical information and Traditional African
        Medicine through a structured ethnobotanical
        reference layer.
        </p>

        <p style="color:#111111;">
        The platform is designed to evolve toward AI-powered
        natural-language medication-safety assistance.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">

        <h3>📊 Current Prototype</h3>

        <p>
        <strong>{len(DRUG_DATABASE)}</strong>
        orthodox medicine entries
        </p>

        <p>
        <strong>{len(HERB_DATABASE)}</strong>
        traditional/local herb entries
        </p>

        <p>
        Up to <strong>4 herbs</strong> can be screened against
        multiple selected orthodox medicines.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# ABOUT PAGE
# ==========================================================
elif page == "ℹ️ About":

    st.title("ℹ️ About SmartRx Plus")

    st.markdown(
        '<div class="card">',
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
        information about potential interactions.

        SmartRx Plus creates a digital bridge between pharmaceutical
        medicine information and Traditional African Medicine (TAM),
        providing users with an accessible way to screen selected
        medicine–herb combinations and understand potential safety
        concerns.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="card">',
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

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("💡 Our Solution")

    st.write(
        """
        SmartRx Plus provides a user-friendly safety-screening
        interface that allows users to select multiple orthodox
        medicines and up to four local herbal preparations.

        The platform cross-references selected combinations against
        its structured pharmaceutical and ethnobotanical knowledge
        base and presents potential safety concerns in an
        understandable format.

        Each plant can be identified through its local Nigerian name,
        English common name, scientific botanical name, Yoruba name,
        Hausa name and Igbo name.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="card">',
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

        This future AI layer can help users ask medication-safety
        questions naturally while the structured SmartRx Plus
        knowledge base provides the underlying safety information.

        The long-term vision is to apply advanced AI technology to
        a distinctly Nigerian healthcare information challenge
        while creating an architecture that can scale across
        African healthcare markets.
        """
    )

    st.info(
        "AI-assisted screening is intended to support information "
        "access and decision-making. It does not replace a qualified "
        "doctor, pharmacist or other healthcare professional."
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🇳🇬 Built for Nigeria, Designed for Global Relevance")

    st.write(
        """
        A major feature of SmartRx Plus is its use of local
        ethnobotanical identification.

        A plant may have different common names across communities
        and countries. By connecting Nigerian local names with
        English names and scientific botanical names, SmartRx Plus
        creates a common identification layer that can make
        traditional medicine information more understandable to
        both Nigerian and international users.

        This approach can support future expansion into other
        African countries and multilingual health-information
        environments.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="card">',
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
        "• Multiple orthodox medicine selection"
    )

    st.write(
        "• Up to four local herb selections"
    )

    st.write(
        "• Local, English and scientific plant identification"
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

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🌍 Startup Vision")

    st.write(
        """
        The vision for SmartRx Plus is to grow beyond a basic
        medication checker into an intelligent African
        medication-safety information platform.

        Future development can include natural-language AI
        assistance, expanded medicine and ethnobotanical databases,
        multilingual interaction, evidence-linked safety
        information, pharmacist and healthcare-provider tools,
        and expansion into additional African healthcare markets.

        The goal is simple:

        **Use AI to make medication-safety information more
        accessible, understandable and relevant to African users.**
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="card">',
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

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="card">',
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

    st.warning(
        "⚠️ SmartRx Plus is a digital health information and "
        "clinical decision-support screening prototype. It does "
        "not diagnose disease, prescribe medication or replace "
        "professional medical advice. Users should consult a "
        "qualified healthcare professional before combining "
        "medicines with herbal preparations."
    )


# ==========================================================
# HOW TO USE PAGE
# ==========================================================
elif page == "📘 How To Use":

    st.title("📘 How To Use SmartRx Plus")

    st.markdown(
        """
        <div class="hero">

        <h1 style="color:white;">How to Use SmartRx Plus</h1>

        <p>
        Follow these simple steps to screen your selected
        orthodox medicines and traditional herbal preparations.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
        <h3>Step 1 — Select Your Medicines 💊</h3>
        <p>
        Go to <strong>Verify Your Medicines</strong> and use the
        medicine selector to choose <strong>as many orthodox
        medicines as you need</strong>.
        </p>
        <p>
        You can select multiple medicines from the same selection
        box. There is no artificial five-medicine limit.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
        <h3>Step 2 — Select Your Local Herbs 🌿</h3>
        <p>
        Select up to <strong>four local herbs</strong>.
        </p>
        <p>
        Each dropdown displays the Nigerian/local name,
        English name and scientific botanical name to help
        users identify the correct plant.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
        <h3>Step 3 — Run the Safety Verification 🔍</h3>
        <p>
        Click <strong>RUN SAFETY VERIFICATION</strong>.
        SmartRx Plus checks each selected orthodox medicine
        against each selected herb in the current knowledge base.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
        <h3>Step 4 — Review the Results 📋</h3>
        <p>
        If a potential interaction is found, the report displays
        the medicine, drug class, local herb name, English name,
        scientific name and available Nigerian language names.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
        <h3>Step 5 — Understand the Safety Status ⚠️</h3>

        <p>
        <strong>Red:</strong> A potential high-risk combination
        was flagged by the current SmartRx Plus knowledge base.
        </p>

        <p>
        <strong>Yellow:</strong> Additional caution or evidence
        review may be required.
        </p>

        <p>
        <strong>Green:</strong> No matching high-risk interaction
        was identified in the current knowledge base.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.warning(
        "Important: A result showing no flagged interaction does "
        "not prove that a combination is universally safe. Always "
        "consult a qualified pharmacist or doctor before making "
        "medication decisions."
    )


# ==========================================================
# VERIFY YOUR MEDICINES PAGE
# ==========================================================
elif page == "🔍 Verify Your Medicines":

    st.title("🔍 Verify Your Medicines")

    st.write(
        "Select multiple orthodox medicines and up to four "
        "local herbs to screen the combination."
    )

    # ======================================================
    # ORTHODOX MEDICINES
    # ======================================================
    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("💊 1. Select Orthodox Medicines")

    st.caption(
        "You can select as many medicines as needed from the "
        "database. Click the box and choose multiple medicines."
    )

    selected_drugs = st.multiselect(
        "Orthodox Medicines",
        options=sorted(DRUG_DATABASE.keys()),
        placeholder="Search and select multiple medicines..."
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ======================================================
    # LOCAL HERBS
    # ======================================================
    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🌿 2. Select Up to Four Local Herbs")

    st.caption(
        "Each herb is displayed with its local Nigerian name, "
        "English name and scientific botanical name."
    )

    herb_options = ["None"] + sorted(
        [
            herb_display_label(herb)
            for herb in HERB_DATABASE
        ]
    )

    reverse_herb_lookup = {
        herb_display_label(herb): herb
        for herb in HERB_DATABASE
    }

    herb1 = st.selectbox(
        "Herb 1",
        herb_options,
        key="herb1"
    )

    herb2 = st.selectbox(
        "Herb 2",
        herb_options,
        key="herb2"
    )

    herb3 = st.selectbox(
        "Herb 3",
        herb_options,
        key="herb3"
    )

    herb4 = st.selectbox(
        "Herb 4",
        herb_options,
        key="herb4"
    )

    selected_herbs = []

    for selected_label in [herb1, herb2, herb3, herb4]:

        if selected_label != "None":

            herb_name = reverse_herb_lookup[selected_label]

            if herb_name not in selected_herbs:
                selected_herbs.append(herb_name)

    st.markdown("</div>", unsafe_allow_html=True)

    # ======================================================
    # RUN VERIFICATION
    # ======================================================
    if st.button(
        "🔍 RUN SAFETY VERIFICATION",
        use_container_width=True
    ):

        if not selected_drugs:

            st.warning(
                "Please select at least one orthodox medicine."
            )

        elif not selected_herbs:

            st.warning(
                "Please select at least one local herb."
            )

        else:

            # ==================================================
            # SELECTED MEDICINES SUMMARY
            # ==================================================
            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            st.subheader("📋 Selected Medicines")

            for drug in selected_drugs:

                st.write(
                    f"• **{drug}** — "
                    f"{DRUG_DATABASE[drug]}"
                )

            st.markdown("</div>", unsafe_allow_html=True)

            # ==================================================
            # SELECTED HERBS SUMMARY
            # ==================================================
            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            st.subheader("🌿 Selected Herbs")

            for herb in selected_herbs:

                info = HERB_DATABASE[herb]

                st.write(
                    f"• **{herb}** — "
                    f"{info['english']} — "
                    f"*{info['scientific']}*"
                )

            st.markdown("</div>", unsafe_allow_html=True)

            # ==================================================
            # SCREENING ENGINE
            # ==================================================
            st.subheader("🔬 Safety Screening Results")

            interaction_found = False
            class_review_found = False

            # --------------------------------------------------
            # LEVEL 1: ORTHODOX-TO-ORTHODOX CLASS REVIEW
            # --------------------------------------------------
            selected_classes = [
                DRUG_DATABASE[drug]
                for drug in selected_drugs
            ]

            class_counts = {}

            for drug_class in selected_classes:

                class_counts[drug_class] = (
                    class_counts.get(drug_class, 0) + 1
                )

            repeated_classes = {
                drug_class: count
                for drug_class, count in class_counts.items()
                if count > 1
            }

            if repeated_classes:

                class_review_found = True

                st.markdown(
                    """
                    <div class="warning">
                    <h3>⚠️ Same Drug Class Detected</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                for drug_class, count in repeated_classes.items():

                    matching_drugs = [
                        drug
                        for drug in selected_drugs
                        if DRUG_DATABASE[drug] == drug_class
                    ]

                    st.write(
                        f"**{drug_class}:** "
                        f"{', '.join(matching_drugs)}"
                    )

                    st.write(
                        "Multiple medicines from the same therapeutic "
                        "class were selected. This does not by itself "
                        "prove duplication, but the combination should "
                        "be reviewed carefully."
                    )

            # --------------------------------------------------
            # LEVEL 2: ORTHODOX → HERB SCREENING
            # --------------------------------------------------
            for drug in selected_drugs:

                drug_class = DRUG_DATABASE[drug]

                for herb in selected_herbs:

                    info = HERB_DATABASE[herb]

                    if drug_class in info["classes"]:

                        interaction_found = True

                        st.markdown(
                            """
                            <div class="danger">
                            <h3>
                            🚨 Potential Herb–Drug Interaction Flag
                            </h3>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        st.write(
                            f"**Orthodox Medicine:** {drug}"
                        )

                        st.write(
                            f"**Drug Class:** {drug_class}"
                        )

                        st.write(
                            f"**Local Name:** {herb}"
                        )

                        st.write(
                            f"**English Name:** "
                            f"{info['english']}"
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

                        st.write(
                            f"**Risk / Evidence Note:** "
                            f"{info['risk']}"
                        )

                        st.divider()

            # --------------------------------------------------
            # NO DIRECT INTERACTION FOUND
            # --------------------------------------------------
            if not interaction_found:

                st.markdown(
                    """
                    <div class="safe">
                    <h3>✅ No Potential Interaction Flagged</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.write(
                    "No matching high-risk herb–drug combination "
                    "was identified within the current SmartRx Plus "
                    "knowledge base."
                )

                if class_review_found:

                    st.write(
                        "However, the selected medicines contain "
                        "repeated therapeutic classes. Review those "
                        "medicines carefully with a pharmacist or doctor."
                    )

            # --------------------------------------------------
            # GENERAL SAFETY GUIDANCE
            # --------------------------------------------------
            st.subheader("💡 Safety Guidance")

            st.write(
                "• Do not combine medicines simply because they "
                "have different brand names."
            )

            st.write(
                "• Check active ingredients and therapeutic classes "
                "before taking multiple medicines."
            )

            st.write(
                "• Tell your pharmacist or doctor about herbal "
                "preparations you are using."
            )

            st.write(
                "• Avoid assuming that a natural product is "
                "automatically safe."
            )

            st.write(
                "• Seek professional advice when the composition "
                "or dose of a traditional preparation is unknown."
            )

            st.info(
                "⚠️ Disclaimer: SmartRx Plus provides educational "
                "information and structured safety screening. "
                "A flagged or unflagged result is not a diagnosis "
                "or a substitute for professional medical advice."
            )


# ==========================================================
# COPYRIGHT FOOTER
# ==========================================================
render_footer()
