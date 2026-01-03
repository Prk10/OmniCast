from core.renderer_interface import DocumentRenderer
from playwright.async_api import async_playwright, TimeoutError

class PlaywrightRenderer(DocumentRenderer):
    def __init__(self):
        self.playwright = None
        self.browser = None

    #called when entering the async with block
    async def __aenter__(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch()
        return self
    
    #called with exiting the async with block
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def _inject_content(self, page, html_content: str):

        if not html_content:
            raise ValueError("html file cannot be empty")
        await page.set_content(html_content)

        if "Mathjax-script" in html_content:
            try:
                await page.wait_for_selector('mjx-container', state='attached', timeout=2000)
            except TimeoutError:
                pass
        else:
            pass

    async def render(self, html_content: str) -> bytes:

        page = await self.browser.new_page()

        await self._inject_content(page, html_content)

        pdf_bytes = await page.pdf(format='A4', print_background=True)
        await page.close()

        return pdf_bytes
    
    async def screenshot(self, html_content: str) -> bytes:

        page = await self.browser.new_page()

        await self._inject_content(page, html_content)

        png_bytes = await page.screenshot(full_page=True)
        await page.close()
        return png_bytes
        
"""

class PlaywrightRenderer(DocumentRenderer):
    

    async def render(self, html_content: str) -> bytes:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.set_content(html_content) #the html content is put onto the webpage which is later converted to pdf
            pdf_bytes = await page.pdf(format="A4", print_background=True)
            await browser.close()
            return pdf_bytes
        
    async def screenshot(self, html_content: str) -> bytes:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            await page.set_content(html_content)

            try:
                await page.wait_for_selector('mjx-container', state='attached', timeout=3000)
            except TimeoutError:
                print("No equations found, proceeding!")
            
            png_bytes = await page.screenshot(full_page=True)
            await browser.close()
            return png_bytes
"""