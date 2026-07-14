export interface Beneficiario {
  id: number;

  uuid: string;

  codigo: string;

  tipo_documento: string;

  numero_documento: string;

  nombre: string;

  apellido: string;

  fecha_nacimiento: string | null;

  telefono: string | null;

  celular: string | null;

  email: string | null;

  direccion: string | null;

  ciudad: string | null;

  departamento: string | null;

  observaciones: string | null;

  activo: boolean;

  fecha_creacion: string;

  fecha_actualizacion: string | null;
}