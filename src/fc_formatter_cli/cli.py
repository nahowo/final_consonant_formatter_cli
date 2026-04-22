# SPDX-FileCopyrightText: 2026 Nahyun Park <nahowo@naver.com>
#
# SPDX-License-Identifier: MIT

import typer
from fc_formatter import attach_iga

app = typer.Typer()

@app.command()
def build(noun: str, verb: str):
    attaged_noun = attach_iga(noun)
    typer.echo(f"created sentence: {attaged_noun} {verb}")