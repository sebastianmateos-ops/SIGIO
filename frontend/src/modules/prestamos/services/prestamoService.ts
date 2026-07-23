import api from "../../../api/axios";

export interface ImplementoPrestamo {
  id: number;
  codigo: string;
  marca: string | null;
  modelo: string | null;
}

export interface BeneficiarioPrestamo {
  id: number;
  codigo: string;
  nombre: string;
  apellido: string;
}

export interface Prestamo {
  id: number;
  uuid: string;

  implemento: ImplementoPrestamo;

  beneficiario: BeneficiarioPrestamo;

  fecha_prestamo: string;
  fecha_devolucion: string | null;
  observaciones: string | null;
  activo: boolean;
}

export interface PrestamoCreate {
  implemento_id: number;
  beneficiario_id: number;
  fecha_prestamo: string;
  observaciones?: string;
}

export interface PrestamoUpdate {
  fecha_devolucion: string;
  observaciones?: string;
}

class PrestamoService {
  async listar(): Promise<Prestamo[]> {
    const response = await api.get<Prestamo[]>("/prestamos");
    return response.data;
  }

  async listarActivos(): Promise<Prestamo[]> {
    const response = await api.get<Prestamo[]>("/prestamos/activos");
    return response.data;
  }

  async obtener(id: number): Promise<Prestamo> {
    const response = await api.get<Prestamo>(
      `/prestamos/${id}`,
    );

    return response.data;
  }

  async crear(
    datos: PrestamoCreate,
  ): Promise<Prestamo> {
    const response = await api.post<Prestamo>(
      "/prestamos",
      datos,
    );

    return response.data;
  }

  async devolver(
    id: number,
    datos: PrestamoUpdate,
  ): Promise<Prestamo> {
    const response = await api.put<Prestamo>(
      `/prestamos/${id}/devolucion`,
      datos,
    );

    return response.data;
  }
}

export default new PrestamoService();