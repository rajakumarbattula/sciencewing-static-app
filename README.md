# Government Junior College, Science Wing, Karimnagar

A buildless college website using HTML5 and one CSS3 stylesheet. No JavaScript, framework, npm packages, template engine, external fonts or build tools.

## Local usage

Open `index.html` directly. All internal links and assets are relative and work with local files and GitHub Pages project URLs. Optionally run `python -m http.server 8000` from this directory and open http://localhost:8000.

## Files and pages

```text
index.html                    Homepage
*.html                        Standalone information pages (28 total)
assets/css/styles.css         Shared styles and responsive rules
assets/images/logo/           Local Telangana emblem
assets/images/college/        Local reference campus image
assets/images/staff/           Approved staff photos
assets/images/facilities/      Approved facility photos
assets/images/placeholders/   Reserved replacement assets
assets/documents/              Approved documents
scripts/validate_site.py       Dependency-free validation
.nojekyll                     Disable Jekyll processing
```

Administrative pages: `administration.html`, `teaching-staff.html`, `office-staff.html`, `admissions.html`, `scholarships.html`, `student-facilities.html`, `hostels.html`, `library.html`, `govt-initiatives.html`, `circulars.html`.

Academic pages: `courses.html`, `timetable.html`, `labs.html`, `study-material.html`, `curriculum.html`, `model-papers.html`, `sports.html`, `cultural-activities.html`, `vocational.html`, `career-guidance.html`, `examinations.html`, `counselling.html`, `anti-drugs.html`, `nss.html`, `toppers.html`, `success-stories.html`.

Also included: `index.html` and `contact.html`.

## Design and wireframes

Navy, green and gold establish a restrained institutional palette. Desktop has Administrative navigation on the left and Academic navigation on the right. Below 1101px both move above content; below 601px they stack. Native `details` / `summary` menus support mouse, keyboard and touch without JavaScript. Menus start expanded for discovery; users can collapse either. Expanded lists scroll within their menus on smaller screens.

The homepage sketch is the attachment ending `9.56.37 PM.jpeg`; the detail sketch ends `10.03.52 PM.jpeg`. Their content, rather than attachment order, determines the layout. The homepage includes notices, a campus image, welcome, principal, quick links, contact and map-search area. Detail pages retain the staff fields, admission-seat table, scholarship categories, hostel fields and library resource categories.

Each standalone page contains shared header/navigation/footer markup so opening files needs no rendering script. Update navigation on every page when adding a page. Preserve `aria-current="page"` for that page in each relevant navigation landmark. CSS has 17 documented sections and custom properties. Accessibility includes semantic landmarks, one H1, skip link, visible focus, labelled scrollable tables and print styles.

## Placeholders and unconfirmed facts

This is a prepared information template, not a live admission announcement. Pending and demo entries require college approval before publication. There are no invented people, marks, ranks, phone numbers, emails, seats or deadlines.

The reference confirms the college name and code **35002**. It lists MPC, BiPC, CEC, MLT, AET and CS; current approval, medium and availability need confirmation. Unclear sketch labels, including MEC, and crossed-out seat figures are not treated as approved offerings. The handwritten 2026–27 note does not establish an admission session or deadline.

The reference lists Mukarampura / Subhashnagar, Karimnagar, Telangana – 505001. The sketch appears to mention Gandhi Chowk and Karkhana Gadda. The full postal address is therefore explicitly pending confirmation. Handwritten coordinates are not used. The map link searches by college name and does not claim a verified entrance.

Principal/staff/contact records from the reference website were not used. On 30 October 2026, the user supplied a photograph of the college staff board to replace the directory placeholders. Names, subjects, designations, qualifications, appointment dates and contact numbers now come from that photograph. Laboratory, hostel, library-resource and service cards remain editable information structures, not claims of available services.

Before launch, college administration must confirm:

- Address, entrance, map pin, telephone, email and office hours.
- Emblem/photo publication permission and whether the campus image depicts this college.
- Principal message/photo, staff photographs, and any staff changes since the supplied board was published.
- Course titles, sanctioned offerings, session, admission status, dates, intake, vacancies and eligibility.
- Application process and current admission/scholarship document requirements.
- Scholarship schemes, categories, eligibility, amounts if applicable, dates and official links.
- Hostel authority, names, addresses, category, capacity, college-student count and contacts.
- Library holdings, newspapers, magazines, textbooks, reading area, hours and borrowing rules.
- Labs, equipment, safety instructions and practical schedules.
- Approved timetables, syllabus, study resources, papers, circulars, examination notices and result links.
- Sports/cultural activities, NSS unit status, counselling and career guidance availability.
- OJT requirements, coordinators and approved partner organisations.
- Achievement evidence, success-story facts and student/alumni publication consent.
- Official anti-drug campaign resources and government initiative information.

## Staff source and updates

Source: user-supplied `WhatsApp Image 2026-10-30 at 9.48.11 PM.jpeg`, a photograph of the college staff board (college code 35002). The photograph has no stated board publication date; 30 October 2026 is the date supplied, not an appointment or effective date. The raw photograph is not published as a site asset.

The board contains 37 named entries: principal **V. Venkata Ramana Chary**, 27 teaching staff and 9 library/office/support staff. Serial numbers 28 and 29 appear twice on the board; each distinct named record has been retained once. The librarian, P. Laxminarayana, appears in the non-teaching directory and Library page. Other teaching roles retain the printed JL, CFM and GF labels. OD Basis, U/M, GFC and vocational abbreviations are preserved without guessing employment status or an unstated medium. Name spacing and punctuation are normalised for readability; no staff identities are invented.

