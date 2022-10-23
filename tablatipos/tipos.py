from enum import Enum

# https://areajugones.sport.es/videojuegos/tabla-de-tipos-de-pokemon-ante-cuales-es-fuerte-y-debil-cada-uno/


class Tipos(Enum):
    ACERO = 'acero'
    AGUA = 'agua'
    BICHO = 'bicho'
    DRAGON = 'dragon'
    ELECTRICO = 'electrico'
    FANTASMA = 'fantasma'
    FUEGO = 'fuego'
    HADA = 'hada'
    HIELO = 'hielo'
    LUCHA = 'lucha'
    NORMAL = 'normal'
    PLANTA = 'planta'
    PSIQUICO = 'psiquico'
    SINIESTRO = 'siniestro'
    TIERRA = 'tierra'
    VENENO = 'veneno'
    VOLADOR = 'volador'
    ROCA = 'roca'
    NONE = 'ninguno'


class ModelTipo(object):
    """
        Clase abstracta para tipos
    """
    eficaz_contra = ''
    poco_eficaz_contra = ''
    resistente_ante = ''
    debil_ante = ''

    def get_eficaz_contra(self):
        return ', '.join([i.value for i in self.eficaz_contra])

    def get_poco_eficaz_contra(self):
        return ', '.join([i.value for i in self.poco_eficaz_contra])

    def get_resistente_ante(self):
        return ', '.join([i.value for i in self.resistente_ante])

    def get_debil_ante(self):
        return ', '.join([i.value for i in self.debil_ante])


class Acero(ModelTipo):
    eficaz_contra = Tipos.HADA, Tipos.HIELO, Tipos.ROCA
    poco_eficaz_contra = Tipos.ACERO, Tipos.AGUA, Tipos.ELECTRICO, Tipos.FUEGO
    resistente_ante = Tipos.ACERO, Tipos.BICHO, Tipos.DRAGON, Tipos.HADA, Tipos.HIELO, Tipos.NORMAL, Tipos.PLANTA, Tipos.PSIQUICO, Tipos.ROCA, Tipos.VENENO, Tipos.VOLADOR
    debil_ante = Tipos.FUEGO, Tipos.LUCHA, Tipos.TIERRA


class Agua(ModelTipo):
    eficaz_contra = Tipos.FUEGO, Tipos.ROCA, Tipos.TIERRA
    poco_eficaz_contra = Tipos.AGUA, Tipos.DRAGON, Tipos.PLANTA
    resistente_ante = Tipos.ACERO, Tipos.AGUA, Tipos.FUEGO, Tipos.HIELO
    debil_ante = Tipos.ELECTRICO, Tipos.PLANTA


class Bicho(ModelTipo):
    eficaz_contra = Tipos.PLANTA, Tipos.PSIQUICO, Tipos.SINIESTRO
    poco_eficaz_contra = Tipos.ACERO, Tipos.FANTASMA, Tipos.FUEGO, Tipos.HADA, Tipos.LUCHA, Tipos.VENENO, Tipos.VOLADOR
    resistente_ante = Tipos.LUCHA, Tipos.PLANTA, Tipos.TIERRA
    debil_ante = Tipos.FUEGO, Tipos.ROCA, Tipos.VOLADOR


class Dragon(ModelTipo):
    eficaz_contra = Tipos.DRAGON,
    poco_eficaz_contra = Tipos.ACERO, Tipos.HADA
    resistente_ante = Tipos.AGUA, Tipos.ELECTRICO, Tipos.FUEGO, Tipos.PLANTA
    debil_ante = Tipos.DRAGON, Tipos.HADA, Tipos.HIELO


class Electrico(ModelTipo):
    eficaz_contra = Tipos.AGUA, Tipos.VOLADOR
    poco_eficaz_contra = Tipos.DRAGON, Tipos.ELECTRICO, Tipos.PLANTA, Tipos.TIERRA
    resistente_ante = Tipos.ACERO, Tipos.ELECTRICO, Tipos.VOLADOR
    debil_ante = Tipos.TIERRA,


class Fantasma(ModelTipo):
    eficaz_contra = Tipos.FANTASMA, Tipos.PSIQUICO
    poco_eficaz_contra = Tipos.NORMAL, Tipos.SINIESTRO
    resistente_ante = Tipos.BICHO, Tipos.LUCHA, Tipos.NORMAL, Tipos.VENENO
    debil_ante = Tipos.FANTASMA, Tipos.SINIESTRO


class Fuego(ModelTipo):
    eficaz_contra = Tipos.ACERO, Tipos.BICHO, Tipos.HIELO, Tipos.PLANTA
    poco_eficaz_contra = Tipos.AGUA, Tipos.DRAGON, Tipos.FUEGO, Tipos.ROCA
    resistente_ante = Tipos.ACERO, Tipos.BICHO, Tipos.FUEGO, Tipos.HADA, Tipos.HIELO, Tipos.PLANTA
    debil_ante = Tipos.AGUA, Tipos.ROCA, Tipos.TIERRA


