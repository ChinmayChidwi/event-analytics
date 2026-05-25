from fastapi import APIRouter, Depends

from app.api.deps.auth import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "role": current_user.role,
        "organization_id": str(
            current_user.organization_id
        )
    }   