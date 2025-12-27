// import { getPermalink, getBlogPermalink, getAsset } from './utils/permalinks';

// Chinese navigation
export const headerDataCN = {
  links: [
    {
      text: '主页',
      href: '/cn',
    },
    {
      text: '产品',
      links: [
        { text: 'ADORA 1 Pro', href: '/cn/product-adora1-pro' },
        { text: 'ADORA 1 Mini', href: '/cn/product-adora1-mini' },
        { text: 'ADORA 1 Nano', href: '/cn/product-adora1-nano' },
        { text: 'ADORA 2 Max', href: '/cn/product-adora2-max' },
        { text: 'ADORA 2 Pro', href: '/cn/product-adora2-pro' },
        { text: 'ADORA 2 Mini', href: '/cn/product-adora2-mini' },
      ],
    },
    { text: '行业方案', href: '/cn/solutions' },
    { text: '新闻中心', href: '/cn/blog' },
    {
      text: '服务与支持',
      links: [
        { text: '帮助中心', href: '/cn/support#faq' },
        { text: '服务条款与政策', href: '/cn/support#policy' },
        { text: '客户服务', href: '/cn/support#contact' },
      ],
    },
    { text: '关于我们', href: '/cn/about' },
    { text: 'DORA开源社区', href: 'http://www.dora-rs.ai' },
  ],
  actions: [{ text: '购买与合作', href: '/cn/support#contact' }],
};

// English navigation
export const headerDataEN = {
  links: [
    {
      text: 'Home',
      href: '/en',
    },
    {
      text: 'Products',
      links: [
        { text: 'ADORA 1 Pro', href: '/en/product-adora1-pro' },
        { text: 'ADORA 1 Mini', href: '/en/product-adora1-mini' },
        { text: 'ADORA 1 Nano', href: '/en/product-adora1-nano' },
        { text: 'ADORA 2 Max', href: '/en/product-adora2-max' },
        { text: 'ADORA 2 Pro', href: '/en/product-adora2-pro' },
        { text: 'ADORA 2 Mini', href: '/en/product-adora2-mini' },
      ],
    },
    { text: 'Solutions', href: '/en/solutions' },
    { text: 'News', href: '/en/blog' },
    {
      text: 'Support',
      links: [
        { text: 'Help Center', href: '/en/support#faq' },
        { text: 'Terms & Policies', href: '/en/support#policy' },
        { text: 'Customer Service', href: '/en/support#contact' },
      ],
    },
    { text: 'About Us', href: '/en/about' },
    { text: 'DORA Community', href: 'http://www.dora-rs.ai' },
  ],
  actions: [{ text: 'Purchase & Partner', href: '/en/support#contact' }],
};

// Default export (Chinese)
export const headerData = headerDataCN;

// Chinese footer
export const footerDataCN = {
  links: [
    {
      title: '产品',
      links: [
        { text: 'ADORA 1 Pro', href: '/cn/product-adora1-pro' },
        { text: 'ADORA 1 Mini', href: '/cn/product-adora1-mini' },
        { text: 'ADORA 1 Nano', href: '/cn/product-adora1-nano' },
        { text: 'ADORA 2 Max', href: '/cn/product-adora2-max' },
        { text: 'ADORA 2 Pro', href: '/cn/product-adora2-pro' },
        { text: 'ADORA 2 Mini', href: '/cn/product-adora2-mini' },
      ],
    },
    {
      title: 'DORA开源社区',
      links: [{ text: 'DORA开源社区', href: 'http://www.dora-rs.ai' }],
    },
    {
      title: '关于我们',
      links: [
        { text: '公司简介', href: '/cn/about' },
        { text: '新闻中心', href: '/cn/blog' },
        { text: '联系我们', href: '/cn/support#contact' },
      ],
    },
    {
      title: '购买与合作',
      links: [
        { text: '购买咨询', href: '/cn/support#contact' },
        { text: '合作洽谈', href: '/cn/support#contact' },
      ],
    },
    {
      title: '服务与支持',
      links: [
        { text: '帮助中心', href: '/cn/support#faq' },
        { text: '服务条款与政策', href: '/cn/support#policy' },
        { text: '客户服务', href: '/cn/support#contact' },
      ],
    },
  ],
  footNote: `
    <img class="w-5 h-5 md:w-6 md:h-6 md:-mt-0.5 bg-cover mr-1.5 rtl:mr-0 rtl:ml-1.5 float-left rtl:float-right rounded-sm" src="/images/favicon.svg" alt="DORA logo" loading="lazy"></img>
    2025 <a class="text-blue-500 underline dark:text-muted" href="https://www.dorarobotics.com/">DORA Robotics</a>  版权所有， 网站图片和内容仅供参考。
  `,
};

// English footer
export const footerDataEN = {
  links: [
    {
      title: 'Products',
      links: [
        { text: 'ADORA 1 Pro', href: '/en/product-adora1-pro' },
        { text: 'ADORA 1 Mini', href: '/en/product-adora1-mini' },
        { text: 'ADORA 1 Nano', href: '/en/product-adora1-nano' },
        { text: 'ADORA 2 Max', href: '/en/product-adora2-max' },
        { text: 'ADORA 2 Pro', href: '/en/product-adora2-pro' },
        { text: 'ADORA 2 Mini', href: '/en/product-adora2-mini' },
      ],
    },
    {
      title: 'DORA Community',
      links: [{ text: 'DORA Open Source', href: 'http://www.dora-rs.ai' }],
    },
    {
      title: 'About Us',
      links: [
        { text: 'Company Profile', href: '/en/about' },
        { text: 'News Center', href: '/en/blog' },
        { text: 'Contact Us', href: '/en/support#contact' },
      ],
    },
    {
      title: 'Purchase & Partner',
      links: [
        { text: 'Purchase Inquiry', href: '/en/support#contact' },
        { text: 'Partnership', href: '/en/support#contact' },
      ],
    },
    {
      title: 'Support',
      links: [
        { text: 'Help Center', href: '/en/support#faq' },
        { text: 'Terms & Policies', href: '/en/support#policy' },
        { text: 'Customer Service', href: '/en/support#contact' },
      ],
    },
  ],
  footNote: `
    <img class="w-5 h-5 md:w-6 md:h-6 md:-mt-0.5 bg-cover mr-1.5 rtl:mr-0 rtl:ml-1.5 float-left rtl:float-right rounded-sm" src="/images/favicon.svg" alt="DORA logo" loading="lazy"></img>
    2025 <a class="text-blue-500 underline dark:text-muted" href="https://www.dorarobotics.com/">DORA Robotics</a>  All rights reserved. Website images and content are for reference only.
  `,
};

// Default export (Chinese)
export const footerData = footerDataCN;