Dates mean **appointment in present cadre**, exactly as the board column states. They must not be relabelled as initial joining dates or website update dates. Contact numbers are transcribed from the board and use telephone links. The principal's displayed number is identified as the principal's contact, not an unverified general office telephone. The principal portrait and approved message remain pending.

Edit the `tbody` in `teaching-staff.html` or `office-staff.html` for later approved changes; add/remove complete `tr` rows and keep the first cell as `th scope="row"`. Teaching columns are name, subject/medium as displayed, designation, qualifications, appointment in present cadre and contact. The non-teaching directory omits the subject column. Keep each displayed date consistent with its `time datetime="YYYY-MM-DD"` value. Keep telephone-link destinations and accessible labels consistent with the displayed number and name.

Save optional approved photographs in `assets/images/staff/`. Add meaningful `alt`, explicit width/height and `loading="lazy"`. Update principal details together in `index.html`, `administration.html` and `contact.html`; update librarian details together in `office-staff.html` and `library.html`. Administrative office contacts also appear in `administration.html`. General office email, telephone and hours remain pending.

## Replace admission and seat data

Edit the `.status-box` fields and seat-table `tbody` in `admissions.html`. Confirm group labels, medium and current sanctioned offerings. Maintain distinct intake and available-seat columns. Add an approved effective date near the table: this static website cannot track real-time vacancies or accept applications.

Confirm the indicative document lists on Admissions and Scholarships. Remove unneeded documents and retain conditional wording where appropriate.

## Add notices

Copy an `article class="notice"` into `index.html` or `circulars.html`. Replace the title, category, sample text and Pending date. Use semantic dates such as `<time datetime="2026-10-29">29 Oct 2026</time>` only for a confirmed publication date. Replace the demo badge with `<span class="badge">New</span>` only for an actually new notice; remove old badges manually.

Save approved documents in `assets/documents/` before adding links. Use descriptive labels with the actual format and size, such as “Admission instructions (PDF, 240 KB)”. Never add guessed URLs, empty links or unavailable download buttons. Resource tables deliberately use text statuses until files exist.

## Add images

Save approved, appropriately licensed local images in the corresponding folders. Compress large photos and supply accurate alt text, dimensions and provenance records. Replace `.image-placeholder` only when a verified photo exists. Current placeholders are CSS boxes, not fabricated portraits or emblems. Confirm the reference campus image and permission before public launch.

## Validation

Run `python scripts/validate_site.py` with Python 3. It checks required pages, local links/assets/fragments, metadata, H1 counts, alt attributes, navigation/current markers and rejects fake links, script rendering and lorem ipsum.

Review 320, 375, 768, 1024, 1366 and 1920px widths after editing. Check Tab order, focus, skip link, Enter/Space menu operation, scrollable tables, 200% zoom and printing. Automated checks do not replace editorial approval or assistive-technology review.

Initial implementation verification: the static checker passed 28 pages and 1,090 link/asset references. Headless Chrome passed 76 page/viewport cases using direct local-file URLs: all pages at 320 and 1366px, plus Home, Admissions, Teaching Staff, Hostels and Library at 375, 768, 1024 and 1920px. No page-level horizontal overflow, broken images or browser console errors were found. Native menu activation with Enter was checked at 375px. Desktop and mobile homepage screenshots were visually reviewed. Screen-reader testing and deployment verification remain outside these checks.

After the 30 October staff update, the static checker passes 28 pages and 1,138 link/asset references, including the new telephone links. All six updated pages also passed 36 Chrome page/viewport cases across 320, 375, 768, 1024, 1366 and 1920px, with no page overflow, broken images or console errors. Staff row counts, date formats, telephone destinations and repeated principal/librarian details were checked for consistency. The supplied board remains the authority for the transcribed entries; it does not establish that appointments or contact details have not changed since it was printed.

## GitHub Pages deployment

1. Commit these files to `rajakumarbattula/sciencewing-static-app` and push the selected branch.
2. In **Settings → Pages**, select **Deploy from a branch**.
3. Choose that branch and **/ (root)**, then save.
4. After deployment, visit `https://rajakumarbattula.github.io/sciencewing-static-app/`.
5. Check navigation and local images on the deployed URL.

No build command, dependencies or workflow is required. Updating the GitHub branch publishes source code; website deployment depends on the repository's GitHub Pages settings.

## Sources and acknowledgements

Reviewed 29 October 2026:

- Reference: https://gjcs.ahteshamtech.com/ — identity, code, navigation terminology and reference-listed courses. Public HTML metadata/application data were inspected; the reference application code and styling are not included.
- Emblem: https://gjcs.ahteshamtech.com/images/telangana-emblem.webp saved as `assets/images/logo/telangana-emblem.webp`.
- Campus image: https://gjcs.ahteshamtech.com/images/hero-campus.jpg saved as `assets/images/college/reference-campus.jpg`.
- Two user-provided handwritten sketches — layout and requested fields. Uncertain handwriting is treated as layout intent, not authoritative institutional data.
- Staff board photograph supplied by the user on 30 October 2026 — principal and staff directory details, as described above. This source supersedes the original staff placeholders, not the unconfirmed admission or facility information.

Public availability is not a blanket copyright licence. Confirm authority and permission for institutional emblem/photo publication before launch. Attribution does not replace permission, and no ownership over reference assets is claimed.
