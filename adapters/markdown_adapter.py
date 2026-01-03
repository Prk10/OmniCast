import markdown

def render_markdown_to_html(md_content: str) -> str:

    html_body = markdown.markdown(md_content)
    
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script type="text/javascript" id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
        </script>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    return full_html