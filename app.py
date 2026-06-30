import streamlit as st
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="July 4th Trip Planner",
    page_icon="🎆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load highlights data
with open("data/highlights.json", "r") as f:
    data = json.load(f)

fm = data["fort_meade"]
dc = data["dc_july4"]

# Header
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1>🎆 July 4th Independence Week Trip Planner</h1>
        <p style='font-size: 18px; color: #7d8a9c;'>Fort Meade & Washington, DC Events</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# Two tabs
tab1, tab2 = st.tabs(["🚩 Fort Meade (July 2)", "🏛️ Washington, DC (July 4)"])

# ============================================================================
# FORT MEADE TAB
# ============================================================================
with tab1:
    # PDF Download — at the top for quick access
    with open("assets/fort-meade.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Full Fort Meade PDF",
            data=pdf_file.read(),
            file_name="FortMeade_July2_2026_Fireworks.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary",
            key="download_fm_top"
        )

    st.markdown("---")

    # Event Summary
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📅 Date", "July 2, 2026")
    with col2:
        st.metric("🕐 Time", "4:00 PM - 10 PM")
    with col3:
        st.metric("🎆 Fireworks", "9:30 PM")
    with col4:
        st.metric("💰 Cost", "$45-85")

    st.markdown("---")

    # Quick Highlights
    st.subheader("🎯 Quick Highlights")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ What to Bring")
        for item in fm["what_to_bring"]:
            st.write(f"• {item}")

        st.markdown("### 🚫 What NOT to Bring")
        for item in fm["not_allowed"]:
            st.write(f"• {item}")

    with col2:
        st.markdown("### 🎫 ID Requirements")
        st.info(
            "**DoD ID Holders:** Mapes/32, Mapes/175, or Rockenbach/175 gates\n\n"
            "**Everyone Else:** Reece/175 gate with REAL ID-compliant license/passport. "
            "All passengers 18+ need valid ID."
        )

        st.markdown("### ⚠️ Heat Safety")
        st.warning(
            "Highs near 100°F with high humidity. Plan for shade breaks, "
            "sunscreen, and extra water. The 6-8 PM period will be the hottest."
        )

    st.markdown("---")

    # Itinerary
    st.subheader("📍 Event Timeline")

    for item in fm["itinerary"]:
        with st.expander(f"{item['time']} — {item['activity'][:40]}..."):
            st.write(item["activity"])

    st.markdown("---")

    # Cost Breakdown
    st.subheader("💵 Cost Breakdown (Group of 4)")

    cost_col1, cost_col2 = st.columns(2)

    with cost_col1:
        st.write("**Expense**")
        st.write("Admission")
        st.write("Parking")
        st.write("Gas")
        st.write("Food & Drinks")
        st.write("---")
        st.write("**TOTAL**")

    with cost_col2:
        st.write("**Amount**")
        st.write(fm["cost_breakdown"]["admission"])
        st.write(fm["cost_breakdown"]["parking"])
        st.write(fm["cost_breakdown"]["gas"])
        st.write(fm["cost_breakdown"]["food_drinks"])
        st.write("---")
        st.write(f"**{fm['cost_breakdown']['total']}**")

