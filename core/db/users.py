from sqlalchemy.orm import Mapped, relationship

from .models import Base


class UserSingIn(Base):
    __tablename__ = 'registration'

    name: Mapped[str]
    email: Mapped[str]
    passsword: Mapped[str]


class UserLogIn(Base):
    __tablename__ = 'authorization'

    user_id: Mapped["UserSingIn"] = relationship(
        back_populates='authorization', cascade='all, delete-orphan'
    )
    name: Mapped[str]
    passsword: Mapped[str]
