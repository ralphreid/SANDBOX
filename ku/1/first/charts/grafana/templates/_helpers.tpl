{{/*
Expand the name of the chart.
*/}}
{{- define "grafana.name" -}}
{{ .Chart.Name }}
{{- end -}}

{{/*
Create a fully qualified name.
*/}}
{{- define "grafana.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{ .Values.fullnameOverride }}
{{- else -}}
{{- if .Values.nameOverride -}}
{{ .Values.nameOverride }}
{{- else -}}
{{ include "grafana.name" . }}-{{ .Release.Name }}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Standard Kubernetes labels.
*/}}
{{- define "grafana.labels" -}}
helm.sh/chart: {{ include "grafana.name" . }}-{{ .Chart.Version | replace "+" "_" }}
app.kubernetes.io/name: {{ include "grafana.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Selector labels.
*/}}
{{- define "grafana.selectorLabels" -}}
app: {{ include "grafana.name" . }}
{{- end -}}

{{/*
Common labels to be used across multiple resources.
*/}}
{{- define "grafana.commonLabels" -}}
{{ include "grafana.selectorLabels" . }}
{{ include "grafana.labels" . }}
{{- end -}}
