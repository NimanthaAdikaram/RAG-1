import streamlit as st
from rag_with_palm import RAGPaLMQuery
# Instantiate the class
rag_palm_query_instance = RAGPaLMQuery()

# Main title with a book emoji
st.title("SmartTutors 📚")

# Subtopic 1
st.header("EduSmart Academy")

# Content for Subtopic 1
st.write("Unlock the world of knowledge with EduSmart Academy's 'SmartTutors'—your companions in unraveling the wonders of mathematics, science, and literature. Empowering students to conquer complex concepts with ease and confidence. 📚✨ #EduSmartAcademy #SmartLearning")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("Explore the world and make it a better place!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = rag_palm_query_instance.query_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})