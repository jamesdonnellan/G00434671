from typing import Annotated
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints, StrictBool

# id
# equipment_id
# borrower_name
# loan_days
# purpose
# status

NameStr=Annotated[str, StringConstraints(min_length=2, max_length=60)]
PurposeStr=Annotated[str,StringConstraints(min_length=5, max_length=100)]


class loanCreate(BaseModel):
    equipment_id: int
    borrower_name: NameStr
    loan_days: int=Field(gt=1, lt=14)
    purpose: PurposeStr
    #status: StatusStr

class loanRead(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:int
    equipment_id: int
    borrower_name: NameStr
    loan_days: int=Field(gt=1, lt=14)
    purpose: PurposeStr
   # status: StatusStr