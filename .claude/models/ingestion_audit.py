"""Pydantic v2 models for ingestion-audit.json validation."""

from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class ComponentStats(BaseModel):
    """Component distribution statistics."""
    count: int = Field(..., ge=0)
    percentage: float = Field(..., ge=0.0, le=100.0)


class TargetRange(BaseModel):
    """Target range for component distribution."""
    min: float
    max: float


class PlaintextTarget(BaseModel):
    """Plaintext target distribution (70-80%)."""
    min: Literal[70.0] = 70.0
    max: Literal[80.0] = 80.0


class OthersCombinedTarget(BaseModel):
    """Others combined target distribution (20-30%)."""
    min: Literal[20.0] = 20.0
    max: Literal[30.0] = 30.0


class TargetDistribution(BaseModel):
    """Target distribution constraints."""
    plaintext: PlaintextTarget
    others_combined: OthersCombinedTarget


class SaturationWarning(BaseModel):
    """Component saturation warning."""
    component: str
    current: float
    threshold: float
    message: str


class ComponentStatsContainer(BaseModel):
    """Container for component statistics and warnings."""
    current_distribution: Optional[dict[str, ComponentStats]] = None
    target_distribution: Optional[TargetDistribution] = None
    saturation_warnings: Optional[List[SaturationWarning]] = None


class AuditMetadata(BaseModel):
    """Metadata for the audit trail."""
    schema_version: Literal["1.0.0"] = "1.0.0"
    created_at: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    last_updated: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    total_chunks: Optional[int] = Field(None, ge=0)
    total_fragments: Optional[int] = Field(None, ge=0)
    component_stats: Optional[ComponentStatsContainer] = None


class SourceMetadata(BaseModel):
    """Source metadata for chunk traceability."""
    document_name: Optional[str] = None
    page_number: Optional[int] = Field(None, ge=1)
    section_number: Optional[str] = None
    extraction_method: Optional[str] = Field(
        None,
        pattern=r"^(manual_paste|ocr|api|file_upload|copy_paste)$"
    )
    source_file_sha256: Optional[str] = Field(None, pattern=r"^[a-f0-9]{64}$")


class Transformation(BaseModel):
    """Transformation applied to fragment."""
    type: str = Field(
        ...,
        pattern=r"^(deduplication|line_breaking|paragraph_splitting|tone_adjustment|modal_replacement|voice_conversion|conciseness|passive_to_active|formality_adjustment|normalization|placeholder_preservation|encoding_fix|whitespace_cleanup|formatting_componentization)$"
    )
    description: str
    before: Optional[str] = None
    after: Optional[str] = None


class BrandguideCompliance(BaseModel):
    """Brandguide compliance metrics."""
    overall_score: Optional[float] = Field(None, ge=0.0, le=1.0)
    voice_check: Optional[float] = Field(None, ge=0.0, le=1.0)
    tone_check: Optional[float] = Field(None, ge=0.0, le=1.0)
    modals_allowed: Optional[bool] = None
    modals_forbidden_detected: Optional[List[str]] = None
    max_line_length_ok: Optional[bool] = None
    max_file_size_ok: Optional[bool] = None
    utf8_lf_ok: Optional[bool] = None
    issues: Optional[List[str]] = None


