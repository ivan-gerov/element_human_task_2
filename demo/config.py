"""Configuration module."""
import os


class Config:
    """Configuration object."""

    LOG_LEVEL = os.environ.get("PIPELINE_LOG_LEVEL", "INFO")
    DATABASE_URI = os.environ.get("PIPELINE_DB_URL", "sqlite://")
