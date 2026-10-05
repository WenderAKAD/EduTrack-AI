// Health check do backend do EduTrack AI.
//
// No Xano o "Name" do endpoint é o PATH e o "Verb" é o método HTTP.
// Este endpoint fica em:
//   https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC/status
//
// Serve para validar a Base URL: abrir no navegador e no FlutterFlow
// deve devolver 200 com o JSON abaixo.
//
// Nota: o campo "timestamp" devolve a string literal "now". Para gerar um
// timestamp real (epoch em ms) usar datetime_now() — ajuste previsto para a
// Tarefa 08.
query "status" verb=GET {
  api_group = "AutenticacaoEduTrackIAEst"
  description = "Health check do backend do EduTrack AI."

  input {
  }

  stack {
  }

  response = {
    status: "ok"
    app: "EduTrack AI"
    modulo: "1 - Introducao ao Spec-Driven Development"
    instance: "x8ki-letl-twmt"
    timestamp: "now"
  }
}
