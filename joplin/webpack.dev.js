var BundleTracker = require("webpack-bundle-tracker");
var path = require("path");

module.exports = {
  mode: "development",
  watch: true,
  watchOptions: {
    poll: true
  },
  entry: {
    admin: "./js/admin.js",
    editor: "./js/editor.js",
    createContentModal: './js/create-content-modal.js'
  },
  module: {
    rules: [
        {
            test: /\.js?$/,
            exclude: /node_modules/,
            use: {
              loader: "babel-loader"
            }
        },
        {
            test: /\.scss$/,
            loaders: [
              "style-loader", // creates style nodes from JS strings
              "css-loader", // translates CSS into CommonJS
              "sass-loader" // compiles Sass to CSS
            ]
        },
        {
            test: /\.(png|jp(e*)g|svg)$/,
            use: [{
                loader: 'url-loader',
                options: {
                    limit: 8000, // Convert images < 8kb to base64 strings
                    name: 'images/[hash]-[name].[ext]'
                }
            }]
        }
    ],
  },
  output: {
    path: path.resolve("./static/webpack_bundles/"),
    filename: "[name]-[hash].js"
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: "./static/webpack-stats.json"
    })
  ]
};
