from flask import jsonify, request
from app import db, app
from app.models import Participant, Event, Location, Enrollment


@app.route("/locations/", methods=["GET"])
def api_get_locations():
    """ GET /locations/ – выводит список городов или локаций, пока выведите [] """
    locations = []
    return jsonify(locations)


@app.route("/events/", methods=["GET"])
def api_get_events():
    """ GET /events/ – выводит список ближайших событий в городе, пока выведите []
    """
    events = []
    return jsonify(events)


@app.route("/enrollments/<int:event_id>/", methods=["POST"])
def api_post_enrollments(event_id):
    """ POST /enrollments/?id=event_id – принимает заявку на участие в событии, пока выведите {"status":"success"}
    """
    enrollment = {"status": "enrollment success"}
    return jsonify(enrollment)


@app.route("/enrollments/<int:event_id>/", methods=["DELETE"])
def api_delete_enrollments(event_id):
    """ DELETE /enrollments/?id=event_id – отзывает заявку на участие в событии, пока выведите {"status":"success"}
    """
    enrollment = {"status": "enrollment deleted successfully"}
    return jsonify(enrollment)


@app.route("/register/", methods=["POST"])
def api_post_register():
    """ POST /register/ – регистрирует пользователя, пока выведите {"status":"ok","id":1}
    """
    user = {"status": "ok", "id": 1}
    return jsonify(user)


@app.route("/auth/", methods=["POST"])
def api_post_auth():
    """ POST /auth/ – проводит аутентификацию пользователя, пока выведите {"status":"success","key":111111111}
    """
    auth = {"status": "success", "key": 111111111}
    return jsonify(auth)


@app.route("/profile/", methods=["GET"])
def api_get_profile():
    """ GET /profile/  – возвращает информацию о профиле пользователя,
        пока выведите {"id":1,"picture":"","city":"nsk","about":"", enrollments:[]}
    """
    user_profile = {"id": 1, "picture": "", "city": "nsk", "about": "", 'enrollments': []}
    return jsonify(user_profile)


@app.route("/books/<int:book_id>/", methods=["GET"])
def api_get(book_id):
    """ Получить одну книгу по ID """
    print('Получить одну книгу по ID')
    book = db.session.query(Book).get(book_id)
    if book:
        return jsonify(book.serialize)
    return jsonify(), 404


@app.route("/books/all/", methods=["GET"])
def api_books_list():
    """ Получить список всех книг """
    print('Получить список всех книг')
    books = db.session.query(Book)
    books_dict = []
    for book in books:
        books_dict.append(book.serialize)
    return jsonify(books_dict), 404


@app.route("/books/filtered/", methods=["GET"])
def api_books_filtered_list():
    """ Получить список всех книг с фильтрацией по параметру language """
    print('Получить список всех книг с фильтрацией по параметру language')
    language = request.args.get("language")
    print(language)
    books_dict = []
    if language:
        books = db.session.query(Book)
        books = books.filter(Book.language == language).all()
        for book in books:
            books_dict.append(book.serialize)
        print(books_dict)
    return jsonify(books_dict), 404


@app.route("/books/sorted/", methods=["GET"])
def api_books_sorted_list():
    sort = request.args.get("sort")
    if not sort:
        return jsonify({'Error': 'Нет такого параметра!'}), 404
    if not hasattr(Book, sort):
        return jsonify(), 500
    books = db.session.query(Book)
    books = books.order_by(getattr(Book, sort))
    books_dict = []
    for book in books:
        books_dict.append(book.serialize)
    return jsonify(books_dict)
