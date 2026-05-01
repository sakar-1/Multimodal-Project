import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Maxwell's Equations: The Illusion of Understanding",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Dark theme and custom styling */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #1e3a8a 100%);
    }
    
    /* Header styles */
    .main-title {
        font-size: 3.5rem;
        font-weight: 300;
        text-align: center;
        color: #f1f5f9;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    .subtitle {
        font-size: 1.3rem;
        font-weight: 300;
        text-align: center;
        color: #94a3b8;
        margin-bottom: 3rem;
        line-height: 1.6;
    }
    
    .badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(96, 165, 250, 0.3);
        border-radius: 2rem;
        color: #93c5fd;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
        margin-bottom: 1.5rem;
    }
    
    /* Equation card styles */
    .equation-card {
        background: rgba(15, 23, 42, 0.4);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(71, 85, 105, 0.5);
        border-radius: 1rem;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .equation-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .equation-name {
        font-size: 0.9rem;
        font-weight: 500;
        color: #60a5fa;
        margin-bottom: 0.25rem;
    }
    
    .equation-desc {
        font-size: 0.75rem;
        color: #64748b;
    }
    
    .equation-number {
        width: 2.5rem;
        height: 2.5rem;
        background: rgba(59, 130, 246, 0.1);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #60a5fa;
        font-weight: 300;
    }
    
    .equation-latex {
        font-size: 3rem;
        font-weight: 300;
        color: #f1f5f9;
        padding: 1.5rem 0;
        font-family: 'Crimson Pro', serif;
        letter-spacing: 0.02em;
    }
    
    /* Question box */
    .question-box {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.05), rgba(249, 115, 22, 0.05));
        border: 2px solid rgba(245, 158, 11, 0.3);
        border-radius: 1rem;
        padding: 3rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    .question-title {
        font-size: 2.5rem;
        font-weight: 300;
        color: #fef3c7;
        margin-bottom: 1.5rem;
    }
    
    .question-text {
        font-size: 1.3rem;
        color: #e2e8f0;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .question-subtext {
        font-size: 1.1rem;
        color: #94a3b8;
        margin-top: 1rem;
    }
    
    /* Layer cards */
    .layer-card {
        border-radius: 1rem;
        padding: 2.5rem;
        margin-bottom: 2rem;
    }
    
    .layer-1 {
        background: linear-gradient(135deg, rgba(127, 29, 29, 0.4), rgba(159, 18, 57, 0.4));
        border: 2px solid rgba(239, 68, 68, 0.3);
    }
    
    .layer-2 {
        background: linear-gradient(135deg, rgba(120, 53, 15, 0.4), rgba(146, 64, 14, 0.4));
        border: 2px solid rgba(249, 115, 22, 0.3);
    }
    
    .layer-3 {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.6), rgba(51, 65, 85, 0.6));
        border: 2px solid rgba(100, 116, 139, 0.4);
    }
    
    .layer-title {
        font-size: 1.8rem;
        font-weight: 300;
        margin-bottom: 1.5rem;
    }
    
    .layer-1 .layer-title { color: #fca5a5; }
    .layer-2 .layer-title { color: #fdba74; }
    .layer-3 .layer-title { color: #cbd5e1; }
    
    .layer-text {
        font-size: 1.05rem;
        color: #e2e8f0;
        line-height: 1.7;
        margin-bottom: 1rem;
    }
    
    .layer-example {
        font-size: 0.9rem;
        color: #94a3b8;
        font-style: italic;
        margin-top: 1rem;
    }
    
    /* Quote box */
    .quote-box {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.3), rgba(67, 56, 202, 0.3));
        border: 1px solid rgba(96, 165, 250, 0.2);
        border-radius: 1rem;
        padding: 3rem;
        margin: 3rem 0;
    }
    
    .quote-mark {
        font-size: 4rem;
        color: rgba(96, 165, 250, 0.2);
        font-family: serif;
        line-height: 0.5;
        margin-bottom: 1rem;
    }
    
    .quote-text {
        font-size: 1.5rem;
        font-weight: 300;
        color: #cbd5e1;
        line-height: 1.6;
        font-style: italic;
        margin-bottom: 1.5rem;
    }
    
    .quote-author {
        color: #93c5fd;
        font-weight: 300;
        text-align: right;
        font-size: 1rem;
    }
    
    /* Final message */
    .final-message {
        text-align: center;
        font-size: 1.2rem;
        color: #94a3b8;
        font-weight: 300;
        line-height: 1.7;
        margin: 3rem 0;
    }
    
    /* Progress indicator */
    .progress-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(96, 165, 250, 0.3);
        border-radius: 2rem;
        color: #93c5fd;
        font-size: 0.85rem;
        margin-bottom: 2rem;
    }
    
    .pulse {
        width: 0.5rem;
        height: 0.5rem;
        background: #60a5fa;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Button styling */
    .stButton > button {
        background: rgba(59, 130, 246, 0.2);
        border: 1px solid rgba(96, 165, 250, 0.4);
        border-radius: 0.5rem;
        color: #93c5fd;
        font-size: 1rem;
        padding: 0.75rem 2rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: rgba(59, 130, 246, 0.3);
        border-color: rgba(96, 165, 250, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 0
    st.session_state.show_quiz = False
    st.session_state.quiz_answer = ""
    st.session_state.revealed = False
    st.session_state.auto_progress = True

# Auto-progress equations
if st.session_state.stage < 4 and st.session_state.auto_progress:
    time.sleep(0.8)
    st.session_state.stage += 1
    st.rerun()

# Maxwell's Equations
equations = [
    {
        "latex": "∇ · E = ρ/ε₀",
        "name": "Gauss's Law",
        "desc": "Electric charges create electric fields"
    },
    {
        "latex": "∇ · B = 0",
        "name": "Gauss's Law for Magnetism",
        "desc": "No magnetic monopoles exist"
    },
    {
        "latex": "∇ × E = -∂B/∂t",
        "name": "Faraday's Law",
        "desc": "Changing magnetic fields create electric fields"
    },
    {
        "latex": "∇ × B = μ₀(J + ε₀∂E/∂t)",
        "name": "Ampère-Maxwell Law",
        "desc": "Currents and changing electric fields create magnetic fields"
    }
]

# Header
st.markdown('<div style="text-align: center;"><span class="badge">THE FOUNDATION OF ELECTROMAGNETISM</span></div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">Maxwell\'s Equations</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">These equations completely describe all electromagnetic phenomena</p>', unsafe_allow_html=True)

# Progress indicator
if st.session_state.stage < 4:
    st.markdown(f'''
    <div style="text-align: center;">
        <span class="progress-badge">
            <span class="pulse"></span>
            Loading equation {st.session_state.stage + 1} of 4...
        </span>
    </div>
    ''', unsafe_allow_html=True)

# Display equations
st.markdown("<br>", unsafe_allow_html=True)
for idx, eq in enumerate(equations):
    if st.session_state.stage > idx:
        st.markdown(f'''
        <div class="equation-card">
            <div class="equation-header">
                <div>
                    <div class="equation-name">{eq["name"]}</div>
                    <div class="equation-desc">{eq["desc"]}</div>
                </div>
                <div class="equation-number">{idx + 1}</div>
            </div>
            <div class="equation-latex">{eq["latex"]}</div>
        </div>
        ''', unsafe_allow_html=True)

# The Question
if st.session_state.stage >= 4 and not st.session_state.show_quiz:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('''
    <div class="question-box">
        <div style="font-size: 3rem; opacity: 0.6; margin-bottom: 1.5rem;">👁️</div>
        <div class="question-title">You've Seen Them</div>
        <div class="question-text">
            These four equations encode the complete theory of electromagnetism. Every electrical device, 
            every electromagnetic wave, every interaction between charges and fields follows from these laws.
        </div>
        <div style="height: 1px; background: linear-gradient(to right, transparent, rgba(245, 158, 11, 0.3), transparent); margin: 2rem 0;"></div>
        <div class="question-text" style="color: #fef3c7;">
            But does just that enable someone to understand the nature and properties of electromagnetic waves?
        </div>
        <div class="question-subtext">
            Can someone design an antenna or an electric motor just by looking at these equations (these equations are all that are needed)?
        </div>
    </div>
    ''', unsafe_allow_html=True)
    

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("The Problem", use_container_width=True):
            st.session_state.revealed = True
            st.rerun()

# The Reveal
if st.session_state.revealed:
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Layer 1: Misinformation
    st.markdown('''
    <div class="layer-card layer-1">
        <div style="font-size: 2rem; margin-bottom: 1rem;">⚠️</div>
        <div class="layer-title">Layer 1: Misinformation</div>
        <div class="layer-text">
            Sometimes what you are presented is simply <strong>wrong</strong>. Popularly available explanations
            frequently contain fundamental errors.
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Layer 2: Flawed Derivations
    st.markdown('''
    <div class="layer-card layer-2">
        <div style="font-size: 2rem; margin-bottom: 1rem;">⚠️</div>
        <div class="layer-title">Layer 2: Flawed Derivations</div>
        <div class="layer-text">
            Even when the fundamental explanation is correct, the application of the fundamental knowledge into another realm are often <strong>incomplete or incorrect</strong>. 
            For example: when using the above equations in circuit analysis or encoding electromagnetic waves for telecommunication.
        </div>
        <div class="layer-example">
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Layer 3: The Illusion of Understanding
    st.markdown('''
    <div class="layer-card layer-3">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🧠</div>
        <div class="layer-title">Layer 3: The Illusion of Understanding</div>
        <div class="layer-text">
            But here's the deepest problem and the core of my argument: <strong>even when everything is correct</strong>, 
            merely listening to the explanation, seeing the equations, and watching animations creates a false sense of comprehension.
        </div>
        <div class="layer-text">
            Right here, Maxwell's equations were rendered and a sentence explained what idea each equation contained.
            One may or may not be familiar with the signs and symbols; 
            But even if you know the symbols, can you actually use them? Do you understand why changing magnetic fields create electric fields? 
            Could you explain to someone why light is an electromagnetic wave?
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Zernike Quote
    st.markdown('''
    <div class="quote-box">
        <div class="quote-mark">"</div>
        <div class="quote-text">
            I am impressed by the great limitations of the human mind. How quick are we to learn, 
            that is, to imitate what others have done or thought before. And how slow to understand, 
            that is, to see the deeper connections. Slowest of all, however, are we in inventing new 
            connections or even in applying old ideas in a new field.
        </div>
        <div class="quote-author">
            — Fritz Zernike, Nobel Laureate in Physics
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Final Message
    st.markdown('''
    <div class="final-message">
        <p>Understanding—as noted above—develops after much more effort, contemplation and experience in a particular domain, whether technical or non-technical.</p>
        <p>We are able to know things today, at an ever-increasing pace in formats much better than this through the internet, but the deluge of information might also be affecting our ability to comprehend it or see deeper connections.</p>
    </div>
    ''', unsafe_allow_html=True)
