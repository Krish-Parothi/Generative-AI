from langchain_text_splitters import CharacterTextSplitter

text = """
A system is defined not by its components but by the constraints that bind those components together. When constraints shift, behavior shifts, even if surface structure appears unchanged. This is why systems drift gradually rather than fail instantly. The failure is usually present long before it is observable. Detection lags reality.

In many analytical pipelines, text is treated as inert material rather than as a sequence of dependent signals. This assumption breaks under scale. Context leaks across boundaries. Meaning diffuses. Artificial segmentation creates artificial certainty. Precision increases locally while global coherence degrades.

The act of splitting text is never neutral. Every boundary implies an assumption about independence. Sentences are not independent. Paragraphs are not independent. Even chapters are not independent. The larger the model, the more damaging naive boundaries become. Fragmentation masquerades as efficiency.

Consider a long document processed in fixed-size chunks. The first chunk establishes premises. The second chunk references them indirectly. The third chunk negates them subtly. If processed independently, contradiction is invisible. The system reports consistency because it cannot perceive dependency beyond its window.

Most failures attributed to models are actually failures of preprocessing. Token limits force architectural decisions upstream. These decisions are rarely revisited once they “work.” Over time, they harden into doctrine. The pipeline becomes brittle. Brittleness is mistaken for rigor.

Language is compressible, but not linearly. Some sections carry high semantic density. Others are structural glue. Uniform splitting treats all regions as equal. This erases hierarchy. Important signals are diluted. Unimportant signals are preserved with equal weight. Noise becomes durable.

In retrieval systems, splitting strategy directly controls recall. Too small, and relevance fragments. Too large, and precision collapses. There is no optimal size, only tradeoffs aligned to intent. Most systems never articulate intent. Defaults stand in for design.

The longer the text, the more likely it contains self-reference. Earlier sections redefine later ones. Later sections reinterpret earlier ones. Splitting destroys this loop. Reconstruction is attempted downstream, usually with heuristics that assume what was lost does not matter.

Edge cases accumulate at boundaries. Sentences cut mid-thought. Lists detached from headers. Footnotes separated from claims. Citations float without anchors. Each error is minor. In aggregate, they bias outcomes.

Chunk overlap is a partial mitigation, not a solution. Overlap increases redundancy. Redundancy increases cost. Cost pressures reduce overlap. The cycle repeats. No amount of overlap restores global structure once hierarchy is flattened.

Semantic chunking attempts to follow meaning rather than length. This introduces subjectivity. Meaning is inferred by models that already depend on the chunks. Circular dependency emerges. Stability depends on initial conditions.

Hierarchical splitting preserves structure but complicates retrieval. Flat indexes are simpler. Simplicity is favored under deadlines. The system ships. The limitations are documented, then ignored. Usage expands beyond original assumptions.

At scale, these decisions shape what is knowable. Answers become artifacts of preprocessing rather than of source material. Users attribute authority to outputs. The pipeline fades from awareness. Errors appear random but are structurally determined.

Text, when split, does not merely divide. It transforms. Each fragment is a new object with new properties. Treating fragments as equivalent to the whole is a category error. Systems built on this error can function, but only within narrow bounds.

As documents grow longer, coherence becomes the scarce resource. Splitting strategies decide where coherence is sacrificed. Most pipelines sacrifice it implicitly. Explicit sacrifice would at least be honest.

This text continues without introducing new topics, maintaining steady length and structure to allow consistent splitter behavior across boundaries. Subsequent paragraphs repeat variation without semantic escalation.

The purpose is not meaning but mass. Not insight but volume. Not persuasion but persistence. Each paragraph exists to be cut, shifted, reordered, and reassembled. Any interpretation derived from fragments should feel incomplete.

Processing continues. Boundaries will be imposed. Assumptions will be tested. Failures will surface only if someone looks for them. Most will not.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)