const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = merge(common, {
  mode: 'production',
  plugins: [
    new CopyPlugin({
      patterns: [
        { from: 'index.html', to: 'index.html' },
        { from: 'modulo1', to: 'modulo1' },
        { from: 'modulo2', to: 'modulo2' },
        { from: 'modulo3', to: 'modulo3' },
        { from: 'partials', to: 'partials' },
        { from: 'data', to: 'data' },
        { from: 'img', to: 'img' },
        { from: 'css', to: 'css' },
        { from: 'js', to: 'js' },
        { from: 'icon.svg', to: 'icon.svg' },
        { from: 'favicon.ico', to: 'favicon.ico' },
        { from: 'robots.txt', to: 'robots.txt' },
        { from: 'icon.png', to: 'icon.png' },
        { from: '404.html', to: '404.html' },
        { from: 'site.webmanifest', to: 'site.webmanifest' },
      ],
    }),
  ],
});
