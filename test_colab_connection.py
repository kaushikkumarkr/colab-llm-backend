import os
from openai import OpenAI

# ==============================================================================
# 🎯 INSTRUCTIONS:
# 1. Run the `colab_llm_backend.ipynb` notebook in Google Colab Pro.
# 2. Wait for the `cloudflared` cell to print your TUNNEL URL.
#    It looks something like: "https://your-random-words.trycloudflare.com"
# 3. Paste that EXACT URL below.
# ==============================================================================

# 👉 Paste your Cloudflare Tunnel URL here:
COLAB_TUNNEL_URL = "https://czwof-34-126-119-41.a.free.pinggy.link"

# The OpenAI client needs the standard `/v1` suffix appended to the base URL
OLLAMA_BASE_URL = f"{COLAB_TUNNEL_URL}/v1"

# We initialize the generic OpenAI client.
# Ollama provides an OpenAI-compatible API so all your LangChain / LlamaIndex
# code will work unmodified if you pass this client.
# The API key can be anything since the local Ollama server doesn't validate it.
client = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="sk-no-key-required",
    default_headers={"Bypass-Tunnel-Reminder": "true"} # Required to bypass Localtunnel's warning page
)

def test_colab_connection():
    print(f"🔗 Connecting to Colab Model via: {OLLAMA_BASE_URL}")
    print("⏳ Waiting for response (this tests your Colab GPU speed!)...")
    
    try:
        # We query the mistral model (or whichever one you pulled in Colab)
        response = client.chat.completions.create(
            model="mistral",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant running on Google Colab hardware."},
                {"role": "user", "content": "Hello! Where are you currently running from?"}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        reply = response.choices[0].message.content
        print("\n✅ CONNECTION SUCCESSFUL!")
        print("🤖 Model Response:")
        print("-" * 40)
        print(reply)
        print("-" * 40)
        
    except Exception as e:
        print("\n❌ CONNECTION FAILED!")
        print(f"Error details: {e}")
        print("\nTroubleshooting Tips:")
        print("1. Did you paste the correct Tunnel URL?")
        print("2. Is the Colab Notebook still running?")
        print("3. Did the `ollama serve` or `cloudflared` process crash in Colab?")

if __name__ == "__main__":
    test_colab_connection()
