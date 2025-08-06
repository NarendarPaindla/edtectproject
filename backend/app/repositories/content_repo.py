from typing import Optional, List
from bson import ObjectId
from ..database import db
from ..models.content import ContentCreate, ContentUpdate

async def list_content(skip: int = 0, limit: int = 50) -> List[dict]:
    cursor = db.content.find().skip(skip).limit(limit)
    return await cursor.to_list(length=limit)

async def get_content(content_id: str) -> Optional[dict]:
    return await db.content.find_one({"_id": ObjectId(content_id)})

async def create_content(data: ContentCreate, creator_id: str) -> dict:
    payload = data.dict()
    payload["created_by"] = ObjectId(creator_id)
    result = await db.content.insert_one(payload)
    return await get_content(str(result.inserted_id))

async def update_content(content_id: str, data: ContentUpdate) -> Optional[dict]:
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    if not update_data:
        return await get_content(content_id)
    await db.content.update_one(
        {"_id": ObjectId(content_id)},
        {"$set": update_data}
    )
    return await get_content(content_id)

async def delete_content(content_id: str) -> bool:
    res = await db.content.delete_one({"_id": ObjectId(content_id)})
    return res.deleted_count == 1