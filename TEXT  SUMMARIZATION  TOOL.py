# 📌 Prerequisites (Install these if not already installed):
# pip install transformers torch

from transformers import pipeline

# Function to summarize text
def summarize_text(text, max_length=130, min_length=30):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# ------------------------
# 🔍 EXAMPLE USAGE
# ------------------------
if _name_ == "_main_":
    article = """
    Artificial intelligence (AI) is rapidly transforming industries across the globe.
    From automating mundane tasks to making complex decisions, AI is at the forefront
    of technological advancement. Companies are increasingly integrating AI-powered
    tools into their business operations to improve efficiency and customer experience.
    However, with these advancements come concerns over job displacement, ethical
    decision-making, and data privacy. As the world navigates this new frontier,
    it becomes crucial to establish regulatory frameworks and ethical guidelines
    to ensure that AI is used responsibly and equitably.
    """

    print("📝 Original Article:\n", article)
    summarized = summarize_text(article)
    print("\n🧾 Summarized Text:\n", summarized)