# ============================================================================
# DC TAB
# ============================================================================
with tab2:
    # PDF Download — at the top for quick access
    with open("assets/dc-july4.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Full DC July 4 PDF",
            data=pdf_file.read(),
            file_name="DC_July4_2026_Itinerary.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary",
            key="download_dc_top"
        )

    st.markdown("---")

    # Key Action - Registration
    st.error(
        "🚨 **ACTION REQUIRED:** Register for free fireworks tickets at "
        "[events.freedom250.org](https://events.freedom250.org) — Max 4 per phone number. "
        "You must verify the confirmation text or your reservation won't lock in."
    )

    st.markdown("---")

    # Event Summary
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📅 Date", "July 4, 2026")
    with col2:
        st.metric("🕐 Time", "10:00 AM - Midnight")
    with col3:
        st.metric("🎆 Fireworks", "~11:00 PM")
    with col4:
        st.metric("💰 Cost (Rec.)", "$160-240")

    st.markdown("---")

    # Key Alerts
    st.subheader("⚠️ Important Information")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔥 Heat Alert")
        st.warning(
            "Forecast: 100°F with heat index 105–110°F\n\n"
            "• Bring refillable water bottle (clear bags only)\n"
            "• Plan 2-6 PM in air-conditioned Smithsonian museums (free!)\n"
            "• Lotion sunscreen (no spray)"
        )

        st.markdown("### 🛡️ Security & What to Bring")
        st.info(
            "✅ **Required:**\n"
            "• Government-issued photo ID\n"
            "• One small clear bag (or small clutch)\n"
            "• Sunscreen, water, snacks\n\n"
            "❌ **Prohibited:**\n"
            "• Chairs, coolers, aerosols\n"
            "• Glass containers\n"
            "• Spray sunscreen, bug spray"
        )

    with col2:
        st.markdown("### 🚌 Transportation (Recommended: Drive + Metro)")
        st.success(
            "**Why This Works:**\n"
            "✅ Free weekend parking at Greenbelt Metro (20-25 min from Fort Meade)\n"
            "✅ Free Metro rides after 5 PM (covers entire return trip)\n"
            "✅ Metro runs until 2 AM (only option for late fireworks)\n\n"
            "**Timeline:**\n"
            "8:30 AM - Leave Fort Meade\n"
            "10:00 AM - Arrive National Mall\n"
            "12:30-1:30 AM - Drive home"
        )

        st.markdown("### ⛔ Why NOT Train?")
        st.error(
            "MARC & Amtrak stop before 11 PM fireworks:\n"
            "• MARC: Last train 10:55 PM\n"
            "• Amtrak: Last train 10:00 PM\n\n"
            "You'd need costly rideshare ($80-150+) to get home."
        )

    st.markdown("---")

    # Transportation Comparison Table
    st.subheader("🚗 Transportation Options Comparison")

    transport_data = []
    for option in dc["transportation_options"]:
        transport_data.append({
            "Method": option["method"],
            "Get There?": "✅ Yes" if option["get_there"] == "Yes" else "⚠️ " + option["get_there"],
            "Get Home?": "✅ Yes" if option["get_home"] == "Yes" else "❌ No",
            "Why": option["reason"]
        })

    st.dataframe(transport_data, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Itinerary
    st.subheader("📍 Detailed Timeline")

    for item in dc["itinerary"]:
        with st.expander(f"{item['time']} — {item['activity'][:50]}..."):
            st.write(item["activity"])

    st.markdown("---")

    # Cost Breakdown
    st.subheader("💵 Cost Estimates (Group of 4)")

    # Create three columns for three scenarios
    cost_scenarios = dc["cost_breakdown"]

    for scenario in cost_scenarios:
        with st.expander(f"📊 {scenario.get('plan', 'Plan')}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Expense**")
                st.write("Parking")
                st.write("Transit Fare")
                st.write("Gas")
                st.write("Return Trip")
                st.write("Food & Drinks")
                st.write("---")
                st.write("**TOTAL**")
            with col2:
                st.write("**Amount**")
                st.write(scenario.get("parking", "—"))
                st.write(scenario.get("transit_fare", "—"))
                st.write(scenario.get("gas", "—"))
                st.write(scenario.get("return", "—"))
                st.write(scenario.get("food_drinks", "—"))
                st.write("---")
                st.write(f"**{scenario.get('total', '—')}**")

    st.markdown("---")

    # Resources
    st.subheader("🔗 Useful Resources")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Tickets & Registration")
        st.markdown("[📋 Register for Fireworks](https://events.freedom250.org)")

    with col2:
        st.markdown("### Transit")
        st.markdown("[🚇 Metro SmarTrip](https://wmata.com)")
        st.markdown("[🚂 MARC Tickets](https://mta.maryland.gov)")

    with col3:
        st.markdown("### Event Info")
        st.markdown("[📍 Official Event Info](https://250.dc.gov)")
        st.markdown("[🅿️ ParkWhiz Parking](https://parkwhiz.com)")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #7d8a9c; font-size: 12px;'>"
    "Last Updated: June 30, 2026 | Check 250.dc.gov, mta.maryland.gov, wmata.com for final updates"
    "</div>",
    unsafe_allow_html=True
)
