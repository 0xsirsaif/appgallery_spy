from fastapi import FastAPI, Depends
from pydantic import BaseModel
import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from datetime import datetime


app = FastAPI()


def get_db() -> Collection:
    client = MongoClient("mongodb://db:27017")
    db = client["AppGallery"]
    review_collection = db["review"]
    return review_collection


class RecentReviewsRequest(BaseModel):
    count: int


class ReviewResponse(BaseModel):
    username: str
    date: datetime
    review_text: str
    rating: int


@app.post("/reviews/recent")
async def get_recent_reviews(request: RecentReviewsRequest, review_collection: Collection = Depends(get_db)):
    count = request.count

    recent_reviews = review_collection.find().sort("date", pymongo.DESCENDING).limit(count)
    reviews = [
        ReviewResponse(
            username=review["username"],
            date=review["date"],
            review_text=review["review_text"],
            rating=review["rating"]
        )
        for review in recent_reviews
    ]

    return reviews


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
