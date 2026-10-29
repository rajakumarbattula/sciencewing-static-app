"""Validate the buildless website using only Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = set('index administration teaching-staff office-staff admissions scholarships student-facilities hostels library govt-initiatives circulars courses timetable labs study-material curriculum model-papers sports cultural-activities vocational career-guidance examinations counselling anti-drugs nss toppers success-stories contact'.split())


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.tags = []
        self.ids = set()
        self.refs = []
        self.current = []
        self.errors = []
        self.feed(path.read_text(encoding='utf-8-sig'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append((tag, a))
        if 'id' in a:
            if a['id'] in self.ids:
                self.errors.append('Duplicate ID: ' + a['id'])
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if key in a:
                self.refs.append(a[key])
        if tag == 'img' and not a.get('alt'):
            self.errors.append('Image missing descriptive alt')
        if tag == 'a' and a.get('aria-current') == 'page':
            self.current.append(a.get('href'))


def validate():
    pages = {p.name: Page(p) for p in ROOT.glob('*.html')}
    errors = []
    for name in REQUIRED:
        if name + '.html' not in pages:
            errors.append('Missing page: ' + name)
    checked = 0
    for name, page in pages.items():
        failures = list(page.errors)
        counts = lambda tag: sum(t == tag for t, _ in page.tags)
        for tag in ('h1', 'main', 'title', 'header', 'footer'):
            if counts(tag) != 1:
                failures.append(f'Expected exactly one {tag}')
        for meta in ('description', 'viewport'):
            if not any(t == 'meta' and a.get('name') == meta and a.get('content') for t, a in page.tags):
                failures.append('Missing metadata: ' + meta)
        if not any(t == 'meta' and a.get('charset', '').lower() == 'utf-8' for t, a in page.tags):
            failures.append('Missing UTF-8 charset')
        if not any(t == 'html' and a.get('lang') == 'en' for t, a in page.tags):
            failures.append('Missing page language')
        for label in ('Administrative', 'Academic', 'Primary'):
            if not any(t == 'nav' and a.get('aria-label') == label for t, a in page.tags):
                failures.append('Missing navigation: ' + label)
        if not page.current or any(ref != name for ref in page.current):
            failures.append('Incorrect current-page navigation')
        if counts('script'):
            failures.append('Unexpected JavaScript')
        raw = page.path.read_text(encoding='utf-8').lower()
        if 'lorem ipsum' in raw or 'style=' in raw:
            failures.append('Unwanted filler or inline styling')
        if not raw.lstrip().startswith('<!doctype html>'):
            failures.append('Missing HTML5 doctype')
        for ref in page.refs:
            checked += 1
            url = urlsplit(ref)
            if not ref or ref == '#' or url.scheme in ('javascript', 'data'):
                failures.append('Fake link: ' + ref)
                continue
            if url.scheme or url.netloc:
                continue
            if ref.startswith('/'):
                failures.append('Root-relative URL breaks local/GitHub project usage: ' + ref)
            target = page.path.parent / unquote(url.path) if url.path else page.path
            if not target.is_file():
                failures.append('Missing local destination: ' + ref)
            if url.fragment and target.name in pages and unquote(url.fragment) not in pages[target.name].ids:
                failures.append('Missing fragment: ' + ref)
        errors.extend(name + ': ' + error for error in failures)
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages; {checked} link/asset references; metadata, landmarks, current navigation and placeholders checked.')


if __name__ == '__main__':
    validate()
