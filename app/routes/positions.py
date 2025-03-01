from flask import Blueprint , render_template,request,redirect
from app.db import Session,Position
from app.data.password import ADMIN_PASS


position_route = Blueprint("positions",__name__,url_prefix="/positions")
@position_route.get("/")
@position_route.post("/")
def add_position():
    msg = ""
    block = False
    if request.method == "POST":
        name = request.form.get("name")

        password = request.form.get("password")
        if password == ADMIN_PASS:
            with Session() as session:
                position = Position(name=name)
                session.add(position)
                session.commit()
                msg = "Посада успішно додана"
        else:
            block = True

    return render_template("position.html", block=block, msg=msg)