class Hada(ModelTipo):
    eficaz_contra = Tipos.DRAGON, Tipos.LUCHA, Tipos.SINIESTRO
    poco_eficaz_contra = Tipos.ACERO, Tipos.FUEGO, Tipos.VENENO
    resistente_ante = Tipos.BICHO, Tipos.DRAGON, Tipos.LUCHA, Tipos.SINIESTRO
    debil_ante = Tipos.ACERO, Tipos.VENENO


class Hielo(ModelTipo):
    eficaz_contra = Tipos.DRAGON, Tipos.PLANTA, Tipos.TIERRA, Tipos.VOLADOR
    poco_eficaz_contra = Tipos.ACERO, Tipos.AGUA, Tipos.FUEGO, Tipos.HIELO
    resistente_ante = Tipos.HIELO,
    debil_ante = Tipos.ACERO, Tipos.FUEGO, Tipos.LUCHA, Tipos.ROCA


class Lucha(ModelTipo):
    eficaz_contra = Tipos.ACERO, Tipos.HIELO, Tipos.NORMAL, Tipos.ROCA, Tipos.SINIESTRO
    poco_eficaz_contra = Tipos.BICHO, Tipos.FANTASMA, Tipos.HADA, Tipos.PSIQUICO, Tipos.VENENO, Tipos.VOLADOR
    resistente_ante = Tipos.BICHO, Tipos.ROCA, Tipos.SINIESTRO
    debil_ante = Tipos.HADA, Tipos.PSIQUICO, Tipos.VOLADOR


class Normal(ModelTipo):
    eficaz_contra = Tipos.NONE,
    poco_eficaz_contra = Tipos.ACERO, Tipos.FANTASMA, Tipos.ROCA
    resistente_ante = Tipos.FANTASMA
    debil_ante = Tipos.LUCHA,


class Planta(ModelTipo):
    eficaz_contra = Tipos.AGUA, Tipos.ROCA, Tipos.TIERRA
    poco_eficaz_contra = Tipos.ACERO, Tipos.BICHO, Tipos.DRAGON, Tipos.FUEGO, Tipos.PLANTA, Tipos.VENENO, Tipos.VOLADOR
    resistente_ante = Tipos.ACERO, Tipos.ELECTRICO, Tipos.PLANTA, Tipos.TIERRA
    debil_ante = Tipos.FUEGO, Tipos.HIELO, Tipos.VENENO, Tipos.VOLADOR


class Psiquico(ModelTipo):
    eficaz_contra = Tipos.LUCHA, Tipos.VENENO
    poco_eficaz_contra = Tipos.ACERO, Tipos.PSIQUICO, Tipos.SINIESTRO
    resistente_ante = Tipos.LUCHA, Tipos.PSIQUICO
    debil_ante = Tipos.BICHO, Tipos.FANTASMA, Tipos.SINIESTRO


class Roca(ModelTipo):
    eficaz_contra = Tipos.BICHO, Tipos.FUEGO, Tipos.HIELO, Tipos.VOLADOR
    poco_eficaz_contra = Tipos.ACERO, Tipos.LUCHA, Tipos.TIERRA
    resistente_ante = Tipos.FUEGO, Tipos.NORMAL, Tipos.VENENO, Tipos.VOLADOR
    debil_ante = Tipos.ACERO, Tipos.AGUA, Tipos.LUCHA, Tipos.PLANTA, Tipos.TIERRA


class Siniestro(ModelTipo):
    eficaz_contra = Tipos.FANTASMA, Tipos.PSIQUICO
    poco_eficaz_contra = Tipos.HADA, Tipos.LUCHA, Tipos.SINIESTRO
    resistente_ante = Tipos.FANTASMA, Tipos.SINIESTRO
    debil_ante = Tipos.BICHO, Tipos.HADA, Tipos.LUCHA


class Tierra(ModelTipo):
    eficaz_contra = Tipos.ACERO, Tipos.ELECTRICO, Tipos.FUEGO, Tipos.ROCA, Tipos.VENENO
    poco_eficaz_contra = Tipos.BICHO, Tipos.PLANTA, Tipos.VOLADOR
    resistente_ante = Tipos.ELECTRICO, Tipos.ROCA, Tipos.VENENO
    debil_ante = Tipos.AGUA, Tipos.HIELO, Tipos.PLANTA


class Veneno(ModelTipo):
    eficaz_contra = Tipos.HADA, Tipos.PLANTA
    poco_eficaz_contra = Tipos.ACERO, Tipos.FANTASMA, Tipos.ROCA, Tipos.TIERRA, Tipos.VENENO
    resistente_ante = Tipos.BICHO, Tipos.HADA, Tipos.LUCHA, Tipos.PLANTA, Tipos.VENENO
    debil_ante = Tipos.PSIQUICO, Tipos.TIERRA


class Volador(ModelTipo):
    eficaz_contra = Tipos.BICHO, Tipos.LUCHA, Tipos.PLANTA
    poco_eficaz_contra = Tipos.ACERO, Tipos.ELECTRICO, Tipos.ROCA
    resistente_ante = Tipos.BICHO, Tipos.LUCHA, Tipos.PLANTA, Tipos.TIERRA
    debil_ante = Tipos.ELECTRICO, Tipos.HIELO, Tipos.ROCA