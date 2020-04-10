from flask.blueprints import Blueprint
from .models import Track
from flask import request, jsonify

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/tracks/")
def get_all_tracks():
    """ return all tracks """
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 20, type=int)

    tracks_pg = Track.query.paginate(page=page,
                                     per_page=per_page,
                                     max_per_page=100)

    data = {
        "items": [item.to_dict() for item in tracks_pg.items],
        "has_next": tracks_pg.has_next,
        "has_prev": tracks_pg.has_prev,
        "page": tracks_pg.page,
        "pages": tracks_pg.pages,
        "total": tracks_pg.total
    }

    return jsonify(data)
