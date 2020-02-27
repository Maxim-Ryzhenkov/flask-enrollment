from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, Admin, AdminIndexView, expose
from flask_login import current_user, login_required
from app import db, app  # , mail
# from flask_mail import Message
from app.models import Participant, Event, Location, Enrollment
from flask import abort, request, flash


# from app.forms import MailForm


class DashboardView(AdminIndexView):
    @expose('/')
    # @login_required
    def index(self):
        #     if not current_user.is_authenticated or not current_user.is_admin:
        #         abort(404)
        return self.render('admin/dashboard.html')


class MailerView(BaseView):
    @expose('/', methods=['GET', 'POST'])
    #    @login_required
    def mailer(self):
        pass
        # form = MailForm()
        #
        # if request.method == 'POST':
        #     # отправка письма
        #     subject = form.subject.data
        #     recipient = form.recipient.data
        #     text_body = form.message.data
        #     msg = Message(
        #         subject,
        #         sender='ryzhenkov.maksim@yandex.ru',
        #         recipients=[recipient, ]
        #     )
        #     msg.body = text_body
        #     mail.send(msg)
        #     flash("Сообщение отправлено")
        #     return self.render('admin/mail_sender/sanded.html')
        # return self.render('admin/mail_sender/send.html', form=form)


class EventView(ModelView):
    pass
    # def is_accessible(self):
    #     return current_user.is_authenticated and current_user.is_admin


class ParticipantView(ModelView):
    pass
    # def is_accessible(self):
    #     return current_user.is_authenticated and current_user.is_admin


class LocationView(ModelView):
    pass
    # def is_accessible(self):
    #    return current_user.is_authenticated and current_user.is_admin


class EnrollmentView(ModelView):
    pass
    # def is_accessible(self):
    #     return current_user.is_authenticated and current_user.is_admin


admin = Admin(app, template_mode='bootstrap3', name='Админка', index_view=DashboardView(name='Статистика'))
admin.add_view(EventView(Event, db.session, name='События'))
admin.add_view(ParticipantView(Participant, db.session, name='Участники'))
admin.add_view(LocationView(Location, db.session, name='Города'))
admin.add_view(EnrollmentView(Enrollment, db.session, name='Заявки'))
admin.add_view(MailerView(name='Отправить письмо', endpoint='mail_sender'))
