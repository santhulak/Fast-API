
from pydantic import BaseModel
#create a class which describes bank notes measurements

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis:float
    entropy: float
    