"""Generate portfolio detail pages from project definitions."""
from pathlib import Path

ROOT = Path(__file__).parent
IMG = "assets/img/portfolio"
PLACEHOLDER = f"{IMG}/no-img.webp"

PROJECTS = [
    {
        "slug": "boarding-house",
        "title": "Boarding House Room Management and Tenant Billing System",
        "subtitle": "Web-based records and rental tracking system",
        "category": "Management System",
        "capstone": True,
        "description": "An automated web application designed to streamline boarding house operations, including real-time room availability tracking, tenant profile management, monthly billing generation, and payment history reporting.",
        "tech": ["PHP", "MySQL", "JavaScript"],
        "images": [f"{IMG}/boarding_house_dashboard.png"],
    },
    {
        "slug": "bookease",
        "title": "BookEase: Web-Based Appointment Scheduling and Reservation Platform",
        "subtitle": "Streamlined booking portal for service-oriented platforms",
        "category": "Booking System",
        "capstone": True,
        "description": "A comprehensive online reservation platform developed to simplify client scheduling, manage service slots, send automated notifications, and provide administrators with booking analytics.",
        "tech": ["PHP", "MySQL", "Bootstrap"],
        "images": [f"{IMG}/bookease_dashboard.png"],
    },
    {
        "slug": "discoverbn",
        "title": "DiscoverBN: Local Business Directory and Tourism Information System",
        "subtitle": "Interactive discovery portal for local businesses and tourist spots",
        "category": "Web Application",
        "capstone": True,
        "description": "A web portal designed to promote local tourism by featuring detailed business listings, historical tourist landmarks, interactive maps, and community recommendations.",
        "tech": ["JavaScript", "HTML", "CSS"],
        "images": [f"{IMG}/discoverbn_web.png"],
    },
    {
        "slug": "divingracia-lujan",
        "title": "Divingracia Lujan Business Records and Management Information System",
        "subtitle": "Custom business operations and transaction tracking system",
        "category": "Management System",
        "capstone": True,
        "description": "A custom-tailored management information system built to centralize operational records, automate transaction processes, and generate business performance reports.",
        "tech": ["PHP", "MySQL", "JavaScript"],
        "images": [PLACEHOLDER],
    },
    {
        "slug": "deoripig-payroll",
        "title": "Deoripig Payroll and Attendance Monitoring System",
        "subtitle": "Automated salary computation and HR records system",
        "category": "Payroll System",
        "capstone": True,
        "description": "A secure web-based payroll system featuring automated salary calculation, attendance tracking, government deduction computation, and payslip generation.",
        "tech": ["PHP", "MySQL", "JavaScript"],
        "images": [f"{IMG}/payroll_system_mockup_1780015451610.png", f"{IMG}/books-1.jpg", f"{IMG}/books-2.jpg"],
    },
    {
        "slug": "electivote",
        "title": "ElectiVote: Cross-Platform Mobile Voting System with Real-Time Analytics",
        "subtitle": "Secure mobile election platform built with Flutter and Firebase",
        "category": "Mobile Application",
        "capstone": True,
        "description": "A secure cross-platform mobile application developed using Flutter and Firebase, featuring student identification verification, anonymous voting, and real-time visual tallying of election results.",
        "tech": ["Flutter", "Firebase", "Node.js"],
        "images": [
            f"{IMG}/electivote_mockup_1779986115319.png",
            f"{IMG}/app-1.jpg",
            f"{IMG}/app-2.jpg",
        ],
        "file": "electivote-details.html",
    },
    {
        "slug": "medical-inventory",
        "title": "Medical Clinic Inventory and Supply Management System with Automated Stock Alerts",
        "subtitle": "Inventory tracking and automated alert system for clinic supplies",
        "category": "Management System",
        "capstone": True,
        "description": "A Django-powered inventory management system for medical clinics designed to log pharmaceutical stock, monitor expiration dates, and send automated notifications when supplies fall below critical levels.",
        "tech": ["Python", "Django", "PostgreSQL"],
        "images": [
            f"{IMG}/medical_inventory_mockup_1780015263434.png",
            f"{IMG}/branding-1.jpg",
            f"{IMG}/branding-2.jpg",
        ],
        "file": "medical-details.html",
    },
    {
        "slug": "mini-hotel",
        "title": "Mini Hotel Room Reservation and Booking Management System",
        "subtitle": "Room occupancy tracking and reservation portal",
        "category": "Booking System",
        "capstone": True,
        "description": "A web-based hotel booking system managing room reservations, guest check-in/check-out logs, housekeeping status, and billing details.",
        "tech": ["PHP", "MySQL", "JavaScript"],
        "images": [PLACEHOLDER],
    },
    {
        "slug": "nobleza-pet-care",
        "title": "Nobleza Pet Care Services Reservation and Grooming Appointment System",
        "subtitle": "Client booking and groomer scheduling application",
        "category": "Booking System",
        "capstone": True,
        "description": "A modern appointment booking and service scheduling portal for pet care centers, allowing owners to schedule grooming slots and staff to manage service capacity.",
        "tech": ["React", "Node.js", "MongoDB"],
        "images": [
            f"{IMG}/appointment_mockup_1779986298631.png",
            f"{IMG}/product-1.jpg",
            f"{IMG}/product-2.jpg",
        ],
    },
    {
        "slug": "network-simulation",
        "title": "Gamified Network Simulation and Interactive Learning Platform",
        "subtitle": "Educational web application for networking concepts",
        "category": "Web Application",
        "capstone": True,
        "description": "An interactive educational web game developed to simulate network topologies, addressing configurations, and routing logic for IT students.",
        "tech": ["JavaScript", "HTML", "CSS"],
        "images": [PLACEHOLDER],
    },
    {
        "slug": "pagamuma",
        "title": "Pagamuma: Maternal Health Education and Support Web Portal",
        "subtitle": "Informational website and resource guide for pregnant women",
        "category": "Web Application",
        "capstone": True,
        "description": "An educational web platform providing pregnant women with centralized health guidelines, prenatal care trackers, and supportive developmental milestones.",
        "tech": ["HTML", "CSS", "JavaScript"],
        "images": [PLACEHOLDER],
    },
    {
        "slug": "pnp-farms",
        "title": "PNP Firearms Inventory Tracking and Records Management System",
        "subtitle": "Secure monitoring and management system for PNP firearms",
        "category": "Management System",
        "capstone": True,
        "description": "A secure record-keeping and inventory system designed for law enforcement agencies to track firearm registrations, assignments, maintenance logs, and custody transfers.",
        "tech": ["PHP", "MySQL", "JavaScript"],
        "images": [PLACEHOLDER],
    },
    {
        "slug": "passi-city",
        "title": "Passi City Tourist Destination Finder and Tourism Information Portal",
        "subtitle": "Web-based tourism guide and interactive map of Passi City",
        "category": "Web Application",
        "capstone": True,
        "description": "A public information portal built to highlight Passi City's cultural heritage and tourist destinations, featuring interactive location reviews and guide resources.",
        "tech": ["PHP", "MySQL", "JavaScript"],
        "images": [PLACEHOLDER],
    },
    {
        "slug": "retail-management",
        "title": "Integrated Retail Point of Sale (POS) and Inventory Management System",
        "subtitle": "Custom sales transaction and inventory control system",
        "category": "Management System",
        "capstone": True,
        "description": "A web-based POS system designed to process customer sales, track real-time product inventory levels, manage supplier records, and compile daily sales analytics.",
        "tech": ["PHP", "jQuery", "MySQL"],
        "images": [f"{IMG}/rms-1.jpg", f"{IMG}/rms-2.jpg", f"{IMG}/rms-3.jpg", f"{IMG}/rms-4.jpg"],
        "file": "rms-details.html",
    },
    {
        "slug": "pototan-payroll",
        "title": "Pototan National Comprehensive High School Payroll and Employee Records System",
        "subtitle": "School payroll computation and employee management system",
        "category": "Payroll System",
        "capstone": True,
        "description": "A customized school payroll system that automates employee salary distribution, tax computation, benefits tracking, and digital payslip generation.",
        "tech": ["PHP", "MySQL", "JavaScript"],
        "images": [PLACEHOLDER],
    },
    {
        "slug": "erp-sample",
        "title": "ERP Dashboard (Sample)",
        "subtitle": "Enterprise resource planning",
        "category": "Professional Sample",
        "capstone": False,
        "description": "A sample ERP dashboard from professional work. Screenshots use blurred data to protect client confidentiality. Not a capstone project.",
        "tech": ["PHP", "MySQL", "JavaScript"],
        "images": [f"{IMG}/bio-1.jpg", f"{IMG}/bio-2.jpg", f"{IMG}/bio-3.jpg"],
        "file": "p1-details.html",
    },
    {
        "slug": "iot-rvm-incentives",
        "title": "IoT-Based Incentivized Reverse Vending Machine for Plastic Bottle Detection",
        "subtitle": "Size-detecting plastic bottle recycler with thermal receipt printing",
        "category": "IoT / Embedded",
        "capstone": True,
        "description": "A microcontroller-powered reverse vending machine that uses physical sensors to detect inserted plastic bottles by size variation and prints a thermal receipt with points/incentives.",
        "tech": ["Arduino", "ESP32", "Sensors"],
        "images": [PLACEHOLDER],
        "iot": True,
    },
    {
        "slug": "iot-poultry-conveyer",
        "title": "ESP32-Controlled Poultry Waste Conveyer System with Automated Scheduling",
        "subtitle": "Smart motor control and automated waste management scheduler",
        "category": "IoT / Embedded",
        "capstone": True,
        "description": "An automated agricultural waste management system using ESP32 to run conveyer belt motors based on real-time sensor triggers and scheduled intervals.",
        "tech": ["ESP32", "Arduino", "Motor Control"],
        "images": [PLACEHOLDER],
        "iot": True,
    },
    {
        "slug": "iot-fish-pond",
        "title": "IoT Fish Pond Management System: Automated Water Level Regulation and Turbidity Monitoring",
        "subtitle": "Closed-loop pump control, water temperature, and turbidity monitoring system",
        "category": "IoT / Embedded",
        "capstone": True,
        "description": "An automated aquaculture system that monitors pond temperature, turbidity, and water level, triggering pump actuators to maintain optimal fish habitat conditions.",
        "tech": ["Arduino", "ESP32", "Sensors"],
        "images": [PLACEHOLDER],
        "iot": True,
    },
    {
        "slug": "iot-wifi-rvm",
        "title": "IoT Reverse Vending Captive Portal: Plastic Bottle & Metal Can Recycler for WiFi Access Exchange",
        "subtitle": "Recyclable coinless vending machine for Piso WiFi credits (Ongoing)",
        "category": "IoT / Embedded",
        "capstone": True,
        "ongoing": True,
        "description": "An ongoing development project combining reverse vending mechanics with captive portals, allowing users to swap recycled plastic bottles and metal cans for Piso WiFi internet access codes.",
        "tech": ["Arduino", "ESP32", "Sensors"],
        "images": [PLACEHOLDER],
        "iot": True,
    },
    {
        "slug": "enotary",
        "title": "ENotary: Web-Based Digital Notary System",
        "subtitle": "Secure online document notarization and management platform",
        "category": "Management System",
        "personal": True,
        "ongoing": True,
        "description": "An ongoing personal project designed to digitize document notarization processes, enabling secure user authentication, digital signature overlays, document upload/view dashboards, and appointment billing.",
        "tech": ["PHP", "MySQL", "JavaScript", "Bootstrap"],
        "images": [f"{IMG}/enotary_dashboard.png"],
    },
    {
        "slug": "elimary-virtual-tour",
        "title": "Elimary Virtual Tour Platform",
        "subtitle": "Interactive panoramic walkthrough system",
        "category": "Web Application",
        "capstone": True,
        "description": "An interactive web-based virtual tour system utilizing 360-degree panoramic imaging to provide users with immersive, remote walkthroughs of the campus or facilities.",
        "tech": ["JavaScript", "Three.js", "HTML", "CSS"],
        "images": [f"{IMG}/elimary_tour.png"],
    },
    {
        "slug": "ebudget",
        "title": "EBudget: Personal Budget and Expense Tracker",
        "subtitle": "Personal finance and expense monitoring application",
        "category": "Web Application",
        "personal": True,
        "ongoing": True,
        "description": "An ongoing personal finance tracking application featuring dashboard analytics, visual categorization of expenses, income logging, and monthly budget limit alerts.",
        "tech": ["React", "Node.js", "MongoDB", "CSS"],
        "images": [f"{IMG}/ebudget_dashboard.png"],
    },
    {
        "slug": "iot-rfid-printing",
        "title": "IoT Self-Service RFID Printing Vending Machine",
        "subtitle": "Self-service printing kiosk with RFID billing and WiFi file upload",
        "category": "IoT / Embedded",
        "capstone": True,
        "description": "An automated self-service printing kiosk application built with C# and integrated with microcontroller hardware. Users can upload their documents wirelessly via WiFi, authenticate using RFID cards, and pay for print jobs using internal points.",
        "tech": ["C#", "RFID", "ESP32", "Arduino"],
        "images": [f"{IMG}/rfid_printing_kiosk.png"],
        "iot": True,
    },
]

