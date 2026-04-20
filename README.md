# MemeticWarfareDefence

An experimental Python sandbox for thinking about adversarial information integrity.

## Status

Early prototype. Personal research project. Not a production tool, not a
finished product, and not making claims about what it can reliably detect. The
commit history is me working through an idea in code rather than in prose.

## What the project is exploring

The premise is that individuals in 2026 are the endpoint of information
ecosystems increasingly shaped by:

- coordinated inauthentic content, both state and commercial
- synthetic multimodal media that defeats naïve perceptual checks
- reputation laundering through citation graphs and cached pages
- compression of source provenance in aggregated feeds

The question this repo pokes at: what would a *personal* defensive layer look
like — something that sits between incoming media (messages, shared articles,
voice clips, social posts, emails) and the user's attention, and which
surfaces provenance signals and contested claims before engagement rather
than after?

"Memetic warfare defence" is deliberately strong language. The name reflects
the framing, not a claim that the code operates at that scale.

## Current scope

The repo contains scaffolding for:

- input adapters for text, URL, and audio streams
- a source-registry abstraction for trusted reference material
- a claim-extraction and cross-reference loop
- structured output flagging provenance, confidence, and contested points

Multimodal handling, real-time stream processing, and messaging-channel
integrations are referenced in the structure but are not implemented
end-to-end. Treat the directory layout as an architecture sketch, not a
shipped surface.

## Running it

Requires Python 3.10+.

    git clone https://github.com/edz314/MemeticWarfareDefence.git
    cd MemeticWarfareDefence
    pip install -r requirements.txt
    python memetic_defence.py --url "https://example.com/article"

The CLI accepts `--url` for articles, `--text` for raw strings, and `--voice`
for an audio path. Output is JSON with per-claim provenance annotations.
Behaviour under adversarial input is not validated.

## Honest limitations

- "Veracity" is not a property the utility can determine. The tool can
  surface disagreement between sources, highlight absent corroboration, and
  flag synthetic-media indicators. It cannot tell you what is true.
- Cross-referencing reputable sources does not defeat an adversary who has
  already seeded those sources. The base-rate problem is real.
- No robustness testing against prompt-injected or adversarially crafted
  input.
- Source selection is itself a political act. The trusted-source basket is
  the bias you inherit.

## Why it's public

This repo exists so the ideas can be criticised in the open. If you think
the framing is wrong, or that a particular detection approach is
load-bearing in a way that won't hold up, raise an issue.

## License

See `LICENSE`.
