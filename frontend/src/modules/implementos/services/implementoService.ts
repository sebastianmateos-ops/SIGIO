import api from "../../../api/axios";

import type { Implemento } from "../types/implemento";
import type { ImplementoFormData } from "../schemas/implementoSchema";

class ImplementoService {
  async listar(): Promise<Implemento[]> {
    const response = await api.get<Implemento[]>(
      "/implementos",
    );

    return response.data;
  }

  async crear(
    datos: ImplementoFormData,
  ): Promise<void> {
    await api.post(
      "/implementos",
      datos,
    );
  }
}

export default new ImplementoService();