DETAIL_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{title} — Project Details</title>
  <meta content="{description}" name="description">
  <link href="assets/img/portfolio/pf.ico" rel="icon">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@600;700&display=swap" rel="stylesheet">
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <link href="assets/css/main.css" rel="stylesheet">
</head>
<body class="portfolio-details-page">
  <i class="header-toggle d-xl-none bi bi-list"></i>
  <main class="main">
    <div class="page-title dark-background">
      <div class="container d-lg-flex justify-content-between align-items-center">
        <h1 class="mb-2 mb-lg-0">{page_title}</h1>
        <nav class="breadcrumbs">
          <ol>
            <li><a href="index.html">Home</a></li>
            <li><a href="index.html#portfolio">Projects</a></li>
            <li class="current">{breadcrumb}</li>
          </ol>
        </nav>
      </div>
    </div>
    <section id="portfolio-details" class="portfolio-details section">
      <div class="container" data-aos="fade-up" data-aos-delay="100">
        <div class="row gy-4">
          <div class="col-lg-8">
            <div class="portfolio-details-media">
              <div class="portfolio-details-slider swiper init-swiper">
                <script type="application/json" class="swiper-config">
                  {{
                    "loop": true,
                    "speed": 600,
                    "autoplay": {{ "delay": 5000 }},
                    "slidesPerView": 1,
                    "pagination": {{
                      "el": ".swiper-pagination",
                      "type": "bullets",
                      "clickable": true
                    }}
                  }}
                </script>
                <div class="swiper-wrapper align-items-center">
{slides}
                </div>
                <div class="swiper-pagination"></div>
              </div>
              <div class="portfolio-sub-gallery">
                <span class="portfolio-sub-gallery-label">Gallery</span>
{thumbs}
              </div>
              <div class="sub-gallery-expand">
                <a href="{first_image}" class="glightbox" data-gallery="gallery-{slug}" title="{title}"><i class="bi bi-arrows-fullscreen"></i> Open full gallery</a>
{hidden_links}
              </div>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="portfolio-info" data-aos="fade-up" data-aos-delay="200">
              <h3>Project information</h3>
              <ul>
                <li><strong>Category</strong>: {category}</li>
                <li><strong>Type</strong>: {project_type}</li>
                <li><strong>Status</strong>: {status}</li>
                <li><strong>Stack</strong>: {stack}</li>
              </ul>
            </div>
            <div class="portfolio-description" data-aos="fade-up" data-aos-delay="300">
              <h2>{subtitle}</h2>
              <p>{description}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
  <div id="preloader"></div>
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def card_html(p):
    file = p.get("file") or f"{p['slug']}-details.html"
    thumb = p["images"][0]
    gallery_id = p["slug"].replace("-", "_")
    badges = "".join(f'<span class="badge">{t}</span>' for t in p["tech"][:4])
    capstone_badge = ""
    if p.get("capstone"):
        extra = ' <span class="portfolio-status-badge ongoing">Ongoing</span>' if p.get("ongoing") else ""
        capstone_badge = f'<span class="portfolio-capstone-badge">Capstone Project</span>{extra}'
    elif p.get("personal"):
        extra = ' <span class="portfolio-status-badge ongoing">Ongoing</span>' if p.get("ongoing") else ""
        capstone_badge = f'<span class="portfolio-capstone-badge personal">Personal Project</span>{extra}'
    else:
        capstone_badge = '<span class="portfolio-capstone-badge professional">Professional Sample</span>'

    hidden = ""
    for i, img in enumerate(p["images"][1:], 1):
        hidden += f'\n                <a href="{img}" title="{p["title"]} - View {i+1}" data-gallery="gallery-{gallery_id}" class="glightbox d-none"></a>'

    preview = ""
    if len(p["images"]) > 0 and p["images"][0] != PLACEHOLDER:
        preview = f'<a href="{p["images"][0]}" title="{p["title"]}" data-gallery="gallery-{gallery_id}" class="glightbox"><i class="bi bi-zoom-in"></i> Preview</a>'

    return f"""            <div class="col">
              <div class="portfolio-card">
                <div class="portfolio-thumb-wrap"><img src="{thumb}" class="portfolio-thumb" alt="{p['title']}"></div>
                <div class="portfolio-body">
                  {capstone_badge}
                  <h4>{p['title']}</h4>
                  <p>{p['subtitle']}</p>
                  <div class="tech-badges">{badges}</div>
                  <div class="portfolio-actions">
                    {preview}
                    <a href="{file}" title="More Details"><i class="bi bi-arrow-up-right"></i> Details</a>
                  </div>
                </div>{hidden}
              </div>
            </div>"""


