import streamlit as st
import json

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

# ----------------------------------------------------------------------------
# Custom styling — dark, patriotic, festive
# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

/* Base */
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp {
    background:
        radial-gradient(1200px 500px at 50% -200px, rgba(230,57,70,0.12), transparent 70%),
        radial-gradient(1000px 500px at 100% 0%, rgba(77,121,255,0.12), transparent 70%),
        #081226;
}
h1, h2, h3, h4 { font-family: 'Oswald', sans-serif; letter-spacing: 0.5px; }

/* Hero banner */
.hero {
    position: relative;
    border-radius: 18px;
    padding: 38px 30px 34px;
    margin-bottom: 8px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 10px 40px rgba(0,0,0,0.45);
}
.hero-dc {
    background:
        radial-gradient(420px 260px at 18% -40px, rgba(255,209,102,0.30), transparent 60%),
        radial-gradient(460px 300px at 82% -60px, rgba(77,121,255,0.32), transparent 60%),
        linear-gradient(135deg, #16224f 0%, #321024 100%);
}
.hero-fm {
    background:
        radial-gradient(420px 260px at 80% -50px, rgba(255,209,102,0.22), transparent 60%),
        linear-gradient(135deg, #112a52 0%, #0c1a3a 60%, #2a1020 100%);
}
.hero-eyebrow {
    font-family: 'Oswald', sans-serif;
    font-weight: 600;
    letter-spacing: 3px;
    font-size: 13px;
    color: #FFD166;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.hero-title {
    font-family: 'Oswald', sans-serif;
    font-weight: 700;
    font-size: 46px;
    line-height: 1.02;
    margin: 0 0 8px 0;
    color: #FFFFFF;
    text-shadow: 0 2px 18px rgba(0,0,0,0.45);
}
.hero-sub { font-size: 16px; color: #C9D6F5; margin: 0; max-width: 640px; }
.hero-fireworks { position: absolute; top: 0; right: 0; height: 100%; opacity: 0.9; pointer-events: none; }

/* Cost / info card */
.cardbox {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 14px;
    padding: 16px 18px;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 14px;
    padding: 14px 16px;
}
[data-testid="stMetricLabel"] p { color: #9FB0D0 !important; font-size: 13px !important; }
[data-testid="stMetricValue"] { font-family: 'Oswald', sans-serif; color: #FFFFFF; }

/* Download button — bold and patriotic */
.stDownloadButton button {
    background: linear-gradient(135deg, #E63946 0%, #B02233 100%) !important;
    color: #FFFFFF !important;
    border: 0 !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    padding: 14px 18px !important;
    box-shadow: 0 6px 22px rgba(230,57,70,0.40) !important;
}
.stDownloadButton button:hover { filter: brightness(1.08); }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 8px; }
.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 12px 12px 0 0;
    padding: 10px 18px;
    font-weight: 600;
}
.stTabs [aria-selected="true"] {
    background: rgba(230,57,70,0.18);
    border-color: rgba(230,57,70,0.5);
}

/* Expanders */
.streamlit-expanderHeader, [data-testid="stExpander"] details summary { font-weight: 500; }
[data-testid="stExpander"] {
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    background: rgba(255,255,255,0.02);
}
</style>
""", unsafe_allow_html=True)


def fireworks_svg():
    """Decorative fireworks burst for the DC hero (red/white/blue/gold)."""
    rays = ""
    import math
    cx, cy = 70, 70
    colors = ["#FFD166", "#E63946", "#4D79FF", "#FFFFFF"]
    for i in range(16):
        ang = math.radians(i * 22.5)
        x2 = cx + 56 * math.cos(ang)
        y2 = cy + 56 * math.sin(ang)
        c = colors[i % len(colors)]
        rays += f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="2.4" stroke-linecap="round"/>'
        rays += f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="2.6" fill="{c}"/>'
    return f'<svg class="hero-fireworks" viewBox="0 0 160 160" width="200" height="200">{rays}<circle cx="{cx}" cy="{cy}" r="4" fill="#FFFFFF"/></svg>'


def stars_svg():
    """Decorative star field for the Fort Meade hero."""
    import random
    random.seed(76)
    star = ('M10 0 L12.4 6.9 L19.5 7.0 L13.8 11.3 L16 18.2 '
            'L10 14 L4 18.2 L6.2 11.3 L0.5 7.0 L7.6 6.9 Z')
    out = '<svg class="hero-fireworks" viewBox="0 0 220 160" width="240" height="170">'
    for _ in range(11):
        x = random.randint(10, 200)
        y = random.randint(8, 130)
        s = random.uniform(0.5, 1.2)
        op = random.uniform(0.45, 1.0)
        out += f'<g transform="translate({x},{y}) scale({s:.2f})" opacity="{op:.2f}"><path d="{star}" fill="#FFD166"/></g>'
    out += '</svg>'
    return out


def hero(css_class, eyebrow, title, subtitle, decoration):
    st.markdown(f"""
    <div class="hero {css_class}">
        {decoration}
        <div class="hero-eyebrow">{eyebrow}</div>
        <div class="hero-title">{title}</div>
        <p class="hero-sub">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


# Global header
st.markdown("""
<div style='text-align:center; padding: 6px 0 14px;'>
    <div style="font-family:'Oswald',sans-serif; font-weight:700; font-size:30px; color:#FFFFFF;">
        🎆 Independence Week 2026 Trip Planner
    </div>
    <div style="color:#9FB0D0; font-size:15px;">Fort Meade · July 2 &nbsp;|&nbsp; Washington, DC · July 4</div>
</div>
""", unsafe_allow_html=True)

# Two tabs
tab1, tab2 = st.tabs(["🚩 Fort Meade (July 2)", "🏛️ Washington, DC (July 4)"])

# ============================================================================
# FORT MEADE TAB
# ============================================================================
with tab1:
    hero(
        "hero-fm",
        "Thursday · July 2, 2026 · Fort Meade Parade Field",
        "Fort Meade Fireworks",
        "America's 250th Birthday — Red, White &amp; Blue Celebration. Free admission, "
        "fireworks at 9:30 PM. The easy, low-cost local option.",
        stars_svg(),
    )

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
    hero(
        "hero-dc",
        "Saturday · July 4, 2026 · National Mall",
        "Washington, DC",
        "Salute to America &amp; Freedom 250 — the largest fireworks show in National Mall "
        "history (~11 PM). Tickets required. Plan transportation carefully.",
        fireworks_svg(),
    )

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
