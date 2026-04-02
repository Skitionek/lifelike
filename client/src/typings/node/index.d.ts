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
