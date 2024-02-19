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

## RerankResource

Types:

```python
from maisa.types.models import Rerank
```

Methods:

- <code title="post /v1/models/rerank">client.models.rerank.<a href="./src/maisa/resources/models/rerank.py">create</a>(\*\*<a href="src/maisa/types/models/rerank_create_params.py">params</a>) -> <a href="./src/maisa/types/models/rerank.py">Rerank</a></code>

# FileInterpreter

## FromPdf

Types:

```python
from maisa.types.file_interpreter import FromPdfCreateResponse
```

Methods:

- <code title="post /v1/file-interpreter/from-pdf">client.file_interpreter.from_pdf.<a href="./src/maisa/resources/file_interpreter/from_pdf.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_pdf_create_params.py">params</a>) -> <a href="./src/maisa/types/file_interpreter/from_pdf_create_response.py">object</a></code>

## FromDocx

Types:

```python
from maisa.types.file_interpreter import FromDocxCreateResponse
```

Methods:

- <code title="post /v1/file-interpreter/from-docx">client.file_interpreter.from_docx.<a href="./src/maisa/resources/file_interpreter/from_docx.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_docx_create_params.py">params</a>) -> <a href="./src/maisa/types/file_interpreter/from_docx_create_response.py">object</a></code>

## FromHTML

Types:

```python
from maisa.types.file_interpreter import FromHTMLCreateResponse
```

Methods:

- <code title="post /v1/file-interpreter/from-html">client.file_interpreter.from_html.<a href="./src/maisa/resources/file_interpreter/from_html.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_html_create_params.py">params</a>) -> <a href="./src/maisa/types/file_interpreter/from_html_create_response.py">object</a></code>

## FromImageResource

Types:

```python
from maisa.types.file_interpreter import FromImage
```

Methods:

- <code title="post /v1/file-interpreter/from-image">client.file_interpreter.from_image.<a href="./src/maisa/resources/file_interpreter/from_image.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_image_create_params.py">params</a>) -> <a href="./src/maisa/types/file_interpreter/from_image.py">FromImage</a></code>

## FromAudio

Types:

```python
from maisa.types.file_interpreter import FromAudioCreateResponse
```

Methods:

- <code title="post /v1/file-interpreter/from-audio">client.file_interpreter.from_audio.<a href="./src/maisa/resources/file_interpreter/from_audio.py">create</a>(\*\*<a href="src/maisa/types/file_interpreter/from_audio_create_params.py">params</a>) -> <a href="./src/maisa/types/file_interpreter/from_audio_create_response.py">object</a></code>

# Mainet

## SearchResource

Types:

```python
from maisa.types.mainet import Search
```

Methods:

- <code title="post /v1/mainet/search">client.mainet.search.<a href="./src/maisa/resources/mainet/search.py">create</a>(\*\*<a href="src/maisa/types/mainet/search_create_params.py">params</a>) -> <a href="./src/maisa/types/mainet/search.py">Search</a></code>
