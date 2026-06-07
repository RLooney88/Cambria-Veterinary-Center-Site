export const siteConfig = {
  practice: {
    name: "Cambria Veterinary Center",
    shortName: "Cambria Vet",
    displayLines: ["Cambria", "Veterinary Center"],
    tagline: "Full-service veterinary medical care in Whiteford, Maryland.",
    description: "Cambria Veterinary Center is a full-service veterinary medical facility in Whiteford, MD, providing medical, surgical, dental, wellness, diagnostic, and preventive care for pets in Whiteford and surrounding communities.",
    serviceArea: "Whiteford, MD and surrounding areas",
  },
  brand: {
    logo: "/brand/cambria-logo.svg",
    logoAlt: "Cambria Veterinary Center text logo",
    colors: {
      light: "#F7F3EA",
      dark: "#5E101D",
      accent: "#A90A30",
      accentLight: "#EEF1D5",
    },
  },
  contact: {
    phone: "(410) 399-0344",
    phoneHref: "tel:+14103990344",
    email: "",
    emailStatus: "Public email intentionally not shown in demo; use phone or source contact form guidance.",
    address: {
      street: "2756 Whiteford Road",
      line2: "",
      city: "Whiteford",
      state: "MD",
      zip: "21160",
      country: "US",
    },
  },
  hours: [
    ["Monday", "9:00 AM - 6:00 PM"],
    ["Tuesday", "9:00 AM - 5:00 PM"],
    ["Wednesday", "Closed"],
    ["Thursday", "9:00 AM - 6:00 PM"],
    ["Friday", "9:00 AM - 5:00 PM"],
    ["Saturday", "8:00 AM - 12:00 PM"],
    ["Sunday", "Closed"],
  ],
  links: {
    website: "http://cambriavet.vetstreet.com/",
    appointment: "/appointment",
    store: "",
    pharmacy: "",
    onlineForms: "http://cambriavet.vetstreet.com/contact_us.html",
    facebook: "",
    instagram: "",
    linkedin: "",
    googleBusinessProfile: "",
  },
  team: [
    {
      name: "Amy Hartman, VMD",
      role: "Practice Owner",
      bio: "Dr. Amy Hartman is listed publicly as Practice Owner on Cambria Veterinary Center's staff page. Full biography and headshot were not available from the source site.",
      image: "",
    },
  ],
  features: {
    clientPortal: true,
    onlineBooking: true,
    storeLink: false,
    pharmacyLink: false,
    onlineFormsLink: true,
    teamSection: true,
  },
};

export const practice = siteConfig.practice;
export const brand = siteConfig.brand;
export const contact = siteConfig.contact;
export const hours = siteConfig.hours;
export const links = siteConfig.links;
export const team = siteConfig.team;
export const features = siteConfig.features;

export function formatAddress(address = contact.address, { multiline = false } = {}) {
  const line1 = address?.street || "";
  const locality = [address?.city, address?.state, address?.zip].filter(Boolean).join(", ").replace(/, (\d{5})$/, " $1");
  if (multiline) return [line1, locality].filter(Boolean);
  return [line1, locality].filter(Boolean).join(", ");
}

export function getExternalLinks() {
  const items = [];
  if (features.storeLink && links.store) items.push({ href: links.store, label: "Online Store" });
  if (features.pharmacyLink && links.pharmacy) items.push({ href: links.pharmacy, label: "Pharmacy" });
  if (features.onlineFormsLink && links.onlineForms) items.push({ href: links.onlineForms, label: "Forms" });
  return items;
}

export default siteConfig;
