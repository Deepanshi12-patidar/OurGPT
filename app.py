# # import os
# # from dotenv import load_dotenv
# # from groq import Groq

# # load_dotenv()
# # client = Groq(
# #     api_key=os.environ.get("GROQ_API_KEY"),
# # )

# # user_input = input("Enter your question: ")
# # chat_completion = client.chat.completions.create(
# #     messages=[
# #         {
# #             "role": "user",
# #             "content": user_input,
# #         }
# #     ],
# #     model="llama-3.3-70b-versatile",
# # )

# # print(chat_completion.choices[0].message.content)




# import os
# from dotenv import load_dotenv
# import streamlit as st
# from groq import Groq

# load_dotenv()
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# # Set page title
# st.title("Chat with Groq AI")

# # Initialize chat history in session state if it doesn't exist
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Display chat history
# for message in st.session_state.chat_history:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# # Chat input
# if prompt := st.chat_input("What's on your mind?"):
#     # Add user message to chat history
#     st.session_state.chat_history.append({"role": "user", "content": prompt})
    
#     # Display user message
#     with st.chat_message("user"):
#         st.write(prompt)

#     # Get AI response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response = client.chat.completions.create(
#                 messages=[
#                     {"role": "user", "content": prompt}
#                 ],
#                 model="llama-3.3-70b-versatile",
#             )
#             ai_response = response.choices[0].message.content
#             st.write(ai_response)
    
#     # Add AI response to chat history
#     st.session_state.chat_history.append({"role": "assistant", "content": ai_response})





# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# user_input = input("Enter your question: ")
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": user_input,
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# print(chat_completion.choices[0].message.content)




import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key from Streamlit secrets or environment variable
api_key = st.secrets["GROQ_API_KEY"] if "GROQ_API_KEY" in st.secrets else os.environ.get("GROQ_API_KEY")

# Check if API key exists
if not api_key:
    st.error("⚠️ GROQ_API_KEY is not set. Please set it in your .env file or Streamlit secrets.")
    st.stop()

# Initialize Groq client
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"⚠️ Error initializing Groq client: {str(e)}")
    st.stop()

# Set page title
st.title("Chat with Groq AI")

# Initialize chat history in session state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
            )
            ai_response = response.choices[0].message.content
            st.write(ai_response)
    
    # Add AI response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
