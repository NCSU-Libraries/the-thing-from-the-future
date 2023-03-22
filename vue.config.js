module.exports = {
  publicPath: process.env.url_path ? process.env.url_path : '/the-thing-from-the-future/',
  chainWebpack: config => {
    // GraphQL Loader
    config.module
      .rule('csv')
      .test(/\.csv$/)
      .use('raw-loader')
        .loader('raw-loader')
        .end()
  }
}