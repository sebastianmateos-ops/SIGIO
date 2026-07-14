import api from "@/api/axios";

import type { Beneficiario } from "../types/beneficiario";
import type {
  BeneficiarioFormData,
} from "../schemas/beneficiarioSchema";

class BeneficiarioService {
  async listar(): Promise<Beneficiario[]> {
    const response = await api.get<Beneficiario[]>(
      "/beneficiarios",
    );

    return response.data;
  }

  async crear(
    datos: BeneficiarioFormData,
  ): Promise<Beneficiario> {
    const response = await api.post<Beneficiario>(
      "/beneficiarios",
      datos,
    );

    return response.data;
  }

  async actualizar(
    id: number,
    datos: BeneficiarioFormData,
  ): Promise<Beneficiario> {
    const response = await api.put<Beneficiario>(
      `/beneficiarios/${id}`,
      datos,
    );

    return response.data;
  }

  async eliminar(
    id: number,
  ): Promise<void> {
    await api.delete(
      `/beneficiarios/${id}`,
    );
  }

  async buscar(
    texto: string,
  ): Promise<Beneficiario[]> {
    const response = await api.get<Beneficiario[]>(
      "/beneficiarios/buscar",
      {
        params: {
          texto,
        },
      },
    );

    return response.data;
  }
}

export default new BeneficiarioService();