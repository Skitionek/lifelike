{{- define "mycelium.apiEnv" -}}
{{ include "mycelium.poostgresEnv" . }}
{{ include "mycelium.neo4jEnv" . }}
{{ include "mycelium.redisEnv" . }}
- name: ELASTICSEARCH_URL
  value: {{ include "mycelium.elasticsearchUrl" . }}
- name: PDFPARSER_URL
  value: http://{{ include "mycelium.fullname" . }}-pdfparser:{{ .Values.pdfparser.service.port }}
- name: APPSERVER_URL
  value: http://{{ include "mycelium.fullname" . }}-api:{{ .Values.api.service.port }}
{{- if .Values.ingress.enabled }}
- name: FRONTEND_URL
  value: https://{{ .Values.ingress.hostname }}
{{- end }}
{{- range $envName, $envValue := .Values.api.extraEnv }}
- name: {{ $envName }}
  value: {{ $envValue | quote }}
{{- end -}}
{{- end -}}
