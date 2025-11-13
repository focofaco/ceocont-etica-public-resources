"""Pydantic v2 models for chunks.json validation."""

from typing import List
from pydantic import BaseModel, Field


class SourceMetadata(BaseModel):
    """Source document metadata."""
    extraction_method: str = Field(..., pattern=r"^(copy_paste|ocr|api|manual|import)$")
    page_number: int = Field(..., ge=1)
    source_format: str


class Fragment(BaseModel):
    """Fragment information."""
    fragment_id: str = Field(..., pattern=r"^chunk_\d+_frag_\d+$")
    seq: int = Field(..., ge=1)
    component: str = Field(..., pattern=r"^(plaintext|callouts|docks|tradeoffs|tables|data|faqs|diagrams|disclaimers|others)$")
    content_id: str = Field(..., pattern=r"^\d{3}-[a-z0-9-]+-[a-f0-9]{4}$")
    title: str
    path_txt: str = Field(..., pattern=r"^online-resources/raw-text/.+\.txt$")
    path_json: str = Field(..., pattern=r"^online-resources/raw-text/.+\.json$")
    sha256_txt: str = Field(..., pattern=r"^[a-f0-9]{64}$")
    word_count: int = Field(..., ge=0)
    character_count: int = Field(..., ge=0)
    transformations_applied: List[str]
    review_status: str = Field(..., pattern=r"^(pending|approved|rejected|needs_review)$")


class Chunk(BaseModel):
    """Chunk information."""
    chunk_id: str = Field(..., pattern=r"^chunk_\d+$")
    status: str = Field(..., pattern=r"^(pending|processing|completed|failed)$")
    ingested_at: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    source_document: str
    source_metadata: SourceMetadata
    fragments_generated: int = Field(..., ge=0)
    fragments: List[Fragment]


class ComponentDistribution(BaseModel):
    """Component distribution counts."""
    plaintext: int = Field(..., ge=0)
    callouts: int = Field(..., ge=0)
    docks: int = Field(..., ge=0)
    tradeoffs: int = Field(..., ge=0)
    tables: int = Field(..., ge=0)
    data: int = Field(..., ge=0)
    faqs: int = Field(..., ge=0)
    diagrams: int = Field(..., ge=0)
    disclaimers: int = Field(..., ge=0)
    others: int = Field(..., ge=0)


class ComponentDistributionPercentage(BaseModel):
    """Component distribution percentages."""
    plaintext: float = Field(..., ge=0.0, le=100.0)
    callouts: float = Field(..., ge=0.0, le=100.0)
    docks: float = Field(..., ge=0.0, le=100.0)
    tradeoffs: float = Field(..., ge=0.0, le=100.0)
    tables: float = Field(..., ge=0.0, le=100.0)
    data: float = Field(..., ge=0.0, le=100.0)
    faqs: float = Field(..., ge=0.0, le=100.0)
    diagrams: float = Field(..., ge=0.0, le=100.0)
    disclaimers: float = Field(..., ge=0.0, le=100.0)
    others: float = Field(..., ge=0.0, le=100.0)


class TargetRange(BaseModel):
    """Target range for distribution."""
    min: float = Field(..., ge=0.0, le=100.0)
    max: float = Field(..., ge=0.0, le=100.0)


class TargetDistribution(BaseModel):
    """Target distribution constraints."""
    plaintext: TargetRange
    others_combined: TargetRange


class ChunksManifest(BaseModel):
    """Complete chunks.json manifest schema (Pydantic v2)."""

    version: str = Field(..., pattern=r"^\d+\.\d+\.\d+$")
    last_updated: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    total_chunks: int = Field(..., ge=0)
    total_fragments: int = Field(..., ge=0)
    chunks: List[Chunk]
    component_distribution: ComponentDistribution
    component_distribution_percentage: ComponentDistributionPercentage
    target_distribution: TargetDistribution
    saturation_warnings: List[str]
    placeholders_inventory: List[str]