def render_detail(p):
    slug = p["slug"]
    images = p["images"]
    slides = "\n".join(
        f'                  <div class="swiper-slide"><img src="{img}" alt="{p["title"]} - Screenshot {i+1}"></div>'
        for i, img in enumerate(images)
    )
    thumbs = "\n".join(
        f'                <button type="button" class="sub-gallery-thumb{" active" if i == 0 else ""}" data-slide="{i}" aria-label="View screenshot {i+1}">\n                  <img src="{img}" alt="Screenshot {i+1}">\n                </button>'
        for i, img in enumerate(images)
    )
    hidden = "\n".join(
        f'                <a href="{img}" class="glightbox d-none" data-gallery="gallery-{slug}" title="{p["title"]} - View {i+1}"></a>'
        for i, img in enumerate(images[1:], 1)
    )
    if p.get("capstone"):
        project_type = "Capstone Project"
        status = "Ongoing Development" if p.get("ongoing") else "Academic / Not Deployed"
    elif p.get("personal"):
        project_type = "Personal Project"
        status = "Ongoing Development" if p.get("ongoing") else "Personal / Side Project"
    else:
        project_type = "Professional Work Sample"
        status = "Confidential Client Work (Sample)"

    return DETAIL_TEMPLATE.format(
        title=p["title"],
        page_title=p["title"] + (" (Ongoing)" if p.get("ongoing") else ""),
        breadcrumb=p["title"][:40],
        description=p["description"],
        subtitle=p["subtitle"],
        category=p["category"],
        project_type=project_type,
        status=status,
        stack=", ".join(p["tech"]),
        slug=slug,
        slides=slides,
        thumbs=thumbs,
        hidden_links=hidden,
        first_image=images[0],
    )


