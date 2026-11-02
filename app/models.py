from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class loanDB(Base):
    __tablename__ = "loans"
    id: Mapped[int]=mapped_column(primary_key=True, index=True)
    equipment_id: Mapped[int]=mapped_column(Integer, nullable=False)
    borrower_name: Mapped[str]=mapped_column(String(60), nullable=False)
    loan_days: Mapped[int]=mapped_column(Integer, nullable=False) # fix the integer limit
    purpose: Mapped[str]=mapped_column(String(100), nullable=False)
    purpose: Mapped[str]=mapped_column(String(40), nullable=False)
