from app.models.rol import Rol
from app.repositories.base_repository import BaseRepository


class RolRepository(BaseRepository[Rol]):
    """
    Repositorio de roles.
    """

    def __init__(self):
        super().__init__(Rol)