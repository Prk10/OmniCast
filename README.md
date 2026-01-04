# OmniCast: High-Fidelity Image Renderering for AI Pipelines

OmniCast is a containerized micoservice designed to bridge the gap between human readable technical documentation and Computer Vision AI pipelines. Currently, OmniCast converts structured code and scientific markup (LaTeX + Markdown) into high-resolution visual assets for Multimodal RAG pipelines.

This tool also solves the "Tokenization Limit" problem in LLMs by converting verbose code/math files into visual tokens, allowing Vision-Language Models (like GPT-4o) to analyze without consuming massive context windows

## Why this matters in 2026?
LLMs like Gemini 3.0 and GPT-5 are vision-native. Feeding them raw LaTeX text is inefficient. Feeding them pixels allows them to 'see' the equation structure just like a human does.

## 🚀 Key Features
* **Universal Rendering:** Transforms Python code and Markdown into pixel-perfect PNGs.
* **Math-Aware:** Uses MathJax to render complex mathematical equations e.g., $$E=mc^2$$
* **Async Code:** Built on FastAPI and Playwright with non blocking browser context management.
* **Containerized:** Fully Dockerized for "One-Line" deployment.

## 🛠️ Architecture
* **Language:** Python 3.10+
* **Framework:** FastAPI (Uvicorn)
* **Engine:** Headless Chromium (Playwright)

## 📸 Examples

**Python Code Rendering:**
![Code Example](assets/code.png)

**Scientific Math Rendering**
![Math Example](assets/science.png)


## 🔌 Usage & Integration

OmniCast exposes a single, high-performance endpoint: `POST /render`.

### 1. The Interactive API Docs
The easiest way to test the API is through the auto-generated documentation.
1. Ensure the container is running: `docker run -p 8080:8000 omnicast-api:v1`
2. Open your browser to: [http://localhost:8080/docs](http://localhost:8080/docs)
3. Click **POST /render** -> **Try it out**.

### 2. CLI Usage (cURL)
You can test the pipeline directly from your terminal.

**Render Python Code:**
```bash
curl -X POST "http://localhost:8080/render" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "def hello_world():\n    print(\"OmniCast works!\")",
    "format_type": "python"
  }' \
  --output code_snippet.png
```

  ### 3. 🐍 Python Integration

To integrate OmniCast into your AI agent, use this helper script:

```python
import requests

def render_code(code_snippet: str, output_filename="result.png"):
    url = "http://localhost:8080/render"
    payload = {
        "content": code_snippet,
        "format_type": "python"
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() # Check for errors
        
        with open(output_filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Success! Saved to {output_filename}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Example Usage:
if __name__ == "__main__":
    render_code("print('Hello World')")
```
