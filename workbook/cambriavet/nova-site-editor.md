# Nova Site Editor Plan

## Demo status
Nova Site Editor remains demo-disabled until production secrets and callback URLs are intentionally configured.

## Suggested identifiers
- Site ID: `cambriavet-vetstreet-com`
- Public site URL: TBD after Railway/Vercel/RCLintegrated preview is assigned.

## Required environment variables when enabled
- `EDIT_REQUEST_ENABLED=true`
- `EDIT_REQUEST_SITE_ID=cambriavet-vetstreet-com`
- `EDIT_REQUEST_SITE_KEY=<generated shared secret>`
- `EDIT_REQUEST_CALLBACK_AUTH=<generated callback secret>`
- `PUBLIC_SITE_URL=<preview-or-production-url>`

## Content editing boundaries
- Safe editable copy: homepage, services summaries, about text, team bio text, CTAs, FAQ answers.
- Review-required fields: hours, phone, address, booking configuration, schema, and medical claims.
- Do-not-invent rules: staff members, email address, pricing, emergency coverage, species treated beyond dogs/cats/ferrets unless clinic confirms.
