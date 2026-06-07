# Implementation Plan

## Completed in demo repo
1. Copied and improved the Cambria practice profile in `workbook/cambriavet/`.
2. Updated global site config in `site.config.json`, `frontend/src/site/site.config.json`, and `frontend/src/site/siteConfig.js`.
3. Replaced generic template contact data with Cambria address, phone, source URL, and hours.
4. Added a Cambria brand fallback logo, mark, and generated local icons.
5. Re-themed Tailwind/CSS tokens to the burgundy, olive, and warm neutral source palette.
6. Added idempotent booking seeding with Cambria hours and appointment types.
7. Updated chatbot defaults to use LiteLLM/OpenAI-style `OPENAI_API_KEY` lookup and Cambria-specific knowledge.
8. Avoided invented staff: only Amy Hartman, VMD, Practice Owner is listed from the public staff page.

## Contact propagation plan
- Phone appears in config, CTAs, appointment fallback text, chatbot, schema/meta, footer, and contact section.
- Public email is intentionally not shown in demo. Use phone and contact-form language until clinic confirms what email should be public.

## Chatbot KB plan
- KB should include address, phone, hours, services, species confirmed by source, owner listing, and strict guardrails.
- For unconfirmed species/policies/pricing, bot should recommend calling (410) 399-0344.

## Booking availability plan
- Seed types: Wellness Exam, Sick Pet Visit, Dental Consultation, Surgery Consultation, Tech Appointment.
- Seed hours: Mon/Tue/Thu/Fri/Sat open, Wed/Sun closed.
- Bookings are requests and should state phone confirmation is required.

## Remaining production steps
- Ask clinic for logo, photos, staff list/bios, preferred public email, and final booking policy.
- Configure deployment URL and optional Nova Site Editor secrets.
- QA browser pages and booking slots after deployment.
