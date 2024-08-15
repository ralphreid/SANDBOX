{{- define "opentelemetry.name" -}}
{{ .Chart.Name }}
{{- end -}}

{{- define "opentelemetry.fullname" -}}
{{ include "opentelemetry.name" . }}-{{ .Release.Name }}
{{- end -}}
