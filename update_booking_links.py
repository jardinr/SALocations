import os

files_to_update = [
    r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-british-homes-web\index.html",
    r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html"
]

gcal_url = (
    "https://calendar.google.com/calendar/render?action=TEMPLATE"
    "&text=Location+Scouting+%26+Recce+-+British+Residential+Homes"
    "&details=Location+Scouting+%26+Technical+Recce+with+Jardin+Roestorff+%28SA+Locations%29.%0A%0A"
    "Curated+Properties%3A%0A"
    "%E2%80%A2+Storybook+House+%28Newlands+%2F+Fernwood%29%0A"
    "%E2%80%A2+Invergara+Estate+%28Bishopscourt+%2F+Constantia%29%0A"
    "%E2%80%A2+Orchard+House+%28Constantia+Upper%29%0A"
    "%E2%80%A2+Silwood+Manor+%28Rondebosch+Heritage+Belt%29%0A"
    "%E2%80%A2+Cloudbreak+%28Bishopscourt%29%0A"
    "%E2%80%A2+Marlbrook+%28Bishopscourt+%2F+Newlands%29%0A%0A"
    "Package%3A+ZAR+6%2C000+%2F+day+%28~%C2%A3266%2Fday+incl.+Scout+%2B+4x4+Vehicle+%2B+Fuel+%2B+High-Res+Photography+Package%29%0A"
    "Web+Dossier%3A+https%3A%2F%2Fsal-british-homes.vercel.app%0A"
    "Direct+Liaison%3A+Jardin+Roestorff+%28jardinr%40gmail.com+%2F+jardin%40salocations.com%29"
    "&location=Cape+Town%2C+South+Africa"
    "&add=jardinr%40gmail.com"
)

js_helper = """        function getGoogleCalendarScoutUrl(propertyName = '') {
            const title = propertyName 
                ? `Location Recce: ${propertyName} (Cape Town)`
                : 'Location Scouting & Recce - British Residential Homes';

            let desc = `Location Scouting & Technical Recce booking with Jardin Roestorff (SA Locations).\\n\\n`;
            if (propertyName) {
                desc += `Target Location: ${propertyName}\\n`;
            }
            desc += `Campaign: British / English Residential Homes & Gardens (Cape Town)\\n`;
            desc += `Daily Scouting Package: ZAR 6,000 / day (~£266/day incl. Scout + 4x4 Vehicle + Fuel + High-Res Photography Package)\\n\\n`;
            desc += `Web Dossier: https://sal-british-homes.vercel.app\\n`;
            desc += `Direct Liaison: Jardin Roestorff\\n`;
            desc += `Email: jardin@salocations.com / jardinr@gmail.com\\n\\n`;
            desc += `Please select your preferred date/time slot on your Google Calendar and click Save to confirm and invite Jardin.`;

            const loc = propertyName ? `${propertyName}, Cape Town, South Africa` : 'Cape Town, South Africa';
            const params = new URLSearchParams({
                action: 'TEMPLATE',
                text: title,
                details: desc,
                location: loc,
                add: 'jardinr@gmail.com'
            });
            return `https://calendar.google.com/calendar/render?${params.toString()}`;
        }

        let currentLocId = locations[0].id;"""

