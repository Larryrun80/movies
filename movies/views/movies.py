from flask import (abort,
                   Blueprint,
                   jsonify)

movies = Blueprint('movies', __name__)


@movies.route('/<int:movie_id>')
def get_film_by_id(movie_id):
    from ..models.business.doubanmovies import DoubanMovies
    result = DoubanMovies().get_movie_by_id(movie_id)
    if result:
        return jsonify(result)
    else:
        abort(404)
