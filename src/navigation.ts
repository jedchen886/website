// import { getPermalink, getBlogPermalink, getAsset } from './utils/permalinks';

export const headerData = {
  links: [
    {
      text: '产品', //Products
      links: [
        {
          text: 'ADORA1 pro',
          href: '/#adora1-pro',
        },
        {
          text: 'ADORA1 mini',
          href: '/#adora1-mini',
        },
        {
          text: 'ADORA2 Pro',
          href: '/#adora2-pro',
        },
        {
          text: 'ADORA2 Mini',
          href: '/#adora2-mini',
        },
      ],
    },
    {
      text: '行业方案', //Solutions
      links: [
        {
          text: '研究与教育', //Research & Education
          href: '/',
        },
        {
          text: '家庭', 
          href: '/',
        },
        {
          text: '商业', //Commercial
          href: '/',
        },
      ],
    },
    {
      text: '新闻中心', //Blog
      href: '/blog',
    },
    {
      text: 'DORA开源社区', //DORA Open Source Community
      href: '/',

    },
    {
      text: '服务与支持', //Services & Support
      href: '/',

    },
    {
      text: '关于我们', //About Us
      links: [
        // {
        //   text: 'Company',
        //   href: '/',
        // },
        {
          text: 'Contact',
          href: "/about",
        },

      ],
    },
  ],
  actions: [{ text: '购买与合作', href: '/#order' }],
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
