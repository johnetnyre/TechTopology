#!/usr/bin/env python3
from __future__ import annotations

import os
import shutil
from pathlib import Path
from urllib.parse import urljoin

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def normalize_baseurl(value: str | None) -> str:
    value = (value or "").strip()
    if not value or value == "/":
        return ""
    return "/" + value.strip("/")


site = load_yaml(ROOT / "site.yml") or {}
conference = load_yaml(ROOT / "_data" / "conference.yml")
speakers = load_yaml(ROOT / "_data" / "speakers.yml")
schedule = load_yaml(ROOT / "_data" / "schedule.yml")
lightning_abstracts = load_yaml(ROOT / "_data" / "lightning_abstracts.yml")
previous = load_yaml(ROOT / "_data" / "previous.yml")
past_speakers = load_yaml(ROOT / "_data" / "past_speakers.yml")
local = load_yaml(ROOT / "_data" / "local.yml")
photos = load_yaml(ROOT / "_data" / "photos.yml") or []

BASEURL = normalize_baseurl(os.getenv("SITE_BASEURL") or site.get("baseurl"))


def site_url(path: str) -> str:
    if path.startswith(("http://", "https://", "mailto:", "tel:")):
        return path
    if not path.startswith("/"):
        path = "/" + path
    return f"{BASEURL}{path}" or "/"


env = Environment(
    loader=FileSystemLoader(str(ROOT)),
    autoescape=select_autoescape(["html", "xml"]),
    trim_blocks=True,
    lstrip_blocks=True,
)
env.globals["url"] = site_url

def render(template_name: str, output_path: str, **context):
    template = env.get_template(template_name)
    full_context = {
        "site": site,
        "conference": conference,
        "speakers": speakers,
        "schedule": schedule,
        "lightning_abstracts": lightning_abstracts,
        "previous": previous,
        "past_speakers": past_speakers,
        "local": local,
        "photos": photos,
        **context,
    }
    html = template.render(**full_context)
    dest = OUT / output_path.lstrip("/")
    if dest.suffix != ".html":
        dest = dest / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    common_desc = site.get("description", "Tech Topology Conference at Georgia Tech")
    render("_templates/home.html", "/", page_title="Home", page_slug="home", page_path="/", meta_description=common_desc)
    render("_templates/schedule.html", "/schedule/", page_title="Schedule", page_slug="schedule", page_path="/schedule/", meta_description=f"{conference['year']} Tech Topology conference schedule, lightning talks, and abstracts.")
    render("_templates/participants.html", "/participants/", page_title="Participants", page_slug="participants", page_path="/participants/", meta_description=f"Speakers and participants for the {conference['year']} Tech Topology Conference.")
    render("_templates/registration.html", "/registration/", page_title="Registration & Support", page_slug="registration", page_path="/registration/", meta_description=f"Registration and support information for the {conference['year']} Tech Topology Conference.")
    render("_templates/local.html", "/local-information/", page_title="Local Information", page_slug="local-information", page_path="/local-information/", meta_description="Venue, hotels, campus map, and local information for Tech Topology at Georgia Tech.")
    render("_templates/photos.html", "/photos/", page_title="Photos", page_slug="photos", page_path="/photos/", meta_description=f"Photos from the {conference['year']} Tech Topology Conference.")
    render("_templates/past-speakers.html", "/past-speakers/", page_title="Past Speakers", page_slug="past-speakers", page_path="/past-speakers/", meta_description="Past colloquium and invited speakers at Tech Topology conferences.")
    render("_templates/previous.html", "/previous-conferences/", page_title="Previous Conferences", page_slug="previous-conferences", page_path="/previous-conferences/", meta_description="Archive of previous Tech Topology conferences at Georgia Tech.")
    render("_templates/contact.html", "/contact/", page_title="Contact", page_slug="contact", page_path="/contact/", meta_description="Contact the organizers of the Tech Topology Conference.")
    render("_templates/accessibility.html", "/accessibility/", page_title="Accessibility", page_slug="accessibility", page_path="/accessibility/", meta_description="Accessibility statement for the Tech Topology Conference website.")
    render("_templates/404.html", "/404.html", page_title="Page Not Found", page_slug="404", page_path="", meta_description="Page not found.")

    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    print(f"Built {OUT}")


if __name__ == "__main__":
    main()
