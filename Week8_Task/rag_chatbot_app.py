# import streamlit as st
# import faiss
# import pickle
# import matplotlib.pyplot as plt
# from sentence_transformers import SentenceTransformer
# from transformers import pipeline

# # Load FAISS index and documents
# index = faiss.read_index("rag_faiss_index.idx")
# with open("rag_documents.pkl", "rb") as f:
#     documents = pickle.load(f)

# # Load embedding model and LLM
# embedder = SentenceTransformer("all-MiniLM-L6-v2")
# llm = pipeline(
#     "text2text-generation",
#     model="google/flan-t5-base",  # Use flan-t5-large if available
#     device=-1,
#     model_kwargs={
#         "repetition_penalty": 1.5,
#         "no_repeat_ngram_size": 3,
#         "early_stopping": True
#     }
# )

# # RAG Function
# def rag_qa_pipeline(query, top_k=2):
#     query_embedding = embedder.encode([query])
#     _, I = index.search(query_embedding, top_k)
#     retrieved_docs = [documents[i] for i in I[0]]
#     context = "\n".join(retrieved_docs)

#     prompt = (
#         f"Context:\n{context}\n\n"
#         f"Question: {query}\n\n"
#         f"Instructions: Use the above context to identify the main factors influencing loan approval. "
#         f"Explain logically and avoid repeating the same facts. Provide an analytical response.\n\n"
#         f"Answer:"
#     )

#     response = llm(prompt, max_new_tokens=256, do_sample=True)[0]["generated_text"]
#     return response, context

# # Streamlit UI
# st.set_page_config(page_title="Loan Approval RAG Chatbot", page_icon="🤖")
# st.title("📊 Loan Approval Q&A Chatbot")
# st.write("Ask questions based on document-driven insights!")

# # Session state for chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # User query input
# query = st.text_input("🔍 Ask a question:", placeholder="e.g., What affects loan approval?")

# if query:
#     with st.spinner("Generating answer..."):
#         answer, context = rag_qa_pipeline(query)

#     # Store chat in history
#     st.session_state.chat_history.append({"query": query, "answer": answer})

#     # Display retrieved context
#     st.markdown("### 📚 Retrieved Context")
#     st.code(context)

#     # Display AI answer
#     st.markdown("### 🤖 AI Answer")
#     st.success(answer)

# # Display full chat history
# if st.session_state.chat_history:
#     st.markdown("---")
#     st.markdown("### 🕒 Chat History")
#     for chat in st.session_state.chat_history[::-1]:
#         st.markdown(f"**You:** {chat['query']}")
#         st.markdown(f"**Bot:** {chat['answer']}")
#         st.markdown("---")

# # Static chart: Loan approval rates by area
# st.markdown("### 📈 Loan Approval Rates by Area")

# areas = ["Rural", "Urban", "Semiurban"]
# approval_rates = [61.54, 65.90, 76.58]  # Replace with actual dynamic data if needed

# fig, ax = plt.subplots()
# bars = ax.bar(areas, approval_rates, color=["green", "blue", "orange"])
# ax.set_title("Loan Approval Rates by Area")
# ax.set_ylabel("Approval Rate (%)")
# ax.set_ylim(0, 100)

# # Add text labels
# for bar in bars:
#     height = bar.get_height()
#     ax.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
#                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

# st.pyplot(fig)

import streamlit as st
import faiss
import pickle
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Page config
st.set_page_config(page_title="Loan Approval RAG Chatbot", page_icon="🤖")
st.title("📊 Loan Approval Q&A Chatbot")
st.write("Ask questions based on document-driven insights!")

# --- Load components ---
@st.cache_resource
def load_faiss_and_docs():
    idx = faiss.read_index("rag_faiss_index.idx")
    with open("rag_documents.pkl", "rb") as f:
        docs = pickle.load(f)
    return idx, docs

@st.cache_resource
def load_models():
    embed = SentenceTransformer("all-MiniLM-L6-v2")
    llm_pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        device=-1,
        model_kwargs={
            "repetition_penalty": 1.5,
            "no_repeat_ngram_size": 3,
            "early_stopping": True
        }
    )
    return embed, llm_pipe

index, documents = load_faiss_and_docs()
embedder, llm = load_models()

# --- Chat Memory ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- RAG Pipeline ---
def rag_qa_pipeline(query, top_k=2):
    query_embedding = embedder.encode([query])
    _, I = index.search(query_embedding, top_k)
    retrieved_docs = [documents[i] for i in I[0]]
    context = "\n".join(retrieved_docs)

    prompt = (
        f"Context:\n{context}\n\n"
        f"Question: {query}\n\n"
        f"Instructions: Based on the context, list the top 2–3 most important factors that influence loan approval. "
        f"Be specific, use evidence from the data, and avoid repeating phrases.\n\n"
        f"Answer:"
    )

    response = llm(prompt, max_new_tokens=256, do_sample=True)[0]["generated_text"]
    return response, context

# --- Input UI ---
query = st.text_input("🔍 Ask a question:", placeholder="e.g., What affects loan approval?")

if query:
    with st.spinner("Generating answer..."):
        answer, context = rag_qa_pipeline(query)

    # Save to chat history
    st.session_state.chat_history.append({"query": query, "answer": answer, "context": context})

    # Show context
    st.markdown("### 📚 Retrieved Context")
    st.code(context)

    # Show answer
    st.markdown("### 🤖 AI Answer")
    st.success(answer)

# --- Chat history ---
if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("### 🕒 Chat History")
    for chat in st.session_state.chat_history[::-1]:
        st.markdown(f"**🧑 You:** {chat['query']}")
        st.markdown(f"**🤖 Bot:** {chat['answer']}")
        st.markdown("---")

# --- Chart Section ---
st.markdown("### 📈 Loan Approval Rates by Property Area")

# Static values (replace with dynamic if available)
areas = ["Rural", "Urban", "Semiurban"]
approval_rates = [61.54, 65.90, 76.58]  # These can be pulled dynamically from your dataset if needed

fig, ax = plt.subplots()
bars = ax.bar(areas, approval_rates, color=["green", "blue", "orange"])
ax.set_title("Loan Approval Rates by Area")
ax.set_ylabel("Approval Rate (%)")
ax.set_ylim(0, 100)

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

st.pyplot(fig)
