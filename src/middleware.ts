import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware((context, next) => {
  const url = context.url.pathname;

  // Remove trailing slash for all paths except root
  if (url.endsWith('/') && url !== '/') {
    const urlWithoutSlash = url.slice(0, -1);
    return context.redirect(urlWithoutSlash, 301);
  }

  return next();
});
