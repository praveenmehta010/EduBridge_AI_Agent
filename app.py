import streamlit as st
from agent import build_agent

st.set_page_config(page_title="EduBridge", page_icon="🎓", layout="centered")


st.markdown("<h1 style='text-align: center;'>🎓 Learning Assistant AI Agent (EduBridge)</h1>",unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Get real-time, free course recommendations.</p>", unsafe_allow_html=True)
st.markdown("---")

user_input = st.text_input(
    "🔍 What do you want to learn today?",
    placeholder="e.g., beginner-level Python, machine learning, data visualization"
)


if st.button("🚀 Find Courses") and user_input:
    with st.spinner("Thinking..."):
        agent = build_agent()
        result = agent.invoke({"user_input": user_input})
        
        # if st.secrets.get("DEBUG") == "true":
        #     st.subheader("🧪 Raw JSON Result (for debugging)")
        #     st.json(result)
        #     st.write("Printing secrets for debugging:")
        # for key, value in st.secrets.items():
        #     st.write(f"{key}: {value}")

        courses = result.get("courses", [])

        if courses:
            st.success("✅ Here are your personalized course recommendations:")
            for course in courses:
                st.markdown(f"""
                    <div style="padding: 1rem; background: linear-gradient(to right, #e0f7fa, #f1f8e9); border-radius: 12px; margin-bottom: 12px;">
                        <a href="{course}" target="_blank" style="color: black; text-decoration: none; font-size: 16px;">
                    {course}
                </a>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("😕 Sorry, I couldn't find any relevant courses. Try a different topic!")

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>Made with ❤️ for SDG - Quality Education by Praveen Mehta</p>", unsafe_allow_html=True)
