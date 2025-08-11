// import { getPermalink, getBlogPermalink, getAsset } from './utils/permalinks';

export const headerData = {
  links: [
    {
      text: '主页', //Home
      href: '/',
    },
    {
      text: '产品', //Products
      links: [
        {
          text: 'ADORA2 Max',
          href: '/product-adora2-max',
        },
        {
          text: 'ADORA2 Pro',
          href: '/product-adora2-pro',
        },
        {
          text: 'ADORA2 Mini',
          href: '/product-adora2-mini',
        },
        {
          text: 'ADORA1 Pro',
          href: '/product-adora1-pro',
        },
        {
          text: 'ADORA1 Mini',
          href: '/product-adora1-mini',
        },
              ],
    },
    {
      text: '行业方案', //Solutions
      href: '/industry-solutions',
    },
    {
      text: '新闻中心', //Blog
      href: '/blog',
    },
    {
      text: 'DORA开源社区', //DORA Open Source Community
      href: 'http://www.dora-rs.ai',
    },
    {
      text: '服务与支持', //Services & Support
      href: '/404',
    },
    {
      text: '关于我们', //About Us
      href: '/about',
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
      title: '产品',
      links: [
        {
          text: 'ADORA2 Max',
          href: '/product-adora2-max',
        },
        {
          text: 'ADORA2 Pro',
          href: '/product-adora2-pro',
        },
        {
          text: 'ADORA2 Mini',
          href: '/product-adora2-mini',
        },
        {
          text: 'ADORA1 Pro',
          href: '/product-adora1-pro',
        },
        {
          text: 'ADORA1 Mini',
          href: '/product-adora1-mini',
        },
      ],
    },
    {
      title: 'DORA开源社区',
      links: [
        {
          text: 'DORA开源社区', //DORA Open Source Community
          href: 'http://www.dora-rs.ai',
      },
      ],
    },
    {
      title: '关于我们',
      links: [
        {
          text: '公司简介',
          href: '/',
        },
        {
          text: '新闻中心',
          href: '/blog',
        },
        {
          text: '联系我们',
          href: '/about',
        },
      ],
    },
    {
      title: '购买与合作',
      links: [
        {
          text: '购买咨询',
          href: '/',
        },
        {
          text: '合作洽谈',
          href: '/',
        },
      ],
    },
    {
      title: '服务与支持',
      links: [
        {
          text: '客户服务',
          href: '/',
        },
        {
          text: '帮助中心',
          href: '/',
        },
        {
          text: '资源与下载中心',
          href: '/',
        },
        {
          text: '服务条款与政策',
          href: '/',
        },
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
    2025 <a class="text-blue-500 underline dark:text-muted" href="https://www.kippal.ai/">KIPPAL Robotics</a>  版权所有
  `,
};
