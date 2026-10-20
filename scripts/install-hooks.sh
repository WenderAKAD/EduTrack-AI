#!/bin/sh
# Instala o hook pre-commit que regenera docs/painel-status.html a cada commit.
# Uso: sh scripts/install-hooks.sh

set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="$DIR/.git/hooks/pre-commit"

if [ ! -d "$DIR/.git" ]; then
  echo "Erro: $DIR nao e um repositorio Git."
  exit 1
fi

cp "$DIR/scripts/pre-commit.hook" "$HOOK"
chmod +x "$HOOK"
echo "Hook instalado: $HOOK"
