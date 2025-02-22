from pydantic import BaseModel
from typing import List

class VectorQuery(BaseModel):
    query: List[List[float]] 

class SearchResponse(BaseModel):
    distances: List[List[float]]
    indices: List[List[int]]