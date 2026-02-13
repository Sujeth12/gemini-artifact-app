import streamlit as st
from google import genai

st.set_page_config(
    page_title="Gemini Historical Artifact Description",
    page_icon="🏺",
    layout="wide"
)

st.title("🏺 Gemini Historical Artifact Description")
st.markdown("""
Generate detailed, AI-powered descriptions of historical artifacts using Google's Gemini 2.0 Flash model.
Simply input an artifact name or historical period and specify your desired word count!
""")

with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Enter your Google API Key:", type="password")
    st.markdown("[Get your API key](https://aistudio.google.com/)")
    
    st.markdown("---")
    st.markdown("### About")
    st.info("""
    This app uses Google's Gemini 2.0 Flash to generate engaging 
    historical artifact descriptions with interesting facts.
    """)

col1, col2 = st.columns([2, 1])

with col1:
    artifact_input = st.text_input(
        "Enter artifact name or historical period:",
        placeholder="e.g., Tutankhamun's Golden Mask, Renaissance Period, Ancient Rome"
    )

with col2:
    word_count = st.number_input(
        "Desired word count:",
        min_value=100,
        max_value=2000,
        value=500,
        step=50
    )

if st.button("🎨 Generate Description", type="primary", use_container_width=True):
    if not api_key:
        st.error("⚠️ Please enter your Google API key in the sidebar!")
    elif not artifact_input:
        st.error("⚠️ Please enter an artifact name or historical period!")
    else:
        try:
            client = genai.Client(api_key=api_key)
            
            prompt = f"""
            Write a detailed and engaging description about {artifact_input} 
            in approximately {word_count} words. 
            
            The description should include:
            - Historical context and significance
            - Physical characteristics and craftsmanship
            - Cultural and artistic importance
            - Interesting facts or discoveries
            
            Also, include one fascinating historical fact related to this artifact 
            or time period that most people might not know.
            
            Make the description informative yet engaging for a general audience.
            """
            
            with st.spinner("🤖 Gemini AI is generating your description..."):
                response = client.models.generate_content(
                    model='gemini-2.0-flash-lite',
                    contents=prompt
                )
                
            st.success("✅ Description generated successfully!")
            
            st.markdown("### 📜 Generated Description")
            st.markdown(response.text)
            
            actual_words = len(response.text.split())
            st.info(f"📊 Generated {actual_words} words (Target: {word_count} words)")
            
            st.download_button(
                label="📥 Download Description",
                data=response.text,
                file_name=f"{artifact_input.replace(' ', '_')}_description.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("Please check your API key and try again.")

st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Powered by Google Gemini 2.0 Flash | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)