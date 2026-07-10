from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from models.database import db
from datetime import datetime

class ImageRecord(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    original_image_path: Mapped[str] = mapped_column(db.String(255), nullable=False)
    edited_image_path: Mapped[Optional[str]] = mapped_column(db.String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "original_image_path": self.original_image_path,
            "edited_image_path": self.edited_image_path,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
