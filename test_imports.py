try:
    from langchainhub import Client
    hub = Client()
    prompt = hub.pull("rlm/rag-prompt")
    print("hub works")
except Exception as e:
    print(f"hub failed: {e}")

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    ts = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    print("text_splitter works")
except Exception as e:
    print(f"text_splitter failed: {e}")
