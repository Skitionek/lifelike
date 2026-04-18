import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';

import {
  AbstractObjectTypeProvider,
  AbstractObjectTypeProviderHelper,
  Exporter,
} from 'app/file-types/providers/base-object.type-provider';
import { FilesystemObject } from 'app/file-browser/models/filesystem-object';
import { FilesystemService } from 'app/file-browser/services/filesystem.service';
import { CODEMIRROR_HANDLED_MIME_TYPES } from 'app/codemirror-viewer/codemirror-language';

@Injectable()
export class CodemirrorTypeProvider extends AbstractObjectTypeProvider {

  constructor(abstractObjectTypeProviderHelper: AbstractObjectTypeProviderHelper,
              protected readonly filesystemService: FilesystemService) {
    super(abstractObjectTypeProviderHelper);
  }

  handles(object: FilesystemObject): boolean {
    return CODEMIRROR_HANDLED_MIME_TYPES.has(object.mimeType);
  }

  getExporters(object: FilesystemObject): Observable<Exporter[]> {
    return of([{
      name: 'Download',
      export: () => {
        return this.filesystemService.getContent(object.hashId).pipe(
          map(blob => new File([blob], object.filename)),
        );
      },
    }]);
  }

}
