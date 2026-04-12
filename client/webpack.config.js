/**
 * Custom webpack configuration to enable top-level await,
 * which is required by pdfjs-dist v4+ ES module bundles.
 */
module.exports = {
  experiments: {
    topLevelAwait: true,
  },
};
