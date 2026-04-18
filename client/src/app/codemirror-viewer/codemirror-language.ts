import { json } from '@codemirror/lang-json';
import { python } from '@codemirror/lang-python';
import { javascript } from '@codemirror/lang-javascript';
import { xml } from '@codemirror/lang-xml';
import { markdown } from '@codemirror/lang-markdown';
import { LanguageSupport } from '@codemirror/language';

/**
 * MIME types handled by the CodeMirror viewer.
 * Files with these MIME types will open in the read-only code/text viewer
 * instead of triggering a generic download.
 */
export const CODEMIRROR_HANDLED_MIME_TYPES: ReadonlySet<string> = new Set([
  'text/plain',
  'application/json',
  'text/x-python',
  'application/x-python',
  'text/javascript',
  'application/javascript',
  'text/typescript',
  'application/typescript',
  'text/html',
  'text/xml',
  'application/xml',
  'text/x-yaml',
  'application/x-yaml',
  'text/yaml',
  'text/markdown',
  'text/x-markdown',
  'text/csv',
]);

/**
 * Returns a CodeMirror LanguageSupport extension for the given MIME type,
 * or null for plain-text MIME types (including YAML and CSV) that have no
 * dedicated language pack.
 */
export function getLanguageExtension(mimeType: string): LanguageSupport | null {
  if (mimeType.includes('json')) {
    return json();
  } else if (mimeType.includes('python') || mimeType.includes('x-python')) {
    return python();
  } else if (mimeType.includes('javascript') || mimeType.includes('typescript')) {
    return javascript();
  } else if (mimeType.includes('xml') || mimeType.includes('html')) {
    return xml();
  } else if (mimeType.includes('markdown') || mimeType.includes('x-markdown')) {
    return markdown();
  }
  return null;
}
