module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: ["../templates/*","../templates/core/*"
      ]
  },
  theme: {
      extend: {},
  },
  variants: {},
  plugins: [],
}