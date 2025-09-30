from dotenv import load_dotenv
from agents import socrates,spy,shakespeare,fabrizio
from tasks import find_topic,research,tweet,publish
from crewai import Crew,Process
import streamlit as st

load_dotenv()

# --- App Title and Description ---
st.title("Autonomous Social Media Agent 🤖")
st.markdown("This app uses a crew of AI agents to autonomously research, write, and draft a tweet about a trending topic in AI.")

if "draft_tweet" not in st.session_state:
    st.session_state.draft_tweet = None

if st.session_state.draft_tweet is None:
    st.subheader("Generate a New AI Trend Tweet")

    if st.button("🚀 Launch the AI Crew!"):
        with st.spinner("🤖 The crew is on the mission... Researching, writing, and drafting..."):
            davinci_crew = Crew(
                agents=[
                    socrates,
                    spy,
                    shakespeare
                ],
                tasks=[find_topic,
                       research,
                       tweet],
                process=Process.sequential,
                verbose=True
            )

            result = davinci_crew.kickoff()

            st.session_state.draft_tweet = result

            st.rerun()

else:
    st.subheader("📢 Review and Post Your Tweet")

    edited_tweet = st.text_area(
        "You can edit the tweet here before posting:",
        value=st.session_state.draft_tweet,
        height=200
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Approve & Post"):
            with st.spinner("🚀 Contacting Publisher Agent Fabrizio..."):

                publish.description = f"Post this tweet to X.com: '{edited_tweet}'"

                publisher_crew = Crew(
                    agents=[fabrizio],
                    tasks=[publish],
                    process=Process.sequential,
                    verbose=True
                )

                publish_result = publisher_crew.kickoff()

                st.success(publish_result)
                st.balloons()

    with col2:
        if st.button("🔄 Regenerate"):

            st.session_state.draft_tweet = None
            st.rerun()


