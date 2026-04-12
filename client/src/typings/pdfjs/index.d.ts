// Ambient module declaration for pdfjs-dist v4 legacy viewer bundle.
// In pdfjs-dist >=4.0, the legacy builds are ES Modules (.mjs). Angular's
// webpack 5 config resolves them at build time, but TypeScript's
// `moduleResolution: node` cannot find them via the bare specifier.
// This declaration lets the TypeScript compiler accept the import while
// webpack handles actual module loading.
declare module 'pdfjs-dist/legacy/web/pdf_viewer';
