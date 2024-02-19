# AI

Types:

```python
from maisa.types import AICompareResponse, AIExtractResponse, AISummarizeResponse
```

Methods:

- <code title="post /v1/ai/compare">client.ai.<a href="./src/maisa/resources/ai/ai.py">compare</a>(\*\*<a href="src/maisa/types/ai_compare_params.py">params</a>) -> <a href="./src/maisa/types/ai_compare_response.py">AICompareResponse</a></code>
- <code title="post /v1/ai/extract">client.ai.<a href="./src/maisa/resources/ai/ai.py">extract</a>(\*\*<a href="src/maisa/types/ai_extract_params.py">params</a>) -> <a href="./src/maisa/types/ai_extract_response.py">AIExtractResponse</a></code>
- <code title="post /v1/ai/summarize">client.ai.<a href="./src/maisa/resources/ai/ai.py">summarize</a>(\*\*<a href="src/maisa/types/ai_summarize_params.py">params</a>) -> <a href="./src/maisa/types/ai_summarize_response.py">AISummarizeResponse</a></code>

## Media

Types:

```python
from maisa.types.ai import MediaCompareResponse, MediaExtractResponse, MediaSummarizeResponse
```

Methods:

- <code title="post /v1/ai/compare/media">client.ai.media.<a href="./src/maisa/resources/ai/media.py">compare</a>(\*\*<a href="src/maisa/types/ai/media_compare_params.py">params</a>) -> <a href="./src/maisa/types/ai/media_compare_response.py">MediaCompareResponse</a></code>
- <code title="post /v1/ai/extract/media">client.ai.media.<a href="./src/maisa/resources/ai/media.py">extract</a>(\*\*<a href="src/maisa/types/ai/media_extract_params.py">params</a>) -> <a href="./src/maisa/types/ai/media_extract_response.py">MediaExtractResponse</a></code>
- <code title="post /v1/ai/summarize/media">client.ai.media.<a href="./src/maisa/resources/ai/media.py">summarize</a>(\*\*<a href="src/maisa/types/ai/media_summarize_params.py">params</a>) -> <a href="./src/maisa/types/ai/media_summarize_response.py">MediaSummarizeResponse</a></code>

# Models

Types:

```python
from maisa.types import ModelRerankResponse
```

Methods:

- <code title="post /v1/models/rerank">client.models.<a href="./src/maisa/resources/models/models.py">rerank</a>(\*\*<a href="src/maisa/types/model_rerank_params.py">params</a>) -> <a href="./src/maisa/types/model_rerank_response.py">ModelRerankResponse</a></code>

## Embeddings

Types:

```python
from maisa.types.models import EmbeddingCreateResponse
```

Methods:

- <code title="post /v1/models/embeddings">client.models.embeddings.<a href="./src/maisa/resources/models/embeddings.py">create</a>(\*\*<a href="src/maisa/types/models/embedding_create_params.py">params</a>) -> <a href="./src/maisa/types/models/embedding_create_response.py">EmbeddingCreateResponse</a></code>
