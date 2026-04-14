{{- define "deep-dive-devops-platform.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" -}}
{{- end -}}

{{- define "deep-dive-devops-platform.labels" -}}
helm.sh/chart: {{ include "deep-dive-devops-platform.chart" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}
