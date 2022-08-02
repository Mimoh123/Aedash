module.exports = {
    darkMode :'class',
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: ["../templates/*",
      "../templates/core/**",
   
      ]
  },
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
  variants: {},
  plugins: [],
}