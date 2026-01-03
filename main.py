import asyncio
from adapters.playwright_renderer import PlaywrightRenderer
from adapters.code_highligher import highlight_code_to_html
from adapters.markdown_adapter import render_markdown_to_html
from core.content_processor import ContentProcessor

async def main():

    inputs = [
        {"type": "python", "file": "main.py", "output": "code.png"},
        {"type": "markdown", "file": "README.md", "output": "science.png"}
    ]

    async with PlaywrightRenderer() as renderer:

        for items in inputs:
            with open(items['file'], "r") as f:
                raw_data = f.read()

            html_content = ContentProcessor.process(raw_data, items['type'])

            data_bytes = await renderer.screenshot(html_content)

            with open(items['output'], "wb") as f:
                f.write(data_bytes)

    

if __name__ == '__main__':
    asyncio.run(main())