# %%writefile app.py
import streamlit as st
from ui_generator import generate_ui # Ensure ui_generator.py is in the same directory

# 🧠 Streamlit UI Configuration
st.set_page_config(
    page_title="Text-to-UI Generator",
    layout="wide", # Use wide layout to maximize horizontal space
    initial_sidebar_state="collapsed" # Optionally collapse sidebar by default
)

# Initialize session state variables for storing generated HTML and view mode
if 'html_code' not in st.session_state:
    st.session_state.html_code = None
if 'full_screen_mode' not in st.session_state:
    st.session_state.full_screen_mode = False

# --- Header Section ---
st.title("🧠 Text-to-UI Generator")
st.markdown("---") # A simple separator for visual clarity

# --- Input Field Section ---
# The text area for the user's UI prompt
prompt = st.text_area(
    "Enter your UI prompt:",
    "Generate a modern, responsive landing page for a tech company with a hero section, services, and a contact form.",
    height=150 # Fixed height for the input prompt area
)

# --- Buttons Row ---
col_buttons1, col_buttons2 = st.columns([0.8, 0.2]) # Adjust column width for buttons

with col_buttons1:
    if st.button("Generate UI", use_container_width=True, help="Click to generate HTML code based on your prompt"):
        st.session_state.full_screen_mode = False # Reset to split view on new generation
        with st.spinner("Generating code... Please wait."):
            try:
                st.session_state.html_code = generate_ui(prompt)
                if not st.session_state.html_code:
                    st.warning("No HTML code was generated. Please try a different prompt or check the model's response.")
            except Exception as e:
                st.error(f"❌ An error occurred during UI generation: {e}")
                st.info("Please ensure your OpenRouter API key is correctly set and the model is accessible.")

with col_buttons2:
    # Only show the full-screen toggle if HTML code has been generated
    if st.session_state.html_code:
        if st.button("Switch View", use_container_width=True, help="Switch between split view and full-screen preview"):
            st.session_state.full_screen_mode = not st.session_state.full_screen_mode
            # Rerun to apply the view mode change
            st.rerun() # Use st.rerun() in newer Streamlit versions

st.markdown("---") # Another separator

# --- Display Area (Conditional Rendering) ---
if st.session_state.html_code:
    if st.session_state.full_screen_mode:
        # Full-screen preview mode
        st.markdown("### 👁️ Full Screen Preview")
        st.components.v1.html(st.session_state.html_code, height=900, scrolling=True) # Larger height for full screen
    else:
        # Split view mode (default)
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📝 Generated HTML Code")
            st.code(st.session_state.html_code, language="html", height=600)

        with col2:
            st.markdown("### 👁️ Live Preview")
            st.components.v1.html(st.session_state.html_code, height=600, scrolling=True)
else:
    st.info("Enter a prompt above and click 'Generate UI' to see the magic happen!")

# --- Optional: Instructions/Tips for the User ---
st.markdown(
    """
    ---
    **Tips for better UI generation:**
    * Be specific and detailed in your prompt (e.g., "a responsive login form with email, password, and a 'Forgot Password' link").
    * Mention desired colors, themes (e.g., "dark theme", "minimalist design").
    * Specify components you want (e.g., "a navigation bar", "a product grid with 3 items", "a contact form with validation").
    * Request specific interactivity (e.g., "a dropdown menu that appears on hover").
    """
)
