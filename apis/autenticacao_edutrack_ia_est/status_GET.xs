// Health check do backend do EduTrack AI.
// Serve para validar a Base URL: abrir no navegador e no FlutterFlow (API Call
// do tipo GET) deve devolver 200 com o JSON abaixo.
query "status" verb=GET {
  api_group = "AutenticacaoEduTrackIAEst"

  input {
  }

  stack {
  }

  response = {
    status: "ok"
    app: "EduTrack AI"
    modulo: "1 - Introducao ao Spec-Driven Development"
    ambiente: "producao"
    instance: "x8ki-letl-twmt"
    timestamp: "now"
  }
}
