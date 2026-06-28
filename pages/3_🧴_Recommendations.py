import streamlit as st

st.title("🧴 Product Recommendations")

skin = st.session_state.get("skin")

if skin is None:
    st.warning("Analyze your skin first.")
    st.stop()

recommendations = {

    "Oily":[
        "Oil Free Cleanser",
        "Niacinamide Serum",
        "Gel Moisturizer",
        "SPF 50 Sunscreen"
    ],

    "Dry":[
        "Cream Cleanser",
        "Hyaluronic Acid",
        "Ceramide Moisturizer",
        "SPF 30"
    ],

    "Combination":[
        "Gentle Face Wash",
        "Vitamin C",
        "Light Moisturizer",
        "SPF 50"
    ],

    "Normal":[
        "Gentle Cleanser",
        "Vitamin C",
        "Daily Moisturizer",
        "SPF 50"
    ],

    "Sensitive":[
        "Fragrance Free Cleanser",
        "Ceramide Cream",
        "Mineral Sunscreen"
    ]
}

st.subheader(f"Detected Skin Type : {skin}")

for product in recommendations[skin]:
    st.write("✅", product)