class ManualOverride(BaseModel):
    """Manual override record."""
    override_type: str = Field(
        ...,
        pattern=r"^(component_change|transformation_skipped|classification_corrected|manual_edit)$"
    )
    reason: str
    timestamp: Optional[str] = Field(None, pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class QualityMetrics(BaseModel):
    """Text quality metrics."""
    readability_score: Optional[float] = Field(None, ge=0.0, le=100.0)
    avg_sentence_length: Optional[float] = Field(None, ge=0.0)
    avg_word_length: Optional[float] = Field(None, ge=0.0)
    technical_term_density: Optional[float] = Field(None, ge=0.0, le=1.0)
    passive_voice_ratio: Optional[float] = Field(None, ge=0.0, le=1.0)


class RelatedFragment(BaseModel):
    """Related fragment relationship."""
    frag_id: str = Field(..., pattern=r"^chunk_\d{2,}_frag_\d{3}$")
    relationship_type: str = Field(
        ...,
        pattern=r"^(continuation|alternative|prerequisite|related|contradicts)$"
    )
    description: Optional[str] = None


class Relationships(BaseModel):
    """Fragment relationships."""
    references: Optional[List[str]] = None
    referenced_by: Optional[List[str]] = None
    related_fragments: Optional[List[RelatedFragment]] = None


class Warning(BaseModel):
    """Warning message."""
    type: str = Field(
        ...,
        pattern=r"^(long_line|large_file|mixed_language|low_confidence|placeholder_unresolved|formatting_issue|encoding_warning|component_saturation)$"
    )
    message: str
    severity: str = Field(..., pattern=r"^(low|medium|high)$")
    line_number: Optional[int] = Field(None, ge=1)


class ReviewStatus(BaseModel):
    """Review status tracking."""
    status: Optional[str] = Field(None, pattern=r"^(pending|approved|rejected|needs_revision)$")
    reviewed_by: Optional[str] = Field(None, pattern=r"^(human|auto)$")
    reviewed_at: Optional[str] = Field(None, pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    review_notes: Optional[str] = None


class AlternativeComponent(BaseModel):
    """Alternative component classification."""
    component: str
    confidence: float = Field(..., ge=0.0, le=1.0)


class Fragment(BaseModel):
    """Fragment within a chunk."""
    frag_id: str = Field(..., pattern=r"^chunk_\d{2,}_frag_\d{3}$")
    seq: int = Field(..., ge=1)
    section_title: Optional[str] = None
    component: str = Field(
        ...,
        pattern=r"^(plaintext|callouts|docks|tradeoffs|tables|data|faqs|diagrams|disclaimers|others|header_h1|header_h2|header_h3)$"
    )
    classification_confidence: float = Field(..., ge=0.0, le=1.0)
    classification_reasoning: Optional[str] = None
    alternative_components: Optional[List[AlternativeComponent]] = None
    original_text: str
    original_word_count: Optional[int] = Field(None, ge=0)
    original_char_count: Optional[int] = Field(None, ge=0)
    transformed_text: str
    transformed_word_count: Optional[int] = Field(None, ge=0)
    transformed_char_count: Optional[int] = Field(None, ge=0)
    transformations: Optional[List[Transformation]] = None
    brandguide_compliance: Optional[BrandguideCompliance] = None
    manual_overrides: Optional[List[ManualOverride]] = None
    quality_metrics: Optional[QualityMetrics] = None
    relationships: Optional[Relationships] = None
    warnings: Optional[List[Warning]] = None
    review_status: Optional[ReviewStatus] = None
    final_filename: Optional[str] = Field(None, pattern=r"^\d{3}-[a-z0-9-]+-[a-f0-9]{4}\.txt$")
    final_path: Optional[str] = None
    final_sha256: Optional[str] = Field(None, pattern=r"^[a-f0-9]{64}$")


class Chunk(BaseModel):
    """Ingestion chunk."""
    chunk_id: str = Field(..., pattern=r"^chunk_\d{2,}$")
    ingested_at: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    source_description: Optional[str] = None
    original_text: str
    sha256_original: Optional[str] = Field(None, pattern=r"^[a-f0-9]{64}$")
    word_count: Optional[int] = Field(None, ge=0)
    char_count: Optional[int] = Field(None, ge=0)
    placeholders_detected: Optional[List[str]] = None
    source_metadata: Optional[SourceMetadata] = None
    fragments: List[Fragment] = Field(..., min_length=1)


class IngestionAudit(BaseModel):
    """Complete ingestion audit trail schema (Pydantic v2)."""
    metadata: AuditMetadata
    chunks: List[Chunk]
