{{/* vim: set filetype=mustache: */}}

{{/*
Expand the name of the chart.
*/}}
{{- define "mycelium.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "mycelium.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end -}}

{{/* ---------------------------------------------------------------------- */}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "mycelium.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{/* ---------------------------------------------------------------------- */}}

{{/*
Common labels
*/}}
{{- define "mycelium.labels" -}}
helm.sh/chart: {{ include "mycelium.chart" . }}
{{ include "mycelium.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: mycelium
{{- end -}}

{{/* ---------------------------------------------------------------------- */}}

{{/*
Selector labels
*/}}
{{- define "mycelium.selectorLabels" -}}
app.kubernetes.io/name: {{ include "mycelium.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}


{{/* ---------------------------------------------------------------------- */}}
{{/* PostgreSQL                                                             */}}
{{/* ---------------------------------------------------------------------- */}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "mycelium.postgresql.fullname" -}}
{{- if .Values.postgresql.fullnameOverride -}}
{{- .Values.postgresql.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default "postgresql" .Values.postgresql.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Return the PostgreSQL hostname
*/}}
{{- define "mycelium.postgresqlHost" -}}
{{- if .Values.postgresql.enabled }}
    {{- printf "%s" (include "mycelium.postgresql.fullname" .) -}}
{{- else -}}
    {{- printf "%s" .Values.postgresqlExternal.host -}}
{{- end -}}
{{- end -}}

{{/*
Return the PostgreSQL port
*/}}
{{- define "mycelium.postgresqlPort" -}}
{{- if .Values.postgresql.enabled }}
    {{- printf "5432" -}}
{{- else -}}
    {{- .Values.postgresqlExternal.port -}}
{{- end -}}
{{- end -}}


{{/*
Return the PostgreSQL database name
*/}}
{{- define "mycelium.postgresqlDatabase" -}}
{{- if .Values.postgresql.enabled }}
    {{- printf "%s" .Values.postgresql.auth.database -}}
{{- else -}}
    {{- printf "%s" .Values.postgresqlExternal.database -}}
{{- end -}}
{{- end -}}

{{/*
Return the PostgreSQL user
*/}}
{{- define "mycelium.postgresqlUser" -}}
{{- if .Values.postgresql.enabled }}
    {{- default "postgres" .Values.postgresql.auth.username | quote -}}
{{- else -}}
    {{- printf "%s" .Values.postgresqlExternal.user -}}
{{- end -}}
{{- end -}}

{{/*
Return the PostgreSQL password
*/}}
{{- define "mycelium.postgresqlPassword" -}}
{{- if .Values.postgresql.enabled }}
    {{- printf "%s" .Values.postgresql.auth.postgresPassword -}}
{{- else -}}
    {{- printf "%s" .Values.postgresqlExternal.password -}}
{{- end -}}
{{- end -}}


{{/*
Set postgres secret
*/}}
{{- define "mycelium.postgresql.secret" -}}
{{- if .Values.postgresql.enabled -}}
{{- template "mycelium.postgresql.fullname" . -}}
{{- else -}}
{{- template "mycelium.fullname" . -}}
{{- end -}}
{{- end -}}


{{/*
Set postgres secretKey
*/}}
{{- define "mycelium.postgresql.secretKey" -}}
{{- if .Values.postgresql.enabled -}}
"postgresql-password"
{{- else -}}
{{- default "postgresql-password" .Values.postgresqlExternal.existingSecretKey | quote -}}
{{- end -}}
{{- end -}}


{{/* ---------------------------------------------------------------------- */}}
{{/* Neo4J                                                                  */}}
{{/* ---------------------------------------------------------------------- */}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "mycelium.neo4j.fullname" -}}
{{- if .Values.neo4j.fullnameOverride -}}
{{- .Values.neo4j.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default "neo4j" .Values.neo4j.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Return the Neo4j hostname
*/}}
{{- define "mycelium.neo4jHost" -}}
{{- if .Values.neo4j.enabled }}
    {{- printf "%s" (include "mycelium.neo4j.fullname" .) -}}
{{- else -}}
    {{- printf "%s" .Values.neo4jExternal.host -}}
{{- end -}}
{{- end -}}

{{/*
Return the Neo4j port
*/}}
{{- define "mycelium.neo4jPort" -}}
{{- if .Values.neo4j.enabled }}
    {{- printf "7687" -}}
{{- else -}}
    {{- .Values.neo4jExternal.port -}}
{{- end -}}
{{- end -}}

{{/*
Return the Neo4j user
*/}}
{{- define "mycelium.neo4jUser" -}}
{{- if .Values.neo4j.enabled }}
    {{- printf "neo4j" -}}
{{- else -}}
    {{- printf "%s" .Values.neo4jExternal.user -}}
{{- end -}}
{{- end -}}

{{/*
Return the Neo4j password
*/}}
{{- define "mycelium.neo4jPassword" -}}
{{- if .Values.neo4j.enabled }}
    {{- printf "%s" .Values.neo4j.neo4jPassword -}}
{{- else -}}
    {{- printf "%s" .Values.neo4jExternal.password -}}
{{- end -}}
{{- end -}}

{{/*
Return the Neo4j database name
*/}}
{{- define "mycelium.neo4jDatabase" -}}
{{- if .Values.neo4j.enabled }}
    {{- default "neo4j" .Values.neo4j.defaultDatabase -}}
{{- else -}}
    {{- default "neo4j" .Values.neo4jExternal.database -}}
{{- end -}}
{{- end -}}

{{/* ---------------------------------------------------------------------- */}}
{{/* Elasticsearch                                                          */}}
{{/* ---------------------------------------------------------------------- */}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "mycelium.elasticsearch.fullname" -}}
{{- if .Values.elasticsearch.fullnameOverride -}}
{{- .Values.elasticsearch.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default "elasticsearch" .Values.elasticsearch.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Return the Elasticsearch hostname
*/}}
{{- define "mycelium.elasticsearchHost" -}}
{{- if .Values.elasticsearch.enabled }}
    {{- printf "%s" (include "mycelium.elasticsearch.fullname" .) -}}
{{- else -}}
    {{- printf "%s" .Values.elasticsearchExternal.host -}}
{{- end -}}
{{- end -}}

{{/*
Return the Elasticsearch port
*/}}
{{- define "mycelium.elasticsearchPort" -}}
{{- if .Values.elasticsearch.enabled }}
    {{- printf "9200" -}}
{{- else -}}
    {{- .Values.elasticsearchExternal.port | quote -}}
{{- end -}}
{{- end -}}

{{/*
Return the Neo4j user
*/}}
{{- define "mycelium.elasticsearchUser" -}}
{{- if .Values.elasticsearch.enabled }}
    {{- range $env := .Values.elasticsearch.extraEnvs }}
    {{- if eq $env.name "ELASTIC_USERNAME" }}
        {{- printf "%s" $env.value -}}
    {{- end -}}
    {{- end -}}
{{- else -}}
    {{- printf "%s" .Values.elasticsearchExternal.user -}}
{{- end -}}
{{- end -}}

{{/*
Return the Elasticsearch password
*/}}
{{- define "mycelium.elasticsearchPassword" -}}
  {{- if .Values.elasticsearch.enabled }}
  {{- range $env := .Values.elasticsearch.extraEnvs }}
    {{- if eq $env.name "ELASTIC_PASSWORD" }}
      {{- printf "%s" $env.value -}}
    {{- end -}}
  {{- end -}}
{{- else -}}
  {{- printf "%s" .Values.elasticsearchExternal.password -}}
{{- end -}}
{{- end -}}

{{- define "mycelium.elasticsearchUrl" -}}
{{- if .Values.elasticsearch.enabled }}
    {{- printf "http://%s:%s@%s:%s" (include "mycelium.elasticsearchUser" .) (include "mycelium.elasticsearchPassword" .) (include "mycelium.elasticsearchHost" .) (include "mycelium.elasticsearchPort" .) -}}
{{- else -}}
    {{- printf "%s" .Values.elasticsearchExternal.url -}}
{{- end -}}
{{- end -}}



{{/* ---------------------------------------------------------------------- */}}
{{/* Redis                                                                  */}}
{{/* ---------------------------------------------------------------------- */}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "mycelium.redis.fullname" -}}
{{- if .Values.redis.fullnameOverride -}}
{{- .Values.redis.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default "redis" .Values.redis.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Return the Redis hostname
*/}}
{{- define "mycelium.redisHost" -}}
{{- if .Values.redis.enabled }}
  {{- printf "%s-master" (include "mycelium.redis.fullname" .) -}}
{{- else -}}
  {{- printf "%s" .Values.redisExternal.host -}}
{{- end -}}
{{- end -}}

{{/*
Return the Redis port
*/}}
{{- define "mycelium.redisPort" -}}
  {{- if .Values.redis.enabled }}
    {{- printf "6379" -}}
  {{- else -}}
    {{- .Values.redisExternal.port -}}
  {{- end -}}
{{- end -}}

{{/*
Return the Redis password
*/}}
{{- define "mycelium.redisPassword" -}}
{{- if .Values.redis.enabled }}
    {{- printf "%s" .Values.redis.auth.password -}}
{{- else }}
    {{- printf "%s" .Values.redisExternal.password -}}
{{- end }}
{{- end -}}


{{/* ---------------------------------------------------------------------- */}}


{{/*
Common image spec
*/}}

{{- define "mycelium.image" -}}
image: {{ .image.repository }}:{{ .image.tag | default (printf "%s" .Chart.AppVersion) }}
imagePullPolicy: {{ .image.imagePullPolicy | default "IfNotPresent" }}
{{- if .image.pullSecrets }}
imagePullSecrets: {{ toYaml .image.pullSecrets | nindent 2 }}
{{- end }}
{{- end -}}


{{/* ---------------------------------------------------------------------- */}}


{{/*
Common pod spec
*/}}
{{- define "mycelium.podSpec" -}}
{{- if .affinity }}
affinity: {{ toYaml .affinity | nindent 2 }}
{{- end }}
{{- if .nodeSelector }}
nodeSelector: {{ toYaml .nodeSelector | nindent 2 }}
{{- end }}
{{- if .tolerations }}
tolerations: {{ toYaml .tolerations | nindent 2 }}
{{- end }}
{{- if .schedulerName }}
schedulerName: {{ .schedulerName }}
{{- end }}
securityContext:
{{- $securityContext := .podSecurityContext | default (dict) | deepCopy }}
{{- toYaml $securityContext | nindent 2 }}
{{- end -}}


{{/* ---------------------------------------------------------------------- */}}


{{/*
Common health checks
*/}}
{{- define "mycelium.healthChecks" -}}
{{- if .livenessProbe.enabled -}}
livenessProbe:
  httpGet:
    path: {{ .livenessProbe.path | default "/healthz" }}
    port: {{ .service.port }}
    scheme: {{ .livenessProbe.scheme | default "HTTP" }}
  initialDelaySeconds: {{ .livenessProbe.initialDelaySeconds | default 10 }}
  timeoutSeconds: {{ .livenessProbe.timeoutSeconds | default 5 }}
  periodSeconds: {{ .livenessProbe.periodSeconds | default 10 }}
  successThreshold: {{ .livenessProbe.successThreshold | default 1 }}
  failureThreshold: {{ .livenessProbe.failureThreshold | default 3 }}
{{- end }}
{{- if .readinessProbe.enabled }}
readinessProbe:
  httpGet:
    path: {{ .readinessProbe.path | default "/healthz" }}
    port: {{ .service.port }}
    scheme: {{ .readinessProbe.scheme | default "HTTP" }}
  initialDelaySeconds: {{ .readinessProbe.initialDelaySeconds | default 10 }}
  timeoutSeconds: {{ .readinessProbe.timeoutSeconds | default 5 }}
  periodSeconds: {{ .readinessProbe.periodSeconds | default 10 }}
  successThreshold: {{ .readinessProbe.successThreshold | default 1 }}
  failureThreshold: {{ .readinessProbe.failureThreshold | default 3 }}
{{- end }}
{{- end -}}


{{/* ---------------------------------------------------------------------- */}}


{{/*
PostgreSQL environment variables helper
*/}}
{{- define "mycelium.poostgresEnv" -}}
- name: POSTGRES_HOST
  value: {{ template "mycelium.postgresqlHost" . }}
- name: POSTGRES_PORT
  value: {{ include "mycelium.postgresqlPort" . | quote }}
- name: POSTGRES_USER
  value: {{ template "mycelium.postgresqlUser" . }}
- name: POSTGRES_PASSWORD
  value: {{ include "mycelium.postgresqlPassword" . | quote }}
- name: POSTGRES_DB
  value: {{ template "mycelium.postgresqlDatabase" . }}
{{- end -}}


{{/*
Neo4j environment variables helper
*/}}
{{- define "mycelium.neo4jEnv" -}}
- name: NEO4J_HOST
  value: {{ template "mycelium.neo4jHost" . }}
- name: NEO4J_PORT
  value: {{ include "mycelium.neo4jPort" . | quote }}
- name: NEO4J_AUTH
  value: {{ template "mycelium.neo4jUser" . }}/{{ template "mycelium.neo4jPassword" . }}
- name: NEO4J_DB
  value: {{ template "mycelium.neo4jDatabase" . }}
{{- end -}}


{{/*
Redis environment variables helper
*/}}
{{- define "mycelium.redisEnv" -}}
- name: REDIS_HOST
  value: {{ template "mycelium.redisHost" . }}
- name: REDIS_PORT
  value: {{ include "mycelium.redisPort" . | quote }}
- name: REDIS_PASSWORD
  value: {{ include "mycelium.redisPassword" . | quote }}
{{- end -}}
