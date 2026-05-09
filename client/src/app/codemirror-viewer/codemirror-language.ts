import { json } from '@codemirror/lang-json';
import { python } from '@codemirror/lang-python';
import { javascript } from '@codemirror/lang-javascript';
import { xml } from '@codemirror/lang-xml';
import { markdown } from '@codemirror/lang-markdown';
import { LanguageSupport } from '@codemirror/language';

import { isCodemirrorHandledMimeType } from 'app/shared/constants';

/**
 * Returns a CodeMirror LanguageSupport extension for the given MIME type,
 * or null for plain-text MIME types (including YAML and CSV) that have no
 * dedicated language pack.
 */
export function getLanguageExtension(mimeType: string): LanguageSupport | null {
  const normalizedMimeType = (mimeType || '').toLowerCase();

  if (normalizedMimeType.includes('json')) {
    return json();
  } else if (normalizedMimeType.includes('python') || normalizedMimeType.includes('x-python')) {
    return python();
  } else if (normalizedMimeType.includes('javascript') || normalizedMimeType.includes('typescript')) {
    return javascript();
  } else if (normalizedMimeType.includes('xml') || normalizedMimeType.includes('html')) {
    return xml();
  } else if (normalizedMimeType.includes('markdown') || normalizedMimeType.includes('x-markdown')) {
    return markdown();
  }
  return null;
}

export { isCodemirrorHandledMimeType };
