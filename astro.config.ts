import path from 'path';
import { fileURLToPath } from 'url';

import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import partytown from '@astrojs/partytown';
import icon from 'astro-icon';
import compress from 'astro-compress';
import type { AstroIntegration } from 'astro';

import astrowind from './vendor/integration';

import { readingTimeRemarkPlugin, responsiveTablesRehypePlugin, lazyImagesRehypePlugin } from './src/utils/frontmatter';

import react from '@astrojs/react';

import expressiveCode from 'astro-expressive-code';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const hasExternalScripts = false;
const whenExternalScripts = (items: (() => AstroIntegration) | (() => AstroIntegration)[] = []) =>
  hasExternalScripts ? (Array.isArray(items) ? items.map((item) => item()) : [items()]) : [];

export default defineConfig({
  site: 'https://www.dorarobotics.com/',
  base: '/',
  trailingSlash: 'ignore',
  output: 'static',

  i18n: {
    defaultLocale: 'cn',
    locales: ['cn', 'en'],
    routing: {
      prefixDefaultLocale: true,
    },
  },

  integrations: [tailwind({
    applyBaseStyles: false,
  }), sitemap(), expressiveCode(), mdx(), icon({
    include: {
      tabler: ['*'],
      'flat-color-icons': [
        'template',
        'gallery',
        'approval',
        'document',
        'advertising',
        'currency-exchange',
        'voice-presentation',
        'business-contact',
        'database',
      ],
    },
  }), ...whenExternalScripts(() =>
    partytown({
      config: { forward: ['dataLayer.push'] },
    })
  ), compress({
    CSS: true,
    HTML: {
      'html-minifier-terser': {
        removeAttributeQuotes: false,
      },
    },
    Image: false,
    JavaScript: true,
    SVG: false,
    Logger: 1,
  }), astrowind({
    config: './src/config.yaml',
  }), react()],

  image: {
    domains: ['cdn.pixabay.com', '192.168.125.136'],
  },

  server: {
    port: 81, // Replace with desired port
    host: true // Optional: Allow network access
  },

  markdown: {
    remarkPlugins: [readingTimeRemarkPlugin],
    rehypePlugins: [responsiveTablesRehypePlugin, lazyImagesRehypePlugin],
  },

  vite: {
    resolve: {
      alias: {
        '~': path.resolve(__dirname, './src'),
      },
    },
    plugins: [
      {
        name: 'trailing-slash-redirect',
        configureServer(server) {
          server.middlewares.use((req, res, next) => {
            // Remove trailing slash for all paths except root
            if (req.url && req.url.endsWith('/') && req.url !== '/') {
              const urlWithoutSlash = req.url.slice(0, -1);
              res.writeHead(301, { Location: urlWithoutSlash });
              res.end();
              return;
            }
            next();
          });
        },
      },
    ],
  },
});
