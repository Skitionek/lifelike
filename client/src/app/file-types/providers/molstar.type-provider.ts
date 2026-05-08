import {
  ComponentFactory,
  ComponentFactoryResolver,
  Injectable,
  Injector,
} from '@angular/core';

import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';

import {
  AbstractObjectTypeProvider,
  AbstractObjectTypeProviderHelper,
  Exporter,
  PreviewOptions,
} from 'app/file-types/providers/base-object.type-provider';
import { FilesystemObject } from 'app/file-browser/models/filesystem-object';
import { FilesystemService } from 'app/file-browser/services/filesystem.service';
import { MolstarViewComponent } from 'app/molstar-viewer/components/molstar-view.component';
import { mapBlobToBuffer } from 'app/shared/utils/files';
import { MimeTypes, PROTEIN_STRUCTURE_MIME_TYPES } from 'app/shared/constants';

type ProteinStructureFormat = 'pdb' | 'mmcif';

@Injectable()
export class MolstarTypeProvider extends AbstractObjectTypeProvider {

  constructor(
    abstractObjectTypeProviderHelper: AbstractObjectTypeProviderHelper,
    protected readonly filesystemService: FilesystemService,
    protected readonly injector: Injector,
    protected readonly componentFactoryResolver: ComponentFactoryResolver,
  ) {
    super(abstractObjectTypeProviderHelper);
  }

  handles(object: FilesystemObject): boolean {
    const filename = (object?.filename || '').toLowerCase();
    return PROTEIN_STRUCTURE_MIME_TYPES.has(object.mimeType)
      || filename.endsWith('.pdb')
      || filename.endsWith('.cif')
      || filename.endsWith('.mmcif')
      || object.mimeType === 'chemical/x-mmcif';
  }

  createPreviewComponent(object: FilesystemObject, contentValue$: Observable<Blob>,
                         options?: PreviewOptions) {
    const format = this.getFormatForObject(object);
    if (!format) {
      return of(undefined);
    }

    const factory: ComponentFactory<MolstarViewComponent> =
      this.componentFactoryResolver.resolveComponentFactory(MolstarViewComponent);
    const componentRef = factory.create(this.injector);
    const instance: MolstarViewComponent = componentRef.instance;
    instance.embedded = true;
    instance.object = object;

    return contentValue$.pipe(
      mapBlobToBuffer(),
      map((buffer) => new TextDecoder('utf-8').decode(buffer)),
      map((text) => {
        instance.setStructureData(text, format);
        return componentRef;
      }),
    );
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

  private getFormatForObject(object: FilesystemObject): ProteinStructureFormat | undefined {
    const filename = (object?.filename || '').toLowerCase();

    if (filename.endsWith('.pdb') || object?.mimeType === MimeTypes.Pdb) {
      return 'pdb';
    }

    if (
      filename.endsWith('.cif') ||
      filename.endsWith('.mmcif') ||
      object?.mimeType === MimeTypes.Cif ||
      object?.mimeType === 'chemical/x-mmcif'
    ) {
      return 'mmcif';
    }

    return undefined;
  }
}
