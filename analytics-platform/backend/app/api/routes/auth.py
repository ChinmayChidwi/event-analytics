from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.models.user import User
from app.models.organization import Organization

from app.schemas.auth import (
    SignupRequest,
    LoginRequest,
    TokenResponse
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/signup",
    response_model=TokenResponse
)
async def signup(
    request: SignupRequest,
    db: AsyncSession = Depends(get_db)
):

    existing_user = await db.execute(
        select(User).where(
            User.email == request.email
        )
    )

    existing_user = existing_user.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    organization = Organization(
        name=request.organization_name
    )

    db.add(organization)

    await db.flush()

    user = User(
        email=request.email,
        password_hash=hash_password(
            request.password
        ),
        role="Owner",
        organization_id=organization.id
    )

    db.add(user)

    await db.commit()

    access_token = create_access_token({
        "sub": user.email
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(
            User.email == form_data.username
        )
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    valid_password = verify_password(
        form_data.password,
        user.password_hash
    )

    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token({
        "sub": user.email
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }