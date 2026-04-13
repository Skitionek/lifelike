# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

> This changelog tracks changes made in the [Lifelike Afterhours fork](https://github.com/Skitionek/lifelike)
> since it was created from the upstream [SBRG/lifelike](https://github.com/SBRG/lifelike) repository.

---

## [Unreleased]

### Removed
- Dropped `jquery`, `jquery-ui`, `jquery-ui-dist`, `qtip2`, `jqueryui`, `@types/jquery`, and `@types/jqueryui` dependencies from the client

### Changed
- Replaced jQuery DOM manipulation in `bioc-view.component.ts` with native DOM APIs and CSS transitions
- Replaced jQuery + qtip2 annotation tooltips in `pdf-viewer-lib.component.ts` with Bootstrap 5 Popover
- Replaced jQuery UI `.resizable()` in `resizable.directive.ts` with native CSS `resize` property

### Security
- Upgrade `pdfjs-dist` 2.9.359 → 4.2.67 to fix arbitrary JavaScript execution on malicious PDF open (CVE-2024-4367, affects ≤ 4.1.392)

### Changed
- Migrated PDF viewer to pdfjs-dist v4 API: removed `TextLayerBuilder.disableTextLayer`/`enhanceTextSelection` (controlled via `textLayerMode` option), moved `LinkTarget` import from core lib to viewer bundle, updated `EventBus` constructor (no argument), updated all type-import paths to `pdfjs-dist/types/src/`
- Added `@angular-builders/custom-webpack` with `experiments.topLevelAwait: true` to handle pdfjs-dist v4 ES module bundles that use top-level await

## [2026-04-12]

### Added
- **Zero-configuration dev environment** via VS Code Dev Container (`.devcontainer/`) — start developing with a single click in GitHub Codespaces or VS Code ([#154])
- **Alternative tab/panel implementation** using [`route-with-dynamic-outlets`](https://github.com/Skitionek/route-with-dynamic-outlets): each workspace tab now maps to a named Angular router outlet; open tabs are encoded in the URL ([#153])
- **Automated UI tests** — added Angular unit specs for `sort-legend`, `results-summary`, `collapsible-window`, `pagination`, `dashboard`, `kg-statistics`, `percent-input`, and `warning-pill` components ([#154])
- **Automated CI/CD** with GitHub Actions workflows for tests, Docker image builds, CodeQL security scans, and Dependabot auto-merge ([#149])
- **Copilot coding agent** instructions and auto-fix workflow for AI-assisted development ([#149])

### Changed
- **Angular v9 → v14** (BREAKING): upgraded all Angular, NgRx, RxJS, ng-bootstrap, chart.js, and related packages; removed `entryComponents`, migrated `throwError`/`toPromise` to RxJS 7 API, switched to ES2020 target ([#150])
- **pdfjs-dist** 2.9.359 → 4.2.67 ([#155])

## [2026-04-11]

### Changed
- **Alembic migrations squashed**: replaced 100 incremental migration files with a single clean baseline schema migration (`000000000000_squashed.py`) covering all 21 tables ([#152])
- Dependabot auto-merge CI pipeline added: automerge patch/minor Dependabot PRs when all CI checks pass ([#149])
- Various dependency bumps: `bioc` 1.3.7→2.1, `marshmallow-dataclass` 8.5.3→8.7.1, `google-cloud-storage` 1.43→3.10, `requests` 2.33.0→2.33.1, `marshmallow-sqlalchemy` 1.4.2→1.5.0, `pytest` 9.0.2→9.0.3 (appserver, statistical-enrichment, cache-invalidator) ([#136]–[#141])
- Security: `cryptography` 46.0.6→46.0.7 ([#134])
- `actions/github-script` 7→9 ([#147])
- Maven dependencies bump ([#148])

## [2026-04-02]

### Fixed
- **Flask 3.x compatibility**: upgraded `flask-sqlalchemy` 2.5.1→3.0.5 to fix `ImportError` on `flask._app_ctx_stack` removed in Flask 2+ ([#132])
- **TypeScript 3.8 compatibility**: pinned `@types/jqueryui` to 1.12.21 to avoid template literal types introduced in 1.12.22+ that TypeScript 3.8 cannot parse ([#132])

### Changed
- Various dependency bumps: `sendgrid` 6.9.3→6.12.5, `sentry-sdk` 1.45→2.57, `intervaltree` 3.1→3.2.1, `types-redis`, `types-requests`, `mypy` 1.19→1.20, `gunicorn` 25.2→25.3, `codelyzer` 5.2→6.0, `jasmine-spec-reporter` 4.2→7.0, `@types/node` 12→25 ([#117]–[#128])
- `lodash` / `lodash-es` 4.17.23→4.18.1 ([#130], [#133])

## [2026-03-31]

### Changed
- **Flask** 2.3.3→3.1.3 ([#116])

### Security
- `cryptography` 46.0.5→46.0.6 ([#115])

## [2026-03-27]

### Added
- **Fork branding**: renamed project to *Lifelike Afterhours*, updated logos, README, and project identity to reflect the fork purpose ([#114])
- **GitHub Actions CI workflows**: Docker build/publish, BrowserStack integration tests, SonarQube analysis, CodeQL code scanning, Dependabot configuration ([#109])
- **Git hooks** for linting and code formatting ([#109])
- **VS Code workspace configuration** (`.vscode/`) ([#109])

### Fixed
- **Bootstrap 5 SCSS architecture**: removed duplicate Bootstrap import from `styles.scss`; fixed `angular.json` build order (`scss/bootstrap.scss` before `styles.scss`); cleaned `_variables.scss`, `_buttons.scss`, `_window.scss` for Bootstrap 5 compatibility ([#109])
- **d3 v5→v7 migration**: replaced removed `d3.event` global with event parameter; replaced `d3.mouse()` with `d3.pointer()`; migrated `sankey.component.ts` to d3 v7 event API ([#109])
- **SQLAlchemy 1.4 compatibility**: replaced deprecated `db.Binary` with `db.LargeBinary` in `models/files.py` and `models/views.py` ([#109])
- Removed non-existent Bootstrap 5 import path `bootstrap/js/dist/index` from `main.ts` ([#109])
- Fixed `Dockerfile` client build: added `--ignore-engines` yarn flag for Node 20 compatibility ([#109])

---

[#109]: https://github.com/Skitionek/lifelike/pull/109
[#114]: https://github.com/Skitionek/lifelike/pull/114
[#115]: https://github.com/Skitionek/lifelike/pull/115
[#116]: https://github.com/Skitionek/lifelike/pull/116
[#117]: https://github.com/Skitionek/lifelike/pull/117
[#128]: https://github.com/Skitionek/lifelike/pull/128
[#130]: https://github.com/Skitionek/lifelike/pull/130
[#132]: https://github.com/Skitionek/lifelike/pull/132
[#133]: https://github.com/Skitionek/lifelike/pull/133
[#134]: https://github.com/Skitionek/lifelike/pull/134
[#136]: https://github.com/Skitionek/lifelike/pull/136
[#141]: https://github.com/Skitionek/lifelike/pull/141
[#147]: https://github.com/Skitionek/lifelike/pull/147
[#148]: https://github.com/Skitionek/lifelike/pull/148
[#149]: https://github.com/Skitionek/lifelike/pull/149
[#150]: https://github.com/Skitionek/lifelike/pull/150
[#152]: https://github.com/Skitionek/lifelike/pull/152
[#153]: https://github.com/Skitionek/lifelike/pull/153
[#154]: https://github.com/Skitionek/lifelike/pull/154
[#155]: https://github.com/Skitionek/lifelike/pull/155
