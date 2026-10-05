import streamlit as st


# -----------------------------
# Work Done During Expansion
# -----------------------------
def work_done():
    st.header("Work Done During Expansion")

    st.latex(r"W = P(V_2 - V_1)")

    P = st.number_input(
        "Enter pressure (Pa):",
        min_value=0.0,
        value=100000.0
    )

    V1 = st.number_input(
        "Enter initial volume (m³):",
        min_value=0.0,
        value=1.0
    )

    V2 = st.number_input(
        "Enter final volume (m³):",
        min_value=0.0,
        value=2.0
    )

    if st.button("Calculate Work"):
        W = P * (V2 - V1)

        st.success(f"Work done = {W:.2f} J")


# -----------------------------
# Heat Supplied
# -----------------------------
def heat_supplied():
    st.header("Heat Supplied")

    st.latex(r"Q = mc(T_2 - T_1)")

    m = st.number_input(
        "Enter mass (kg):",
        min_value=0.0,
        value=1.0
    )

    c = st.number_input(
        "Enter specific heat capacity (J/kg K):",
        min_value=0.0,
        value=4186.0
    )

    T1 = st.number_input(
        "Enter initial temperature (K):",
        min_value=0.0,
        value=300.0
    )

    T2 = st.number_input(
        "Enter final temperature (K):",
        min_value=0.0,
        value=400.0
    )

    if st.button("Calculate Heat"):
        Q = m * c * (T2 - T1)

        st.success(f"Heat supplied = {Q:.2f} J")


# -----------------------------
# Change in Internal Energy
# -----------------------------
def change_internal_energy():
    st.header("Change in Internal Energy")

    st.latex(r"\Delta U = Q - W")

    Q = st.number_input(
        "Enter heat supplied (J):",
        value=1000.0
    )

    W = st.number_input(
        "Enter work done by the system (J):",
        value=400.0
    )

    if st.button("Calculate Internal Energy"):
        delta_U = Q - W

        st.success(
            f"Change in internal energy = {delta_U:.2f} J"
        )


# -----------------------------
# Efficiency of Heat Engine
# -----------------------------
def efficiency():
    st.header("Efficiency of Heat Engine")

    st.latex(r"\eta = \frac{W}{Q_{in}} \times 100")

    W = st.number_input(
        "Enter work output (J):",
        min_value=0.0,
        value=500.0
    )

    Qin = st.number_input(
        "Enter heat supplied (J):",
        min_value=0.0,
        value=1000.0
    )

    if st.button("Calculate Efficiency"):

        if Qin == 0:
            st.error("Heat supplied cannot be zero.")
            return

        eta = (W / Qin) * 100

        st.success(f"Efficiency = {eta:.2f} %")


# =============================
# MAIN STREAMLIT PROGRAM
# =============================

st.set_page_config(
    page_title="Thermodynamics Calculator",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Thermodynamics Calculator")

st.write(
    "Select the required calculation from the menu below."
)

st.divider()

# Menu
choice = st.selectbox(
    "Select a calculation:",
    [
        "Work done during expansion",
        "Heat supplied",
        "Change in internal energy",
        "Efficiency of a heat engine"
    ]
)

# Run selected function
if choice == "Work done during expansion":
    work_done()

elif choice == "Heat supplied":
    heat_supplied()

elif choice == "Change in internal energy":
    change_internal_energy()

elif choice == "Efficiency of a heat engine":
    efficiency()

st.divider()

st.caption("Product-1 | Thermodynamics Calculator")
