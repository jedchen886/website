// import { getPermalink, getBlogPermalink, getAsset } from './utils/permalinks';

export const headerData = {
  links: [
    {
      text: 'Products',
      links: [
        {
          text: 'ADORA 1',
          href: '/#adora1-mini',
        },
        {
          text: 'ADORA 2',
          href: '/#adora2-mini',
        },
      ],
    },
    {
      text: 'Solutions',
      links: [
        {
          text: 'Research & Education',
          href: '/',
        },
        {
          text: 'Home',
          href: '/',
        },
        {
          text: 'Business',
          href: '/',
        },
      ],
    },
    {
      text: 'Blog',
      href: '/blog',
    },
    {
      text: 'Open-Source',
      href: '/',

    },
    {
      text: 'About',
      links: [
        {
          text: 'Company',
          href: '/',
        },
        {
          text: 'Contact',
          href: "/",
        },

      ],
    },
  ],
  actions: [{ text: 'Order Now', href: 'https://www.kippal.ai/', target: '_blank' }],
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
      title: 'KIPPAL Robotics',
      links: [
        { text: 'Home', href: '/' },
        { text: 'Blog', href: '/blog' },
        { text: 'About', href: '/' },
      ],
    },
  ],
/*   secondaryLinks: [
    { text: 'Terms', href: getPermalink('/terms') },
    { text: 'Privacy Policy', href: getPermalink('/privacy') },
    { text: 'Code of Conduct', href: getPermalink('/code-of-conduct') },
  ], */
/*   socialLinks: [
    { ariaLabel: 'GitHub', icon: 'tabler:brand-github', href: 'https://github.com/gosimfoundation' },
    { ariaLabel: 'LinkedIn', icon: 'tabler:brand-linkedin', href: 'https://www.linkedin.com/company/gosim-foundation' },
    { ariaLabel: 'Mastodon', icon: 'tabler:brand-mastodon', href: 'https://mastodon.social/@gosim' },
    { ariaLabel: 'BlueSky', icon: 'tabler:brand-bluesky', href: 'https://bsky.app/profile/gosimfoundation.bsky.social' },
    { ariaLabel: 'X', icon: 'tabler:brand-x', href: 'https://x.com/gosimfoundation' },
    { ariaLabel: 'YouTube', icon: 'tabler:brand-youtube', href: 'https://www.youtube.com/@GOSIMFoundation' },
    // { ariaLabel: 'RSS', icon: 'tabler:rss', href: getAsset('/rss.xml') },
  ], */
  footNote: `
    <img class="w-5 h-5 md:w-6 md:h-6 md:-mt-0.5 bg-cover mr-1.5 rtl:mr-0 rtl:ml-1.5 float-left rtl:float-right rounded-sm" src="/images/favicon.svg" alt="kippal logo" loading="lazy"></img>
    Made by <a class="text-blue-600 underline dark:text-muted" href="https://www.kippal.ai/">KIPPAL Robotics</a> · All rights reserved.
  `,
};
