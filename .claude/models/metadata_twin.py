"""Pydantic v2 models for metadata twin JSON validation."""

from typing import List, Optional
from pydantic import BaseModel, Field, field_validator


class Placeholder(BaseModel):
    """Placeholder variable definition."""
    key: str = Field(..., pattern=r"^\$\{[a-z0-9-]+\}$")
    description: str
    type: str
    format: Optional[str] = None
    required: bool


class Transformation(BaseModel):
    """Text transformation record."""
    type: str
    description: str
    before: str
    after: str
    timestamp: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class BrandguideCompliance(BaseModel):
    """Brandguide compliance scores."""
    overall_score: float = Field(..., ge=0.0, le=1.0)
    voice_check: float = Field(..., ge=0.0, le=1.0)
    tone_check: float = Field(..., ge=0.0, le=1.0)
    modals_allowed: bool
    modals_forbidden_detected: List[str]
    max_line_length_ok: bool
    max_file_size_ok: bool
    utf8_lf_ok: bool
    issues: List[str]


class QualityMetrics(BaseModel):
    """Text quality metrics."""
    word_count: int = Field(..., ge=0)
    character_count: int = Field(..., ge=0)
    readability_score: float
    avg_sentence_length: float = Field(..., ge=0)
    avg_word_length: float = Field(..., ge=0)
    technical_term_density: float = Field(..., ge=0.0, le=1.0)
    passive_voice_ratio: float = Field(..., ge=0.0, le=1.0)
    flesch_reading_ease: float
    gunning_fog_index: float


class Relationships(BaseModel):
    """Fragment relationships."""
    references: List[str]
    referenced_by: List[str]
    related_fragments: List[str]


class ReviewStatus(BaseModel):
    """Review and approval status."""
    status: str = Field(..., pattern=r"^(pending|approved|rejected|needs_review)$")
    reviewed_by: str
    reviewed_at: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    review_notes: str


class Audit(BaseModel):
    """Audit trail information."""
    fragment_id: str
    chunk_id: str
    ingestion_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    sha256_original: str = Field(..., pattern=r"^[a-f0-9]{64}$")
    sha256_transformed: str = Field(..., pattern=r"^[a-f0-9]{64}$")
    classification_confidence: float = Field(..., ge=0.0, le=1.0)
    classification_reasoning: str
    alternative_components: List[str]


class Metadata(BaseModel):
    """Content metadata."""
    title: str
    description: str
    domain: str
    keywords: List[str]
    language: str = Field(..., pattern=r"^[a-z]{2}-[A-Z]{2}$")
    created_at: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    updated_at: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    author: str
    source: str
    section: str
    target_audience: List[str]
    reading_level: str
    estimated_reading_time_minutes: int = Field(..., ge=0)


class SourceMetadata(BaseModel):
    """Source document metadata."""
    document_name: str
    extraction_method: str = Field(..., pattern=r"^(copy_paste|ocr|api|manual|import)$")
    page_number: Optional[int] = Field(None, ge=1)
    source_format: Optional[str] = None


class MetadataTwin(BaseModel):
    """Complete metadata twin JSON schema (Pydantic v2)."""

    version: str = Field(..., pattern=r"^\d+\.\d+\.\d+$")
    content_id: str = Field(..., pattern=r"^\d{3}-[a-z0-9-]+-[a-f0-9]{4}$")
    component: str = Field(..., pattern=r"^(plaintext|callouts|docks|tradeoffs|tables|data|faqs|diagrams|disclaimers|others)$")
    original_text: str = Field(..., min_length=1)
    transformed_text: str = Field(..., min_length=1)
    metadata: Metadata
    source_metadata: SourceMetadata
    placeholders: List[Placeholder]
    transformations: List[Transformation]
    brandguide_compliance: BrandguideCompliance
    quality_metrics: QualityMetrics
    relationships: Relationships
    warnings: List[str]
    review_status: ReviewStatus
    audit: Audit

    @field_validator('original_text', 'transformed_text')
    @classmethod
    def validate_text_not_empty(cls, v: str) -> str:
        """Ensure text fields are not empty or whitespace only."""
        if not v.strip():
            raise ValueError("Text cannot be empty or whitespace only")
        return v
