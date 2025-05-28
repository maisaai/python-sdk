# Shared Types

```python
from maisa.types import TextComparator, TextExtractor, TextSummary
```

# Capabilities

Methods:

- <code title="post /v1/capabilities/compare">client.capabilities.<a href="./src/maisa/resources/capabilities/capabilities.py">compare</a>(\*\*<a href="src/maisa/types/capability_compare_params.py">params</a>) -> <a href="./src/maisa/types/shared/text_comparator.py">TextComparator</a></code>
- <code title="post /v1/capabilities/extract">client.capabilities.<a href="./src/maisa/resources/capabilities/capabilities.py">extract</a>(\*\*<a href="src/maisa/types/capability_extract_params.py">params</a>) -> <a href="./src/maisa/types/shared/text_extractor.py">TextExtractor</a></code>
- <code title="post /v1/capabilities/summarize">client.capabilities.<a href="./src/maisa/resources/capabilities/capabilities.py">summarize</a>(\*\*<a href="src/maisa/types/capability_summarize_params.py">params</a>) -> <a href="./src/maisa/types/shared/text_summary.py">TextSummary</a></code>

## Media

Methods:

- <code title="post /v1/capabilities/compare/media">client.capabilities.media.<a href="./src/maisa/resources/capabilities/media.py">compare</a>(\*\*<a href="src/maisa/types/capabilities/media_compare_params.py">params</a>) -> <a href="./src/maisa/types/shared/text_comparator.py">TextComparator</a></code>
- <code title="post /v1/capabilities/extract/media">client.capabilities.media.<a href="./src/maisa/resources/capabilities/media.py">extract</a>(\*\*<a href="src/maisa/types/capabilities/media_extract_params.py">params</a>) -> <a href="./src/maisa/types/shared/text_extractor.py">TextExtractor</a></code>
- <code title="post /v1/capabilities/summarize/media">client.capabilities.media.<a href="./src/maisa/resources/capabilities/media.py">summarize</a>(\*\*<a href="src/maisa/types/capabilities/media_summarize_params.py">params</a>) -> <a href="./src/maisa/types/shared/text_summary.py">TextSummary</a></code>

# Models

## Embeddings

Types:

```python
from maisa.types.models import Embeddings
```

Methods:

- <code title="post /v1/models/embeddings">client.models.embeddings.<a href="./src/maisa/resources/models/embeddings.py">create</a>(\*\*<a href="src/maisa/types/models/embedding_create_params.py">params</a>) -> <a href="./src/maisa/types/models/embeddings.py">Embeddings</a></code>

# Kpu

Methods:

- <code title="post /v1/kpu/run">client.kpu.<a href="./src/maisa/resources/kpu.py">run</a>(\*\*<a href="src/maisa/types/kpu_run_params.py">params</a>) -> object</code>

# FileInterpreter

## FromPdf

Methods:

- <code title="post /v1/file-interpreter/from-pdf">client.file_interpreter.from_pdf.<a href="./src/maisa/resources/file_interpreter/from_pdf.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_pdf_create_params.py">params</a>) -> object</code>

## FromDocx

Methods:

- <code title="post /v1/file-interpreter/from-docx">client.file_interpreter.from_docx.<a href="./src/maisa/resources/file_interpreter/from_docx.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_docx_create_params.py">params</a>) -> object</code>

## FromHTML

Methods:

- <code title="post /v1/file-interpreter/from-html">client.file_interpreter.from_html.<a href="./src/maisa/resources/file_interpreter/from_html.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_html_create_params.py">params</a>) -> object</code>

## FromImage

Methods:

- <code title="post /v1/file-interpreter/from-image">client.file_interpreter.from_image.<a href="./src/maisa/resources/file_interpreter/from_image.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_image_create_params.py">params</a>) -> object</code>

## FromAudio

Methods:

- <code title="post /v1/file-interpreter/from-audio">client.file_interpreter.from_audio.<a href="./src/maisa/resources/file_interpreter/from_audio.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_audio_create_params.py">params</a>) -> object</code>
