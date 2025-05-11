// import { getPermalink, getBlogPermalink, getAsset } from './utils/permalinks';

import { getPermalink } from './utils/permalinks';


export const headerData = {
  links: [
    {
      text: 'Schedules',
      href: "/schedules",
    },
    {
      text: 'Speakers',
      href: "/#speakers",
    },
/*     {
      text: 'Sponsors',
      href: "/sponsors",
    }, */
    {
      text: 'Co-Located Events',
      links: [
        {
          text: 'PyTorch AI Paris Day',
          href: '/',
        },
        {
          text: 'Open-Source AI Strategy Forum',
          href: '/os-ai-strategy-forum',
        },
        {
          text: 'GOSIM AI Spotlight',
          href: 'https://spotlight.gosim.org/ai2025',
        },
      ],
    },
    {
      text: 'About',
      links: [
        {
          text: 'Why Attend',
          href: '/#why-attend',
        },
                {
          text: 'Tracks',
          href: "/#tracks",
        },
        {
          text: 'Venue - Station F',
          href: "https://stationf.co/",
        },
        {
          text: 'Be a Volunteer',
          href: 'https://docs.google.com/forms/d/e/1FAIpQLSc62kJczw7lr-l0JAAbkabeIrrPPAD7OWyzwDopTD0L4HC6EQ/viewform',
        },
        {
          text: 'Volunteers List',
          href: '/volunteers',
        },
      ],
    },
  ],
  actions: [{ text: 'Early Bird Tickets', href: 'https://gosimaiparis.eventbrite.com/', target: '_blank' }],
};

export const footerData = {
  links: [
    // {
    //   title: 'Product',
    //   links: [
    //     { text: 'Features', href: '#' },
    //     { text: 'Team', href: '#' },
    //     { text: 'Enterprise', href: '#' },
    //     { text: 'Resources', href: '#' },
    //   ],
    // },

    {
      title: 'GOSIM',
      links: [
        { text: 'Home', href: 'https://gosim.org' },
        { text: 'Blog', href: 'https://blog.gosim.org' },
        { text: 'Spotlight', href: 'https://spotlight.gosim.org' },
        { text: 'Call for Proposal', href: 'https://cfp.gosim.org' },
      ],
    },
  ],
  secondaryLinks: [
    { text: 'Terms', href: getPermalink('/terms') },
    { text: 'Privacy Policy', href: getPermalink('/privacy') },
    { text: 'Code of Conduct', href: getPermalink('/code-of-conduct') },
  ],
  socialLinks: [
    { ariaLabel: 'GitHub', icon: 'tabler:brand-github', href: 'https://github.com/gosimfoundation' },
    { ariaLabel: 'LinkedIn', icon: 'tabler:brand-linkedin', href: 'https://www.linkedin.com/company/gosim-foundation' },
    { ariaLabel: 'Mastodon', icon: 'tabler:brand-mastodon', href: 'https://mastodon.social/@gosim' },
    { ariaLabel: 'BlueSky', icon: 'tabler:brand-bluesky', href: 'https://bsky.app/profile/gosimfoundation.bsky.social' },
    { ariaLabel: 'X', icon: 'tabler:brand-x', href: 'https://x.com/gosimfoundation' },
    { ariaLabel: 'YouTube', icon: 'tabler:brand-youtube', href: 'https://www.youtube.com/@GOSIMFoundation' },
    // { ariaLabel: 'RSS', icon: 'tabler:rss', href: getAsset('/rss.xml') },
  ],
  footNote: `
    <img class="w-5 h-5 md:w-6 md:h-6 md:-mt-0.5 bg-cover mr-1.5 rtl:mr-0 rtl:ml-1.5 float-left rtl:float-right rounded-sm" src="/images/favicon.svg" alt="gosim logo" loading="lazy"></img>
    Made by <a class="text-blue-600 underline dark:text-muted" href="https://www.gosim.org/"> GOSIM Foundation</a> · All rights reserved.
  `,
};