for path in files_to_update:
    if not os.path.exists(path):
        print("File does not exist:", path)
        continue

    print(f"\nProcessing {os.path.basename(path)}...")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Top nav action button
    target_nav = '<a href="mailto:jardin@salocations.com?subject=Hold%20Inquiry%20-%20British%20Homes%20Pitch%20March%202027" class="btn-nav primary">✉️ Request Hold</a>'
    nav_replacement = f'<a href="{gcal_url}" target="_blank" rel="noopener noreferrer" class="btn-nav" style="border-color: var(--gold); color: var(--gold-bright); font-weight: 600;">📅 Book Scouting (Cal)</a>\n            {target_nav}'
    if target_nav in content and '📅 Book Scouting (Cal)' not in content:
        content = content.replace(target_nav, nav_replacement, 1)
        print(" -> Added Google Calendar button to top nav")

    # 2. Rate Card booking button
    target_rc = '<a href="mailto:jardin@salocations.com?subject=Book%20Location%20Scouting%20Days%20-%20March%202027" class="btn-nav primary" style="padding: 0.45rem 1rem; font-size: 0.8rem; text-decoration: none;">Book Scouting Days</a>'
    rc_replacement = f"""<div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
                    <a href="{gcal_url}" target="_blank" rel="noopener noreferrer" class="btn-nav primary" style="padding: 0.5rem 1.15rem; font-size: 0.82rem; text-decoration: none; display: inline-flex; align-items: center; gap: 0.4rem; background: var(--gold); color: #0b0f0e; font-weight: 700;">
                        📅 Book Scouting via Google Calendar
                    </a>
                    <a href="mailto:jardin@salocations.com?subject=Book%20Location%20Scouting%20Days%20-%20March%202027" class="btn-nav" style="padding: 0.5rem 0.9rem; font-size: 0.8rem; text-decoration: none;">
                        ✉️ Email Inquiry
                    </a>
                </div>"""
    if target_rc in content:
        content = content.replace(target_rc, rc_replacement, 1)
        print(" -> Replaced Rate Card booking button with Google Calendar link")

    # 3. Footer CTA button
    target_cta = """<a href="mailto:jardin@salocations.com?subject=Technical%20Recce%20Request%20-%20British%20Homes%20Brief" class="cta-btn gold">
                    Schedule Technical Recce
                </a>"""
    cta_replacement = f"""<a href="{gcal_url}" target="_blank" rel="noopener noreferrer" class="cta-btn gold" style="display: inline-flex; align-items: center; gap: 0.5rem;">
                    📅 Schedule Recce on Google Calendar
                </a>"""
    if target_cta in content:
        content = content.replace(target_cta, cta_replacement, 1)
        print(" -> Replaced Footer CTA button with Google Calendar link")

    # 4. Add JavaScript helper function
    target_js = "let currentLocId = locations[0].id;"
    if target_js in content and "function getGoogleCalendarScoutUrl" not in content:
        content = content.replace(target_js, js_helper, 1)
        print(" -> Added getGoogleCalendarScoutUrl helper function to JS")

    # 5. Add property card recce button
    target_prop_old = """                            <div style="margin-top: 1.25rem; display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
                                <a href="mailto:jardin@salocations.com?subject=Film%20Enquiry%20-%20${encodeURIComponent(loc.name)}%20(March%202027)&body=Hi%20Jardin,%0D%0A%0D%0AWe%20would%20like%20to%20enquire%20about%20availability%20and%20rates%20for%20filming%20at%20${encodeURIComponent(loc.name)}%20for%20our%20March%202027%20shoot.%0D%0A%0D%0AProduction%20Company:%20%0D%0AProject:%20%0D%0ATarget%20Dates:%20" class="btn-nav primary" style="text-decoration: none; padding: 0.65rem 1.25rem;">
                                    📩 Enquire on ${loc.name}
                                </a>
                                <span style="font-size: 0.82rem; color: var(--text-muted);">Direct Film Enquiries: <strong style="color: var(--gold);">jardin@salocations.com</strong></span>
                            </div>"""

    target_prop_new = """                            <div style="margin-top: 1.25rem; display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
                                <a href="mailto:jardin@salocations.com?subject=Film%20Enquiry%20-%20${encodeURIComponent(loc.name)}%20(March%202027)&body=Hi%20Jardin,%0D%0A%0D%0AWe%20would%20like%20to%20enquire%20about%20availability%20and%20rates%20for%20filming%20at%20${encodeURIComponent(loc.name)}%20for%20our%20March%202027%20shoot.%0D%0A%0D%0AProduction%20Company:%20%0D%0AProject:%20%0D%0ATarget%20Dates:%20" class="btn-nav" style="text-decoration: none; padding: 0.65rem 1.15rem;">
                                    📩 Enquire on ${loc.name}
                                </a>
                                <a href="${getGoogleCalendarScoutUrl(loc.name)}" target="_blank" rel="noopener noreferrer" class="btn-nav primary" style="text-decoration: none; padding: 0.65rem 1.25rem; display: inline-flex; align-items: center; gap: 0.45rem; background: var(--gold); color: #0b0f0e; font-weight: 700;">
                                    📅 Book Recce (Google Cal)
                                </a>
                                <span style="font-size: 0.82rem; color: var(--text-muted);">Direct Film Enquiries: <strong style="color: var(--gold);">jardin@salocations.com</strong></span>
                            </div>"""
    if target_prop_old in content:
        content = content.replace(target_prop_old, target_prop_new, 1)
        print(" -> Added property card Google Calendar button")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Finished updating {os.path.basename(path)}")
