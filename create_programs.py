import re

with open('programs.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# split at header end
header_part = orig.split('</header>')[0] + '</header>\n'
# split at footer start
footer_part = '\n    <!-- Footer -->' + orig.split('<!-- Footer -->')[1]

main_content = """
    <section class="page-header">
        <div class="page-header-bg"></div>
        <div class="container fade-in-up">
            <h1>Programs & Initiatives</h1>
            <p>Empowering youth through hands-on robotics, technical research, and impactful community events.</p>
        </div>
    </section>

    <!-- Past Events & Achievements -->
    <section class="section-padding bg-light">
        <div class="container">
            <div class="section-title reveal">
                <h2>Past Events & Achievements</h2>
                <div class="divider"></div>
            </div>
            <div class="programs-grid reveal">
                <article class="program-card">
                    <div class="program-img">
                        <img src="assets/world robotics competion.png" alt="Technoxian Championship" loading="lazy" decoding="async">
                    </div>
                    <div class="program-content">
                        <h3>Technoxian World Robotics Championship</h3>
                        <p>In August 2024, RoboYuwa proudly represented Nepal on the international stage at the Technoxian World Robotics Championship.</p>
                    </div>
                </article>
                <article class="program-card">
                    <div class="program-img">
                        <img src="assets/competetion.png" alt="Aavishkar Competition" loading="lazy" decoding="async">
                    </div>
                    <div class="program-content">
                        <h3>Aavishkar Competition</h3>
                        <p>Secured second prize in May 2025, demonstrating strong technical abilities and creative problem-solving from our team.</p>
                    </div>
                </article>
                <article class="program-card">
                    <div class="program-img">
                        <img src="assets/workshop (2).png" alt="School Workshops" loading="lazy" decoding="async">
                    </div>
                    <div class="program-content">
                        <h3>Robotics Bootcamps</h3>
                        <p>Organized over 40 structured workshops and bootcamps, expanding to 3 new districts and empowering over 1,200 youth by November 2024.</p>
                    </div>
                </article>
            </div>
        </div>
    </section>

    <!-- Upcoming Agendas & Initiatives -->
    <section class="section-padding">
        <div class="container">
            <div class="section-title reveal">
                <h2>Upcoming Agendas & Core Initiatives</h2>
                <div class="divider"></div>
            </div>
            <div class="programs-grid reveal">
                <article class="program-card">
                    <div class="program-img">
                        <img src="assets/hackathon radar 2026.jpeg" alt="RADAR26" loading="lazy" decoding="async">
                    </div>
                    <div class="program-content">
                        <h3>RADAR26</h3>
                        <p>Our premier annual planning and event milestone scheduled for January 2026. Setting the stage for the next year of youth innovation.</p>
                    </div>
                </article>
                <article class="program-card">
                    <div class="program-img">
                        <img src="assets/workshop.png" alt="RoboLearn Initiative" loading="lazy" decoding="async">
                    </div>
                    <div class="program-content">
                        <h3>RoboLearn Initiative</h3>
                        <p>A structured 12-week robotics curriculum designed for underserved schools, bringing vital tech education to those who need it most.</p>
                    </div>
                </article>
                <article class="program-card">
                    <div class="program-img">
                        <img src="assets/homepage.jpg" alt="InnovatYouth Summit" loading="lazy" decoding="async">
                    </div>
                    <div class="program-content">
                        <h3>InnovatYouth Summit</h3>
                        <p>An annual youth solution showcase empowering young creators to present projects assessed by industry experts.</p>
                    </div>
                </article>
                <article class="program-card">
                    <div class="program-img">
                        <img src="assets/socoor bot.jpeg" alt="Tech4Community" loading="lazy" decoding="async">
                    </div>
                    <div class="program-content">
                        <h3>Tech4Community</h3>
                        <p>Enabling youth to design low-cost technical solutions tailored to address the immediate needs of local organizations and communities.</p>
                    </div>
                </article>
            </div>
        </div>
    </section>
"""

with open('programs.html', 'w', encoding='utf-8') as f:
    f.write(header_part + main_content + footer_part)
print("programs.html generated")
