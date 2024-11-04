# NPM

## Getting Started


**Steps:**
1. Initialize npm manager:
   ```bash
   npm init -y
   ```

2. Install any npm pack that you want, in this example, tailwindcss and daisyui:
   ```bash
   npm install tailwindcss daisyui @tailwindcss/typography @tailwindcss/forms
   ```
   
   Note: the @ are plugins for tailwindcss
   
3. with npx initialize the json config.
   ```bash
   npx tailwindcss init
   ```

4. Setup the config:

```
module.exports = {
  content: [
    './templates/to_do_list_app/**/*.html',  // point to the html of the app
    './static/to_do_list_app/js/*.js',  // Point to any other js
  ],
  theme: {
    extend: {},
  },
  plugins: [  // add the plugins, as daisyui and the other for tailwind
    require('daisyui'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
  daisyui: {
    // themes: ['light', 'dark'],  // selec themes
    themes: ['dracula'],
  },
};
```

5. Create a input.css for tailwind, in the static path

```bash 
mdkir static/to_do_list_app/css/
 ```
```bash
   touch tailwind_input.css
```

6. Add this to the created file
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

7. Compile the css pack
```bash
npx tailwindcss -i ./static/to_do_list_app/css/tailwind_input.css -o ./static/to_do_list_app/css/tailwind_daisyui_output.css

```





