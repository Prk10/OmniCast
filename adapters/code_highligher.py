# adapters/code_highlighter.py
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def highlight_code_to_html(code_content: str) -> str:
    
    formatter = HtmlFormatter(style="monokai", full=True, linenos=True)

    result = highlight(code_content, PythonLexer(), formatter)
    
    return result