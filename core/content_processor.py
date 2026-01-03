from adapters.markdown_adapter import render_markdown_to_html
from adapters.code_highligher import highlight_code_to_html

class ContentProcessor:
    @staticmethod
    def process(content: str, format_type: str) -> str:

        if (format_type == "markdown"):
            html_content = render_markdown_to_html(content)
        elif (format_type == "python"):
            html_content = highlight_code_to_html(content)
        
        else:
            html_content=f"""
            <!DOCTYPE html>
            <html>
            <head>
                <script type="text/javascript" id="MathJax-script" async
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
                </script>
            </head>
            <body>
                <pre>{content}</pre>
            </body>
            </html>
            """
        return html_content