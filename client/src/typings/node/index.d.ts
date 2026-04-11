// Minimal Node.js type stub for browser-targeted Angular client.
// The full @types/node package uses TypeScript 4.5+ syntax (e.g. export { type X })
// which is incompatible with the TypeScript 3.8 compiler used by Angular 9.
// This stub is placed first in typeRoots to shadow node_modules/@types/node so
// the compiler never attempts to parse the incompatible declarations.
// Add any NodeJS namespace members here if browser code ever needs them.
declare namespace NodeJS {}

// require() used in test files and webpack contexts
declare function require(module: string): any;
declare namespace require {
  function context(directory: string, useSubdirectories?: boolean, regExp?: RegExp): any;
}

// pdfjs-dist legacy paths
declare module 'pdfjs-dist/legacy/build/pdf' {
  export * from 'pdfjs-dist';
  export const LinkTarget: {
    NONE: number;
    SELF: number;
    BLANK: number;
    PARENT: number;
    TOP: number;
  };
  const pdfjsLib: any;
  export default pdfjsLib;
}
declare module 'pdfjs-dist/legacy/web/pdf_viewer' {
  export const PDFViewer: any;
  export const PDFPageView: any;
  export const EventBus: any;
  export const PDFLinkService: any;
  export const TextLayerBuilder: any;
  export const NullL10n: any;
  export const DefaultTextLayerFactory: any;
  export const GenericL10n: any;
}
