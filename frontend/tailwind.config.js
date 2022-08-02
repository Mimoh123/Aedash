/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/**/*.{html,js}"],
  darkMode :'class',
  theme: {
  
    extend: {
      screens: {
        'mob': {"max":"500px"},
       'tab': {"max":"640px"},
       'lap' : {'max' : '1024px'},
       'desk': {"max":"1280px"},
        'scr-fix': {'min': '500px', 'max': '640px'},
      }
    },
  },
  plugins: [
    require("tailwindcss-hyphens"),
    require('@tailwindcss/forms'),
  ],
}
