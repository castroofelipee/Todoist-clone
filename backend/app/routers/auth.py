from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer
from fastapi import status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import requests
import os

router = APIRouter()

GITHUB_CLIENT_ID = "Ov23liBZCFARY6OmNKHm"
GITHUB_CLIENT_SECRET = os.getenv("**********************************")
OAUTH_CALLBACK_URL = "http://localhost:8000/auth/callback"


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://github.com/login/oauth/authorize",
    tokenUrl="https://github.com/login/oauth/access_token",
)


class OAuth2Token(BaseModel):
    access_token: str
    token_type: str


@router.get("/login")
def login():
    redirect_url = f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={OAUTH_CALLBACK_URL}"
    return RedirectResponse(redirect_url)


@router.get("/callback")
def callback(code: str):
    token_url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    data = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
        "redirect_uri": OAUTH_CALLBACK_URL,
    }

    response = requests.post(token_url, headers=headers, data=data)
    response_data = response.json()

    if "access_token" not in response_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error fetching access token",
        )

    access_token = response_data["access_token"]

    # Redirects to task page
    return RedirectResponse(url="http://localhost:3000/tasks")


@router.get("/profile")
def read_profile(token: str = Depends(oauth2_scheme)):
    response = requests.get(
        "https://api.github.com/user", headers={"Authorization": f"Bearer {token}"}
    )

    profile_data = response.json()
    return profile_data
