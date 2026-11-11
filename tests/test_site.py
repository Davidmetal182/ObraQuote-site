"""Lightweight checks for the public static ObraQuote landing page."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
PUBLIC_EMAIL = "contato.obraquote@gmail.com"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.urls = []
        self.title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        for name in ("href", "src", "poster"):
            if attributes.get(name):
                self.urls.append(attributes[name])
        if tag == "title":
            self.title = True


class LandingPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (PUBLIC / "index.html").read_text(encoding="utf-8")
        cls.js = (PUBLIC / "site-config.js").read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.html)

    def test_html_structure(self):
        self.assertTrue(self.parser.title)
        self.assertIn('lang="pt-BR"', self.html)
        for anchor in ("inicio", "como-funciona", "recursos", "demonstracao", "duvidas", "participar"):
            self.assertIn(anchor, self.parser.ids)

    def test_all_local_assets_and_anchors_exist(self):
        for address in self.parser.urls:
            with self.subTest(url=address):
                if address.startswith("#"):
                    self.assertIn(unquote(address[1:]), self.parser.ids)
                    continue
                parts = urlsplit(address)
                if parts.scheme in ("http", "https", "mailto", "tel", "data") or address.startswith("//"):
                    continue
                self.assertFalse(address.startswith("/"), "Site assets should be relative, not absolute")
                asset = (PUBLIC / unquote(parts.path)).resolve()
                self.assertTrue(asset.is_relative_to(PUBLIC.resolve()))
                self.assertTrue(asset.is_file(), f"Missing site asset: {address}")

    def test_commercial_contact_is_configured(self):
        self.assertIn(PUBLIC_EMAIL, self.js)
        self.assertIn(PUBLIC_EMAIL, self.html)
        self.assertIn('id="interest-form"', self.html)
        self.assertIn('id="form-feedback"', self.html)
        self.assertIn("mailto:", self.html)

    def test_all_demonstration_assets(self):
        for path in (
            "assets/app-screenshot.webp", "assets/orcamento-example.webp",
            "assets/video-poster.webp", "assets/obraquote-demo.mp4", "assets/favicon.svg",
        ):
            self.assertTrue((PUBLIC / path).is_file())

    def test_no_private_application_sources_in_site(self):
        for forbidden in ("src/gui.py", "src/obrate_core.py", ".env", "tokens.json", "output/orcamento_cliente.pdf"):
            self.assertFalse((ROOT / forbidden).exists(), f"Don't publish: {forbidden}")

    def test_netlify_configuration(self):
        config = (ROOT / "netlify.toml").read_text(encoding="utf-8")
        self.assertRegex(config, r'publish\s*=\s*"public"')


if __name__ == "__main__":
    unittest.main()
