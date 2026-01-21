# crud.py
from sqlmodel import select
from db import async_session
from models import Item
from sqlmodel.ext.asyncio.session import AsyncSession

async def create_item(item: Item) -> Item:
    async with async_session() as session:
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item

async def get_item(item_id: int) -> Item | None:
    async with async_session() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        return result.scalar_one_or_none()

async def update_item(item_id: int, name: str | None = None, description: str | None = None) -> Item | None:
    async with async_session() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        item = result.scalar_one_or_none()
        if not item:
            return None
        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item

async def delete_item(item_id: int) -> Item | None:
    async with async_session() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        item = result.scalar_one_or_none()
        if not item:
            return None
        await session.delete(item)
        await session.commit()
        return item
