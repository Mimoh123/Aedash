/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/**/*.{html,js}"],
  darkMode :'class',
  theme: {
  
    extend: {
      screens: {
        'mob': {"max":"500px"},
        'scr-fix': {'min': '500px', 'max': '640px'},
      }
    },
  },
  plugins: [],
}
