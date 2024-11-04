/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/to_do_list_app/**/*.html',
    './static/to_do_list_app/js/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
  daisyui: {
    // themes: ['light', 'dark'],
    themes: ['dracula'],
  },
};

