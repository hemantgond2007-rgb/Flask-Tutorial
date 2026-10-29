from flask import Blueprint
users_bp=Blueprint(
    "users",
    __name__,
    url_prefix="/users"

)
@users_bp.route("/")
def users():
    return "users page"

@users_bp.route("/profile")
def porfile():
    return  "profile page"