def main():
    software_apps = []
    web_apps = []
    mobile_apps = []
    iot = []

    for p in PROJECTS:
        if p.get("iot"):
            iot.append(p)
        elif p["category"] == "Mobile Application":
            mobile_apps.append(p)
        elif p["category"] == "Web Application":
            web_apps.append(p)
        else:
            software_apps.append(p)

    # ERP sample goes first in software applications
    software_apps.sort(key=lambda x: (0 if x["slug"] == "erp-sample" else 1, x["title"]))
    web_apps.sort(key=lambda x: x["title"])
    mobile_apps.sort(key=lambda x: x["title"])

    sections = [
        ("Software Applications", "bi-window-stack", software_apps),
        ("Web Applications", "bi-globe", web_apps),
        ("Mobile Applications", "bi-phone", mobile_apps),
        ("Internet of Things (IoT)", "bi-cpu", iot),
    ]

    blocks = []
    delay = 100
    for name, icon, items in sections:
        if not items:
            continue
        cards = "\n\n".join(card_html(p) for p in items)
        blocks.append(f"""        <div class="portfolio-category-block" data-aos="fade-up" data-aos-delay="{delay}">
          <div class="portfolio-category-header">
            <div class="portfolio-category-icon"><i class="bi {icon}"></i></div>
            <h3>{name}</h3>
            <div class="portfolio-category-line"></div>
          </div>
          <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 portfolio-grid">
{cards}
          </div>
        </div>""")
        delay += 50

    portfolio_inner = "\n\n".join(blocks)

    index = (ROOT / "index.html").read_text(encoding="utf-8")
    start = index.find("      <div class=\"container\">\n\n        <!-- Web Applications -->")
    end = index.find("        <div class=\"portfolio-more-note\"")
    if start == -1:
        start = index.find("      <div class=\"container\">", index.find("id=\"portfolio\""))
        end = index.find("        <div class=\"portfolio-more-note\"")

    new_section = f"""      <div class="container">

{portfolio_inner}

"""
    index = index[:start] + new_section + index[end:]

    # Update section title
    index = index.replace(
        "<p>A showcase of business solutions and educational projects — ERP systems, retail management, mobile apps, and more.</p>",
        "<p>Capstone projects and academic work from ISAT U and related programs. These systems were developed for learning and demonstration — not published or deployed to production.</p>",
    )
    index = index.replace(
        "<h2>Selected work</h2>",
        "<h2>Capstone &amp; academic projects</h2>",
    )
    index = index.replace(
        "&amp; More <span style=\"font-weight:400;color:var(--default-color);\">(ongoing update)</span>",
        "Gallery images are placeholders for some projects — screenshots will be updated as they become available.",
    )
    (ROOT / "index.html").write_text(index, encoding="utf-8")

    for p in PROJECTS:
        fname = p.get("file") or f"{p['slug']}-details.html"
        (ROOT / fname).write_text(render_detail(p), encoding="utf-8")
        print(f"Wrote {fname}")

    print("Updated index.html portfolio section")


if __name__ == "__main__":
    main()
