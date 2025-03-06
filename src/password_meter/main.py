import streamlit as st
import re
import plotly.graph_objects as go

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    elif len(password) >= 8:
        feedback.append("🔸 Password should be at least 12 characters for better security.")
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character.")
    
    # Determine Strength Message
    if score == 4:
        strength = "✅ Cyber-Secure Password!"
    elif score == 3:
        strength = "⚠️ Moderate Encryption Level"
    else:
        strength = "❌ Security Breach Risk Detected"
    
    return score, strength, feedback

# Configure the page
st.set_page_config(page_title="PassMeter", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Ubuntu+Mono&display=swap');
    
    body {
        background: #FFFFFF;
    }
    .reportview-container {
        background: radial-gradient(circle at center, #F0F0F0, #FFFFFF);
    }
    h1 {
        font-family: 'Orbitron', sans-serif;
        color: #000000;
        text-align: center;
    }
    .stTextInput input {
        background: rgba(0, 0, 0, 0.1) !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 5px;
        font-family: 'Ubuntu Mono', monospace;
    }
    .stButton>button {
        width: 100%;
        background: #000000 !important;
        color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px #000000;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("## 🔐 PassMeterX")  
st.markdown("*Measure. Secure. Dominate Your Password Strength.*")


password = st.text_input("ENTER PASSWORD:", type="password")

if st.button("INITIATE SCAN"):
    if password:
        score, strength, feedback = check_password_strength(password)
        progress_percentage = int((score / 4) * 100)
        
        # Black and white gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=progress_percentage,
            domain={'x': [0, 1], 'y': [0, 1]},
            number={
                'font': {'size': 48, 'color': "#000000", 'family': "Orbitron"},
                'prefix': "",
                'suffix': "%"},
            gauge={
                'axis': {
                    'range': [0, 100],
                    'tickwidth': 1,
                    'tickcolor': "#000000",
                    'dtick': 25,
                    'tickfont': {'size': 16, 'color': "#000000"}},
                'bar': {'color': "#000000", 'thickness': 0.25},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 2,
                'bordercolor': "#000000",
                'steps': [
                    {'range': [0, 25], 'color': 'rgba(100, 100, 100, 0.7)'},
                    {'range': [25, 50], 'color': 'rgba(150, 150, 150, 0.7)'},
                    {'range': [50, 75], 'color': 'rgba(200, 200, 200, 0.7)'},
                    {'range': [75, 100], 'color': 'rgba(250, 250, 250, 0.7)'}],
                'threshold': {
                    'line': {'color': "#000000", 'width': 4},
                    'thickness': 0.75,
                    'value': progress_percentage}}
        ))

        fig.update_layout(
            height=400,
            margin=dict(l=50, r=50, t=100, b=50),
            font={'color': "#000000", 'family': "Orbitron"},
            paper_bgcolor='rgba(0,0,0,0)',
            annotations=[dict(
                text="SECURITY LEVEL",
                x=0.5,
                y=0.6,
                font_size=24,
                showarrow=False,
                font_color="#000000"
            )]
        )

        st.plotly_chart(fig, use_container_width=True)
        
        # Results display
        st.markdown(f"""
            <div style="border: 2px solid #000000; padding: 20px; border-radius: 10px; margin: 20px 0;">
                <h3 style="color:#000000; font-family: Orbitron; margin:0;">SCAN RESULTS</h3>
                <p style="color:#000000; font-family: Ubuntu Mono;">STRENGTH RATING: {score}/4</p>
                <p style="color:{'#00FF00' if score ==4 else '#FFD700' if score==3 else '#FF0000'}; 
                   font-family: Orbitron; font-size: 18px;">{strength}</p>
            </div>
            """, unsafe_allow_html=True)
        
        if feedback:
            st.markdown("""
                <div style="border: 2px solid #000000; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h4 style="color:#000000; font-family: Orbitron; margin-top:0;">SECURITY PROTOCOL SUGGESTIONS:</h4>
            """, unsafe_allow_html=True)
            for msg in feedback:
                st.markdown(f"""
                    <div style="color:#000000; font-family: Ubuntu Mono; padding: 5px 0; 
                                border-left: 3px solid {'#FF007F' if '❌' in msg else '#FFD700'}; 
                                padding-left: 10px;">
                        ➺ {msg.replace('❌', '🚫').replace('🔸', '⚠️')}
                    </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("⚠️ PASSWORD REQUIRED")

st.markdown("""
    <div style="position: fixed; bottom: 10px; width: 100%; text-align: center; color: #000000; 
               font-family: Ubuntu Mono;">
    CYBERSECURITY AI v3.14 © 2077 | ALL SYSTEMS OPERATIONAL
    </div>
    """, unsafe_allow_html=True)