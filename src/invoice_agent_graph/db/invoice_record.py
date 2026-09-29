from enum import Enum
from sqlalchemy import Integer
from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, String, Text, func, Integer, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from invoice_agent_graph.db.base import Base

class InvoiceRecordStatus(Enum):
    FETCHED = "FETCHED"
    PARSED = "PARSED"
    VALIDATED = "VALIDATED"
    SAVED = "SAVED"
    FAILED = "FAILED"

class InvoiceRecord(Base):
    __tablename__ = "invoice_records"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    process_id: Mapped[str] = mapped_column(String, nullable=False, unique=True, index=True)
    file_path: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[InvoiceRecordStatus] = mapped_column(
        SQLEnum(
            InvoiceRecordStatus,
            native_enum=False,
            values_callable=lambda obj: [item.value for item in obj],
        ),
        default=InvoiceRecordStatus.FETCHED,
        nullable=False,
    )
    vendor_email: Mapped[str] = mapped_column(String, nullable=True)
    actual_content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    parsed_content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    note: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )