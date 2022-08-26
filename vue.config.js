 // const IS_PRODUCTION = process.env.NODE_ENV === 'production'

module.exports = {
    outputDir: 'dist',
    assetsDir: 'static',
     // publicPath: IS_PRODUCTION
     // ? 'https://d3i9hwjfzmc2xm.cloudfront.net'
     // : '/',
    // For Production, replace set baseUrl to CDN
    // And set the CDN origin to `yourdomain.com/static`
    // Whitenoise will serve once to CDN which will then cache
    // and distribute
    publicPath: '/',
    //indexPath: "index.html",
    devServer: {
      proxy: {
        '/api/*': {
          // Forward frontend dev server request for /api to django dev server
          target: 'http://127.0.0.1:8000/',
        }
      }
    }
  }
