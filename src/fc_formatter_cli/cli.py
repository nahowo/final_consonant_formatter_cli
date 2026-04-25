# SPDX-FileCopyrightText: 2026 Nahyun Park <nahowo@naver.com>
#
# SPDX-License-Identifier: MIT

import typer
from fc_formatter import attach_iga, attach_eulreul

app = typer.Typer()

@app.command(name = "subject")
def build_subject(noun: str, verb: str):
    attaged_noun = attach_iga(noun)
    typer.echo(f"created sentence: {attaged_noun} {verb}")

@app.command(name = "object")
def build_object(noun: str, verb: str):
    attaged_noun = attach_eulreul(noun)
    typer.echo(f"created sentence: {attaged_noun} {verb}")